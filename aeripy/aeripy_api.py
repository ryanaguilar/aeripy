import logging
from typing import Iterator, Callable, Union
from aeripy.rest_adapter import RestAdapter
from aeripy.exceptions import AeripyException
from aeripy.models import *
from .endpoints import API_PATH
from .models import SystemInfo


class AeripyApi:
    def __init__(self, hostname: str = "demo.aeries.net/aeries/api", api_key: str = '', ver: str = 'v5',
                 ssl_verify: str = '', logger: logging.Logger = None, page_size: int = 5):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._page_size = page_size

    def get_system_info(self) -> SystemInfo:
        result = self._rest_adapter.get(endpoint=API_PATH["system_info"])
        sys_info: SystemInfo = SystemInfo(**result.data)
        return sys_info
