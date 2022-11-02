from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import Aeripy
from aeripy.models import SystemInfo, Result, StaffElement
from aeripy.exceptions import AeripyException
import pytest
from aeripy.exceptions import StateEducatorIdError
from pydantic import ValidationError


class TestAeripyApi(TestCase):
    def setUp(self) -> None:
        self.aeripyapi = Aeripy(hostname='dummy',
                                api_key='dummy')
        self.aeripyapi._rest_adapter = MagicMock()

    def test_get_one_staff_id_only(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                               headers={},
                                                               data={"Id": 1}
                                                               )
        staff = self.aeripyapi.get_staff(1)
        assert isinstance(staff, StaffElement)

    def test_get_one_staff_return_list_fail(self):
        pass

    def test_get_all_staff(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                               headers={},
                                                               data=[
                                                                        {"ID": 1},
                                                                        {"ID": 2}
                                                                    ]
                                                               )
        staff_list = self.aeripyapi.get_staff()
        for staff in staff_list:
            assert isinstance(staff, StaffElement)

    def test_get_all_staff_return_dict(self):
        pass

    def test_get_one_staff_equals_requested_staff(self):
        pass

    def test_get_one_staff_no_id_fail(self):
        with pytest.raises(ValidationError):
            self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                                   headers={},
                                                                   data=[{"NameFirst": 'Joe'}]
                                                     )
            self.aeripyapi.get_staff()

    def test_get_staff_seid_too_long(self):
        with pytest.raises(StateEducatorIdError):
            self.aeripyapi._rest_adapter.get.return_value = Result(status_code=200,
                                                                   headers={},
                                                                   data={
                                                                        "Id": 1,
                                                                        "StateEducatorId": "12345678901",
                                                                        }
                                                                   )
            self.aeripyapi.get_staff(1)

    def test_update_staff_success(self):
        pass

    def test_update_staff_no_data(self):
        pass

    def test_update_staff_no_id(self):
        pass

    def test_insert_staff_no_data(self):
        pass

    def test_insert_staff_no_id(self):
        pass

