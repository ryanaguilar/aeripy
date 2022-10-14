import requests
import logging
from typing import List, Dict, Union
from json import JSONDecodeError
from aeripy.exceptions import AeripyException
from aeripy.models import Result


class RestAdapter:
    def __init__(self, hostname: str,
                 api_key: str, ver: str = 'v5',
                 ssl_verify: str = '',
                 logger: logging.Logger = None):
        """
        Constructor for RestAdapter
        :param hostname: URL of the Aeries instance. Required
        :param api_key: API key of the Aeries instance. Required
        :param ver: v5 is the default
        :param ssl_verify: True by default, but can also take a PEM path for testing
        :param logger: (optional) If your app has a logger, pass it here
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = f"https://{hostname}/{ver}"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        """
        Private method for get(), post, delete() methods
        :param http_method: GET, POST, DELETE
        :param endpoint: URL endpoint as a string
        :param ep_params: Dictionary of endpoint parameters (optional)
        :param data: Dictionary of data to pass to Aeripy (optional)
        :return: a Result object
        """
        full_url = self.url + endpoint
        headers = {"AERIES-CERT": self._api_key}
        log_line_pre = f"method{http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))

        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify,
                                        headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise AeripyException("Request failed") from e

        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, TypeError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise AeripyException("Bad JSON in response") from e

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200     # 200 to 299 is OK
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, headers=response.headers, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise AeripyException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)

    def put(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='PUT', endpoint=endpoint, ep_params=ep_params, data=data)

    def delete(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> Result:
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)
