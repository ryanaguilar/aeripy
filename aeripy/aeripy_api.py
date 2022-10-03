import logging
from typing import Iterator, Callable, Union, Optional, List
from aeripy.rest_adapter import RestAdapter
from aeripy.exceptions import AeripyException
from aeripy.models import *
from .endpoints import API_PATH
from .models import SystemInfo, School


class AeripyApi:
    def __init__(self, hostname: str = "demo.aeries.net/aeries/api", api_key: str = '477abe9e7d27439681d62f4e0de1f5e1',
                 ver: str = 'v5',
                 ssl_verify: str = '', logger: logging.Logger = None, page_size: int = 5):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._page_size = page_size

    def get_system_info(self) -> SystemInfo:
        result = self._rest_adapter.get(endpoint=API_PATH["system_info"])
        sys_info: SystemInfo = SystemInfo(**result.data)
        return sys_info

    def get_schools(self) -> List[School]:
        result = self._rest_adapter.get(endpoint=f"{API_PATH['schools']}/")
        schools_list: List[School] = [School(**datum) for datum in result.data]
        return schools_list

