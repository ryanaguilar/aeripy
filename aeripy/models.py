from typing import List, Dict, Any, Union, Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator, PydanticValueError
from .util import camel_to_snake, snake_to_camel
from .exceptions import StateEducatorIdError, AeripyException


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
    data: Optional[Union[List[Dict], Dict]]
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
    school_access_permissions: Optional[SchoolAccessPermission]
    extended_properties: Optional[List[Any]]
    early_childhood_certification_code: Optional[str]
    gender: Optional[str]
    education_level_code: Optional[int]
    ethnicity_code: Optional[str]
    race_code1: Optional[str]
    race_code2: Optional[str]
    race_code3: Optional[str]
    race_code4: Optional[str]
    race_code5: Optional[str]
    position_status_code: Optional[str]
    total_years_of_edu_service: Optional[int]
    total_years_in_this_district: Optional[int]
    previous_last_name: Optional[str]
    previous_first_name: Optional[str]
    previous_middle_name: Optional[str]
    name_suffix: Optional[str]
    address: Optional[str]
    address_city: Optional[str]
    address_state: Optional[str]
    address_zip_code: Optional[int]
    address_zip_ext: Optional[int]
    home_phone: Optional[str]
    emergency_contact_name: Optional[str]
    emergency_contact_phone: Optional[str]
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    birth_year: Optional[int]
    full_time_percentage: Optional[int]
    inactive_status_code: Optional[str]
    state_educator_id: Optional[str]
    user_name: Optional[str]
    email_address: Optional[str]
    primary_aeries_school: Optional[int]
    network_login_id: Optional[str]
    alternate_email_address: Optional[str]
    human_resources_system_id: Optional[str]
    cell_phone: Optional[str]
    notification_preference_code: Optional[str]
    title: Optional[str]
    birth_date: Optional[datetime] = None
    hire_date: Optional[datetime] = None
    leave_date: Optional[datetime] = None

    @validator('state_educator_id')
    def seid_must_be_nine_digits(cls, v):
        if len(v) > 10:
            raise ValueError('SEID must be less than 10 digits')
        return v

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


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

class Student(BaseModel):
    student_id: int
    old_student_id: int
    correspondence_language_code: str
    counselor_number: int
    student_personal_email_address: str
    school_code: int
    student_number: int
    state_student_id: str
    last_name: str
    first_name: str
    middle_name: str
    last_name_alias: str
    first_name_alias: str
    middle_name_alias: str
    gender: str
    grade: int
    grade_level_short_description: int
    grade_level_long_description: str
    birthdate: datetime
    parent_guardian_name: str
    home_phone: str
    student_mobile_phone: str
    mailing_address: str
    mailing_address_city: str
    mailing_address_state: str
    mailing_address_zip_code: int
    mailing_address_zip_ext: str
    residence_address: str
    residence_address_city: str
    residence_address_state: str
    residence_address_zip_code: int
    residence_address_zip_ext: str
    address_verified: bool
    ethnicity_code: str
    race_code1: int
    race_code2: str
    race_code3: str
    race_code4: str
    race_code5: str
    user_code1: str
    user_code2: str
    user_code3: str
    user_code4: str
    user_code5: str
    user_code6: str
    user_code7: str
    user_code8: str
    user_code9: str
    user_code10: str
    user_code11: str
    user_code12: str
    user_code13: str
    school_enter_date: datetime
    school_leave_date: None
    district_enter_date: datetime
    track: str
    attendance_program_code_primary: str
    attendance_program_code_additional1: str
    attendance_program_code_additional2: str
    locker_number: str
    low_scheduling_period: int
    high_scheduling_period: int
    inactive_status_code: str
    family_key: int
    language_fluency_code: str
    home_language_code: str
    parent_ed_level_code: int
    parent_email_address: str
    student_email_address: str
    network_login_id: str
    early_warning_points: int
    home_room_teacher_number: int
    notification_preference_code: str
    next_school_code: int
    next_grade: int
    next_grade_level_short_description: int
    next_grade_level_long_description: str
    records_release_code: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
