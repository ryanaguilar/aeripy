from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import Aeripy
from aeripy.models import School, SystemInfo, Result, Term, BellScheduleElement, StaffElement
from aeripy.exceptions import AeripyException


class TestAeripyApi(TestCase):

    def test_init
    def setUp(self) -> None:
        self.aeripyapi = Aeripy(hostname='dummy',
                                        api_key='dummy')
        self.aeripyapi._rest_adapter = MagicMock()