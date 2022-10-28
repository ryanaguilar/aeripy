"""Provide the Aeripy class"""
import logging
from .rest_adapter import RestAdapter
from .models import *
from .endpoints import API_PATH
from .models import SystemInfo
from .util import snake_case_keys, camel_case_keys


class Aeripy:
    """
    The Aeripy class provides access to the Aeries API.

    Instances of this class are the primary way to interact with the Aeries API.  To obtain and instance of this class:

    .. code-block:: python

        from aeripy import Aeripy

        aeries = Aeripy(
            hostname="demo.aeries.net/aeries/api",
            api_key="477abe9e7d27439681d62f4e0de1f5e1"
        )

    """
    def __init__(self, hostname: str,
                 api_key: str,
                 ver: str = 'v5',
                 ssl_verify: str = '',
                 logger: logging.Logger = None,
                 page_size: int = 5):
        """
        Initialize a :class:`Aeripy` instance.

        :param hostname: The base url of the Aeries SIS with the path /api on the end
        :param api_key: This api_key is found in Aeries->Security->API security. See Aeries documentation for details
        :param ver: default version is v5
        :param ssl_verify: The path to your SSL cert must be provided if your district uses SSL inspection
        :param logger: default logger
        :param page_size:

        """
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)
        self._page_size = page_size

    def get_system_info(self) -> SystemInfo:
        """
        Gets information about the target Aeries SIS.
        :return: SystemInfo
        """
        result = self._rest_adapter.get(endpoint=API_PATH["system_info"])
        sys_info = SystemInfo(**snake_case_keys(result.data))
        print(result.data)
        return sys_info


    def get_staff(self, staff_id: int = None) -> List[StaffElement]:
        """Return objects from a GET request to the ``staff`` endpoint.
        :param staff_id: Int, ID of staff to get. None to request all staff (default: ``None``).
        :return: All staff will be returned if no staff_id is supplied
        """
        if staff_id is not None:
            endpoint = API_PATH['staff_id'].format(staff_id=staff_id)
            result = self._rest_adapter.get(endpoint=endpoint)
            staff = StaffElement(**result.data)
        else:
            endpoint = API_PATH['staff']
            result = self._rest_adapter.get(endpoint=endpoint)
            staff = [StaffElement(**snake_case_keys(datum)) for datum in result.data]
        return staff

    def insert_staff(self, data: dict) -> StaffElement:
        """Inserts staff into the Aeries SIS using POST. After a successful request,
        this end point returns HTTP status code 201,
        and the response body contains the ``staff`` object that was just created.
        :param data: Dict, the data to create the staff with.
        :return:
        """
        result = self._rest_adapter.post(endpoint=API_PATH["staff"], data=camel_case_keys(data))
        staff = StaffElement(**snake_case_keys(result.data))
        return staff

    def update_staff(self, data: dict, staff_id: int = None) -> StaffElement:
        """
        Update staff using PUT.
        A 200 status will be returned if staff exists.
        A 201 status will be returned if staff was created.
        :param data: Dict, If property is omitted or null, it will be ignored.  An empty string is a valid value.
        Except in the case of LeaveDate, which will be nulled if it is omitted.
        :param staff_id: Int, If staff_id is supplied, but doesn't exist, and if auto-generate IDs IS NOT enabled,
        a new record will be created. If auto-generate IDs IS enabled, an error will be generated
        :return:
        """
        if staff_id is None:
            staff_id = data.get("staff_id")
        result = self._rest_adapter.put(endpoint=API_PATH["staff_id"].format(staff_id=staff_id), data=camel_case_keys(data))
        staff = StaffElement(**snake_case_keys(result.data))
        return staff
