import json
import time
import datetime
import requests

from dataclasses import dataclass
from typing import Tuple, List, Union
from ratelimiter import RateLimiter

# Rate limiters
L_GET_RATE_LIMITER = RateLimiter(max_calls=1, period=2)
L_PUT_RATE_LIMITER = RateLimiter(max_calls=1, period=2)
L_POST_RATE_LIMITER = RateLimiter(max_calls=10, period=60)

L_LOOKUP_RATE_LIMITER = RateLimiter(max_calls=1, period=1)
H_LOOKUP_RATE_LIMITER = RateLimiter(max_calls=400, period=3600)

# Other API restrictions
MAX_URLS_PER_LOOKUP = 100


@dataclass(order=True)
class CategoryReport:
    """
    Class which stores basic information about managed during ZScaler API session url category.
    """
    name: str
    urls_excluded: int = 0
    urls_skipped: int = 0
    urls_added: int = 0
    urls_deleted: int = 0
    urls_total: int = 0


@dataclass(frozen=True, order=True)
class SessionErrors:
    """
    Class which stores basic information about errors happened during ZScaler session.
    """
    error_type: str
    codes: List[int]
    messages: List[str]

    def append_error(self, code: int, message: str):
        """
        Adds provided error code and error message to category.
        :param code:
        :param message:
        :return:
        """
        if message not in self.messages:
            self.messages.append(message)
        if code not in self.codes:
            self.codes.append(code)


class ZscalerSession:
    """
    Class used as interface between user and ZScaler API.
    """
    CLOUD_NAME: str
    BASE_PATH: str
    USERNAME: str
    PASSWORD: str
    API_KEY: str
    URL_QUOTA_MARGIN: int

    session: requests.session
    headers: dict
    result: Union[requests.Response, dict]
    uniqueUrlsProvisioned: int
    remainingUrlsQuota: int
    categoriesLite: List[dict]
    categoriesFull: List[dict]
    sessionReports: List[CategoryReport]
    sessionErrors: List[SessionErrors]

    def __init__(self, cloud_name: str, base_path: str, username: str, password: str, api_key: str,
                 url_quota_margin: int = 0):
        self.CLOUD_NAME, self.BASE_PATH = cloud_name, base_path
        self.USERNAME, self.PASSWORD = username, password
        self.API_KEY = api_key
        self.URL_QUOTA_MARGIN = url_quota_margin

        self.session, self.headers, self.result = create_session(cloud_name, base_path, username, password, api_key)
        if self.result.status_code != 200:
            raise NameError('An error occurred during session initialization')
        self.update_urls_total_number()
        self.categoriesLite: List[dict] = self.get_categories(lite=True)
        self.categoriesFull: List[dict] = self.get_categories()
        self.sessionReports: List[CategoryReport] = []
        self.sessionErrors: List[SessionErrors] = []

        self.needUpdate = False

        self.categoryModificationRequestBody = {
            "superCategory": "USER_DEFINED",
            "configuredName": "string",
            "urls": []
        }

    def get_categories(self, lite: bool = False, custom_only: bool = True) -> List[dict]:
        """Load existing URLs categories. Use boolean 'lite' parameter to load lightweight URLs categories"""
        url = f'{self.CLOUD_NAME}{self.BASE_PATH}/urlCategories'
        url += '/lite' if lite else ''
        url += '?customOnly=True' if custom_only else ''
        with L_GET_RATE_LIMITER:
            self.result = self.session.get(url=url, headers=self.headers)
        self.needUpdate = False
        return self.result.json()

    def update_urls_total_number(self) -> Tuple[int, int]:
        """Get current URL quota"""
        with L_GET_RATE_LIMITER:
            self.result = self.session.get(url=f'{self.CLOUD_NAME}{self.BASE_PATH}/urlCategories/urlQuota',
                                           headers=self.headers).json()
        self.uniqueUrlsProvisioned, self.remainingUrlsQuota = self.result['uniqueUrlsProvisioned'], self.result[
            'remainingUrlsQuota']
        return self.uniqueUrlsProvisioned, self.remainingUrlsQuota

    def delete_urls(self, category_id: str, urls: List[str]):
        """Deletes provided URLs from selected category"""
        data = self.categoryModificationRequestBody
        configuredName = self.get_configured_name(category_id)
        data['urls'] = urls
        data['configuredName'] = configuredName
        with L_PUT_RATE_LIMITER:
            self.result = self.session.put(
                url=f"{self.CLOUD_NAME}{self.BASE_PATH}/urlCategories/{category_id}?action=REMOVE_FROM_LIST",
                data=json.dumps(data), headers=self.headers)

        if self.result.status_code != 200:
            self.add_error(configuredName, self.result.status_code, self.result.text)
            return

        self.needUpdate = True
        self.uniqueUrlsProvisioned, self.remainingUrlsQuota = self.update_urls_total_number()
        self.update_category_report(configuredName, deleted=len(urls))

    def add_urls(self, category_id: str, urls: List[str]):
        """Adds provided URLs from selected category"""
        data = self.categoryModificationRequestBody
        configuredName = self.get_configured_name(category_id)
        data['urls'] = urls
        data['configuredName'] = configuredName
        with L_PUT_RATE_LIMITER:
            self.result = self.session.put(
                url=f"{self.CLOUD_NAME}{self.BASE_PATH}/urlCategories/{category_id}?action=ADD_TO_LIST",
                data=json.dumps(data), headers=self.headers)

        if self.result.status_code != 200 and self.result.json()['message'][:12] == 'Invalid urls':
            # Convert list-like string to actual list
            invalid_urls = self.result.json()['message'][13:]
            invalid_urls = invalid_urls.strip('][').split(',')

            # Add invalid URLs to skipped
            self.update_category_report(configuredName, skipped=len(invalid_urls))
            f = open('../outputs/invalidURLs.txt', 'w')
            f.writelines(invalid_urls)
            urls = [url for url in urls if url not in invalid_urls]
            return self.add_urls(category_id, urls)
        elif self.result.status_code != 200:
            self.add_error(configuredName, self.result.status_code, self.result.text)
            return

        self.needUpdate = True
        self.uniqueUrlsProvisioned, self.remainingUrlsQuota = self.update_urls_total_number()
        self.update_category_report(configuredName, added=len(urls))

    def update_category_urls(self, category_id: str, urls: List[str], force_update=False) -> Union[None, int]:
        """Updates category urls set by calculating differences between provided urls and those
        stored on server. Method utilise both add_urls and delete_urls if necessary. After updating url set
        method updates internal report. If URL quota exceeded"""
        category = self.get_category(category_id)
        configuredName = self.get_configured_name(category_id)

        urls_to_delete = [url for url in category['urls'] if url not in urls]
        urls_to_add = [url for url in urls if url not in category['urls']]

        self.delete_urls(category_id, urls_to_delete)

        dropped = 0
        if not force_update:
            limit = self.remainingUrlsQuota - self.URL_QUOTA_MARGIN
            if limit < len(urls_to_add):
                dropped = len(urls_to_add) - limit
        else:
            limit = len(urls_to_add) - 1

        self.add_urls(category_id, urls_to_add[:limit])
        total = self.get_category_total_urls(category_id)
        self.update_category_report(configuredName, total=total)
        self.needUpdate = True
        return dropped if dropped != 0 else None

    def lookup_urls(self, urls: List[str], show_progress_bar=False) -> Union[Tuple[List[dict], int], Tuple[None, int]]:
        """Lookup up to 100 urls and categorize them. If provided urls list is longer than 100
        it will be separated into proper chunks."""

        limit = MAX_URLS_PER_LOOKUP
        lookup_results = []
        urls_skipped = 0
        while True:
            chunk = urls[limit - MAX_URLS_PER_LOOKUP:limit]
            if show_progress_bar:
                progress = limit / len(urls) * 100
                print_progress_bar(progress)
            while True:
                if len(chunk) == 0:
                    return lookup_results, urls_skipped
                time.sleep(1)
                self.result = self.session.post(url=f'{self.CLOUD_NAME}{self.BASE_PATH}/urlLookup',
                                                headers=self.headers,
                                                data=json.dumps(chunk))
                if self.result.status_code == 429:
                    self.wait_for_limit_refresh()
                elif self.result.status_code == 400 and self.result.json()['code'] == 'INVALID_INPUT_ARGUMENT':
                    invalid_url = self.result.json()['message'].split('[')[1].split(']')[0]
                    chunk.remove(invalid_url)
                    urls_skipped += 1
                else:
                    if self.result.status_code != 200:
                        self.add_error('Lookup error', self.result.status_code, self.result.text)
                    else:
                        lookup_results += self.result.json()
                    break
            if limit >= len(urls):
                return lookup_results, urls_skipped
            limit += MAX_URLS_PER_LOOKUP

    def get_firewall_filtering_rules(self):
        with L_GET_RATE_LIMITER:
            self.result = self.session.get(url=f"{self.CLOUD_NAME}{self.BASE_PATH}/firewallFilteringRules",
                                           headers=self.headers).json()
        return self.result.json()

    def activate(self):
        """Save changes made to ZScaler"""
        with L_POST_RATE_LIMITER:
            self.result = self.session.post(url=f"{self.CLOUD_NAME}{self.BASE_PATH}/status/activate",
                                            headers=self.headers)

    def delete(self):
        """Delete ZScaler API session"""
        self.session.delete(url=f'{self.CLOUD_NAME}{self.BASE_PATH}/authenticatedSession', headers=self.headers)

    def get_configured_name(self, category_id: str) -> Union[str, None]:
        """Returns string which represents category configuredName corresponding with category ID. Returns None
        if category with provided ID does not exist"""
        for category in self.categoriesLite:
            if category_id == category['id']:
                return category['configuredName']
        return None

    def get_id(self, configured_name: str) -> Union[str, None]:
        """Returns string which represents category ID corresponding with category configuredName. Returns None
        if category with provided name does not exist"""
        for category in self.categoriesLite:
            if 'configuredName' in category and category['configuredName'] == configured_name:
                return category['id']
        return

    def get_category(self, category_id: str) -> dict:
        """
        Get category by its ID. Returns dictionary.
        :param category_id:
        :return:
        """
        if self.needUpdate:
            self.categoriesFull = self.get_categories()
        for category in self.categoriesFull:
            if category['id'] == category_id:
                return category

    def get_category_total_urls(self, category_id: str) -> int:
        """
        Get total number of URLs within category
        :param category_id:
        :return:
        """
        return len(self.get_category(category_id)['urls'])

    def wait_for_limit_refresh(self) -> None:
        wait_time = self.result.json()['Retry-After']
        wait_time = int(wait_time.split(' ')[0])
        t = datetime.datetime.now()
        print(f'\rWaiting {wait_time} seconds until ', end='')
        print('{:%H:%M:%S}'.format(t + datetime.timedelta(seconds=wait_time)), end='')
        print(' due to rate limiting')
        if wait_time >= 1800:
            time.sleep(1740)
            self.session.get(url=f'{self.CLOUD_NAME}{self.BASE_PATH}/status', headers=self.headers)
            wait_time -= 1740
        time.sleep(wait_time)

    def update_category_report(self, configured_name: str, excluded: int = 0, skipped: int = 0, added: int = 0,
                               deleted: int = 0, total: int = 0):
        """
        Update category report record. Every parameter will be added to corresponding report field except total
        which represents number of all URLs within category. Providing total parameter will override current total value
        :param configured_name:
        :param excluded:
        :param skipped:
        :param added:
        :param deleted:
        :param total:
        :return:
        """
        for categoryReport in self.sessionReports:
            if configured_name == categoryReport.name:
                categoryReport.urls_excluded += excluded
                categoryReport.urls_skipped += skipped
                categoryReport.urls_added += added
                categoryReport.urls_deleted += deleted
                categoryReport.urls_total = total
                return

        category_report = CategoryReport(configured_name, excluded, skipped, added, deleted, total)
        self.sessionReports.append(category_report)

    def add_error(self, error_type: str, code: int, message: str) -> None:
        """
        Add error with given type, code and message
        :param error_type:
        :param code:
        :param message:
        :return:
        """
        self.sessionErrors.append(SessionErrors(error_type, [code], [message]))


def obfuscateApiKey(api_key: str) -> Tuple[int, str]:
    """
    ZScaler obfuscate key function from API documentation
    https://help.zscaler.com/zia/getting-started-zia-api#pythonobfuscate
    :param api_key:
    :return:
    """
    seed = api_key
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(str(n)), 1):
        key += seed[int(str(n)[i])]
    for j in range(0, len(str(r)), 1):
        key += seed[int(str(r)[j]) + 2]
    return now, key


def create_session(cloud_name: str, base_path: str, username: str, password: str, api_key: str) -> Tuple[
    requests.Session, dict, requests.Response]:
    """Create new session with ZScaler API.
    Returns session, header and connection result"""
    # Establish connection
    session = requests.session()
    session.get(cloud_name)
    now, key = obfuscateApiKey(api_key=api_key)

    session_credentials = json.dumps({
        "apiKey": key,
        "username": username,
        "password": password,
        "timestamp": now
    })
    headers = {
        "content-type": "application/json"
    }
    with L_POST_RATE_LIMITER:
        result = requests.post(url=f'{cloud_name}{base_path}/authenticatedSession', data=session_credentials,
                               headers=headers)

    # Get JSESSIONID and add it to the header
    headers['cookie'] = result.headers['Set-Cookie'].split(';')[0]

    return session, headers, result


def print_progress_bar(progress: float):
    bar_length = 20
    if progress < 100:
        bar = '|' + '=' * int(bar_length * progress // 100) + ' ' * int(
            bar_length - bar_length * progress // 100) + '|'
        print("\r\t{} {:.1f}%".format(bar, progress), end='')
    else:
        bar = '|' + '=' * bar_length + '|'
        print('\r\t{} Done'.format(bar))
