from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import AeripyApi
from aeripy.models import School, SystemInfo, Result


class TestAeripyApi(TestCase):
    def setUp(self) -> None:
        self.aeripyapi = AeripyApi()
        self.aeripyapi._rest_adapter = MagicMock()

    def test_get_system_info(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200, headers={},
                                                               data={
                                                                   "AeriesVersion": "9.21.2.25",
                                                                    "DatabaseYear": "2020-2021",
                                                                    "AvailableDatabaseYears": ["2020-2021","2019-2020"],
                                                                    "LocalTimeZoneName": "(UTC-0:8:00) Pacific Time (US & Canada)",
                                                                    "CurrentDateTime": "2021-03-03T11:13:38.9539491-08:00"
                                                               })
        sysinfo = self.aeripyapi.get_system_info()
        self.assertIsInstance(sysinfo, SystemInfo )
