from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from aeripy import AeripyException


class Result:
    def __init__(self, status_code: int, headers: CaseInsensitiveDict, message: str = '', data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.headers = headers
        self.message = str(message)
        self.data = data if data else []


@dataclass
class School:
    aeries_version: str
    database_year: str
    available_database_years: List[str]
    local_time_zone_name: str
    current_date_time: datetime


@dataclass
class SystemInfo:
    aeries_version: str
    database_year: str
    available_database_years: List[str]
    local_time_zone_name: str
    current_date_time: datetime


@dataclass
class Term:
    first_half_end_date: None
    second_half_start_date: None
    track_terms: List[Any]
    term_code: str
    term_description: str
    start_date: datetime
    end_date: datetime


@dataclass
class School:
    region_code: str
    state_charter_number: str
    charter_status_code: str
    federal_tax_id: str
    federal_information_processing_standards_code: str
    quality_rating_and_improvement_system_participation_code: str
    accreditation_status_code: str
    school_website: str
    organization_category_code: str
    school_category_code: str
    local_education_agency_type_code: str
    title_i_part_a_code: str
    nslp_status_code: str
    nces_school_id: str
    college_board_school_code: int
    campus_enrollment_type_code: str
    pre_k_school_type_code: str
    early_college_high_school_indicator: bool
    science_technology_engineering_and_mathematics_indicator: bool
    pathways_in_technology_indicator: bool
    short_name: str
    using_section_staff_in_master_schedule: bool
    using_section_staff_in_scheduling: bool
    terms: List[Term]
    school_code: int
    name: str
    inactive_status_code: str
    address: str
    address_city: str
    address_state: str
    address_zip_code: int
    address_zip_ext: str
    do_not_report: bool
    state_county_id: int
    state_district_id: int
    state_school_id: int
    low_grade_level: int
    high_grade_level: int
    principal_name: str
    principal_email_address: str
    attendance_period: int
    tracks: int
    schedule_type: str
    session_type: str
    attendance_type: str
    attendance_reporting: str
    schedule_basis: str
    phone_number: str


@dataclass
class BellScheduleElement:
    school_code: int
    period: int
    start_time: datetime
    end_time: datetime
    calendar_date: None


