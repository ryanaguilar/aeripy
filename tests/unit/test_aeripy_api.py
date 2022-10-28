from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import Aeripy
from aeripy.models import SystemInfo, Result, StaffElement
from aeripy.exceptions import AeripyException
import pytest
from pydantic import ValidationError


class TestAeripyApi(TestCase):
    def setUp(self) -> None:
        self.aeripyapi = Aeripy(hostname='dummy',
                                api_key='dummy')
        self.aeripyapi._rest_adapter = MagicMock()

    def test_get_one_staff_id_only(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                               headers={},
                                                               data=[{"ID": 1}]
                                                               )
        staff_list = self.aeripyapi.get_staff()
        for staff in staff_list:
            self.assertIsInstance(staff, StaffElement)

    def test_get_one_staff_no_id_fail(self):
        with pytest.raises(ValidationError):
            self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                                   headers={},
                                                                   data=[{"NameFirst": 'Joe'}]

                                                                   )
            self.aeripyapi.get_staff()


