from typing import List, Dict, Any, Union, Optional
from datetime import datetime
from pydantic import BaseModel, Json


def to_camel(string: str) -> str:
    string_split = string.split('_')
    return string_split[0].capitalize()+''.join(word.capitalize() for word in string_split[1:])

class Result(BaseModel):
    """
    Result returned from low-level RestAdapter
    :param status_code: Standard HTTP Status code
    :param message: Human readable result
    :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
    """
    status_code: int
    headers: dict
    data: Json
    message: str = ''


class SystemInfo(BaseModel):
    aeries_version: str
    database_year: str
    available_database_years: List[str]
    local_time_zone_name: str
    current_date_time: datetime

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class SchoolAccessPermission(BaseModel):
    school_code: int
    read_only_access: bool
    communication_group: bool


class StaffElement(BaseModel):
    school_access_permissions: List[SchoolAccessPermission]
    extended_properties: List[Any]
    early_childhood_certification_code: str
    gender: str
    education_level_code: int
    ethnicity_code: str
    race_code1: str
    race_code2: str
    race_code3: str
    race_code4: str
    race_code5: str
    position_status_code: str
    total_years_of_edu_service: int
    total_years_in_this_district: int
    previous_last_name: str
    previous_first_name: str
    previous_middle_name: str
    name_suffix: str
    address: str
    address_city: str
    address_state: str
    address_zip_code: int
    address_zip_ext: int
    home_phone: str
    emergency_contact_name: str
    emergency_contact_phone: str
    id: int
    first_name: str
    last_name: str
    middle_name: str
    birth_year: int
    full_time_percentage: int
    inactive_status_code: str
    state_educator_id: str
    user_name: str
    email_address: str
    primary_aeries_school: int
    network_login_id: str
    alternate_email_address: str
    human_resources_system_id: str
    cell_phone: str
    notification_preference_code: str
    title: str
    birth_date: Optional[datetime] = None
    hire_date: Optional[datetime] = None
    leave_date: Optional[datetime] = None


class AssignmentElement(BaseModel):
    monthly_minutes: int
    population_served_code: str
    service_id_code: str
    assignment_type: str
    id: int
    sequence_number: int
    job_classification_code: int
    full_time_percentage: int
    non_classroom_based_job_assignment_code1: str
    non_classroom_based_job_assignment_code2: str
    non_classroom_based_job_assignment_code3: str
    non_classroom_based_job_assignment_code4: str
    non_classroom_based_job_assignment_code5: str
    non_classroom_based_job_assignment_code6: str
    non_classroom_based_job_assignment_code7: str
    school_code: int
    start_date: datetime
    end_date: None
