import requests
from requests.exceptions import RequestException
from unittest import TestCase, mock
from aeripy.exceptions import AeripyException
from aeripy.models import Result
from aeripy.rest_adapter import RestAdapter


class TestRestAdapter(TestCase):
    def setUp(self) -> None:
        self.rest_adapter = RestAdapter(hostname='demo.aeries.net/aeries/api',
                                        api_key='477abe9e7d27439681d62f4e0de1f5e1')
        self.response = requests.Response()

    def tearDown(self) -> None:
        pass

    def test__do_good_request_returns_result(self):
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.request", return_value=self.response):
            result = self.rest_adapter._do('GET', '')
            self.assertIsInstance(result, Result)

    def test__do_bad_request_raises_aeripy_exception(self):
        with mock.patch("requests.request", side_effect=RequestException):
            with self.assertRaises(AeripyException):
                self.rest_adapter._do('GET', '')

    def test__do_bad_json_raises_aeripy_exception(self):
        bad_json = '{"some bad json": '
        self.response._content = bad_json
        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AeripyException):
                self.rest_adapter._do('GET', '')

    def test__do_300_or_higher_raises_aeripy_exception(self):
        self.response.status_code = 300
        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AeripyException):
                self.rest_adapter._do('GET', '')

    def test__do_199_or_lower_raises_aeripy_exception(self):
        self.response.status_code = 199
        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AeripyException):
                self.rest_adapter._do('GET', '')

    def test_get_method_passes_in_get(self):
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.request", return_value=self.response) as request:
            self.rest_adapter.get(endpoint='')
            self.assertTrue(request.method, 'GET')
