import logging
from typing import Iterator, Callable, Union, Optional, List
from aeripy.rest_adapter import RestAdapter
from aeripy.exceptions import AeripyException
from aeripy.models import *
from .endpoints import API_PATH
from .models import SystemInfo, School
from .util.snake import snake_case_keys

class AeripyApi:
    def __init__(self, hostname: str = "demo.aeries.net/aeries/api", api_key: str = '477abe9e7d27439681d62f4e0de1f5e1',
                 ver: str = 'v5',
                 ssl_verify: str = '', logger: logging.Logger = None, page_size: int = 5):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._page_size = page_size

    def get_system_info(self) -> SystemInfo:
        result = self._rest_adapter.get(endpoint=API_PATH["system_info"])
        sys_info = SystemInfo(**snake_case_keys(result.data))
        return sys_info

    def get_schools(self) -> List[School]:
        result = self._rest_adapter.get(endpoint=API_PATH['schools'])
        schools_list = [School(**snake_case_keys(datum)) for datum in result.data]
        return schools_list

    def get_school(self, school_code: int) -> School:
        result = self._rest_adapter.get(endpoint=API_PATH['school'].format(school_code=school_code))
        school = School(**snake_case_keys(result.data))
        return school

    def get_terms(self, school_code: int) -> List[Term]:
        result = self._rest_adapter.get(endpoint=API_PATH['terms'].format(school_code=school_code))
        terms_list = [Term(**snake_case_keys(datum)) for datum in result.data]
        return terms_list

    def get_bell_schedules(self, school_code: str, date: int=None) -> List[BellScheduleElement]:
        if date is not None:
            endpoint = API_PATH['bell_schedule_date'].format(school_code=school_code, date=date)
        else:
            endpoint = API_PATH['bell_schedule'].format(school_code=school_code)
        result = self._rest_adapter.get(endpoint=endpoint)
        bell_schedules = [BellScheduleElement(**snake_case_keys(datum)) for datum in result.data]
        return bell_schedules

    def get_bell_schedule(self, school_code: str, date: int) -> BellScheduleElement:
        result = self.get_bell_schedules(school_code, date)
        bell_schedule = BellScheduleElement(**snake_case_keys(result.data))
        return bell_schedule


