"""Provide the Aeripy class"""
import logging
from .rest_adapter import RestAdapter
from .models import *
from .endpoints import API_PATH
from .models import SystemInfo, School
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
    def __init__(self, hostname: str = "demo.aeries.net/aeries/api",
                 api_key: str = '477abe9e7d27439681d62f4e0de1f5e1',
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
        return sys_info

    def get_schools(self) -> List[School]:
        """
        Gets all the schools in the Aeries system.  To get info about one school, use get_school().
        :return: List[School], a list of all schools in Aeries
        """
        result = self._rest_adapter.get(endpoint=API_PATH['schools'])
        schools_list = [School(**snake_case_keys(datum)) for datum in result.data]
        return schools_list

    def get_school(self, school_code: int) -> School:
        """
        Gets info about a specific school.  If the schools does not exist an HTTP 404 error is returned

        :param school_code: Int, required
        :return: School
        """
        result = self._rest_adapter.get(endpoint=API_PATH['school'].format(school_code=school_code))
        school = School(**snake_case_keys(result.data))
        return school

    def get_terms(self, school_code: int) -> List[Term]:
        """
        Gets a list of terms for the school

        :param school_code: Int, required
        :return: List[Term]
        """
        result = self._rest_adapter.get(endpoint=API_PATH['terms'].format(school_code=school_code))
        terms_list = [Term(**snake_case_keys(datum)) for datum in result.data]
        return terms_list

    def get_bell_schedules(self, school_code: int, date: str = None) -> List[BellScheduleElement]:
        """
        Gets bell schedules for all schools. A date can be supplied to get the schedule for a specific date

        :param school_code: Int, required
        :param date: Str, optional, in the format mm-dd-yyyy
        :return: List[BellScheduleElement]
        """
        if date is not None:
            endpoint = API_PATH['bell_schedule_date'].format(school_code=school_code, date=date)
        else:
            endpoint = API_PATH['bell_schedule'].format(school_code=school_code)
        result = self._rest_adapter.get(endpoint=endpoint)
        bell_schedules = [BellScheduleElement(**snake_case_keys(datum)) for datum in result.data]
        return bell_schedules

    def get_bell_schedule(self, school_code: int, date: str) -> BellScheduleElement:
        """
        Gets bell schedule for individual school.  If the date is not a school day
        :param school_code: Int, required.
        :param date: Str, required, in the format "mm-dd-yyyy".
        :return: BellScheduleElement
        """
        result = self.get_bell_schedules(school_code, date)
        bell_schedule_list = BellScheduleElement(**snake_case_keys(result.data[0]))
        return bell_schedule_list

    def get_calendar(self, school_code: int) -> List[CalendarElement]:
        result = self._rest_adapter.get(endpoint=API_PATH["calendar"].format(school_code=school_code))
        calendar = [CalendarElement(**snake_case_keys(datum)) for datum in result.data]
        return calendar

    def get_absence_codes(self, school_code: int, absence_code: int = None) -> List[AbsenceCodeElement]:
        if absence_code is not None:
            endpoint = API_PATH['absence_code'].format(school_code=school_code, absence_code=absence_code)
        else:
            endpoint = API_PATH['absence_codes'].format(school_code=school_code)
        result = self._rest_adapter.get(endpoint=endpoint)
        absence_codes_list = [AbsenceCodeElement(**snake_case_keys(datum)) for datum in result.data]
        return absence_codes_list

    def get_absence_code(self, school_code: int, absence_code: int) -> AbsenceCodeElement:
        result = self._rest_adapter.get(endpoint=API_PATH['absence_code'].format(school_code=school_code,
                                                                                 absence_code=absence_code))
        absence_code = AbsenceCodeElement(*snake_case_keys(result.data))
        return absence_code

    def get_staff(self, staff_id: int = None) -> List[StaffElement]:
        """Return objects from a GET request to the ``staff`` endpoint.
        :param staff_id: Int, ID of staff to get. None to request all staff (default: ``None``).
        :return: All staff will be returned if no staff_id is supplied
        """
        if staff_id is not None:
            endpoint = API_PATH['staff_id'].format(staff_id=staff_id)
            result = self._rest_adapter.get(endpoint=endpoint)
            staff = StaffElement(**snake_case_keys(result.data))
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
