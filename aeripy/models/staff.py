from dataclasses import dataclass
from typing import List, Any
from datetime import datetime


@dataclass
class SchoolAccessPermission:
    school_code: int
    read_only_access: bool
    communication_group: bool


@dataclass
class Staff:
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
    position_status_code: int
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
    birth_date: None
    full_time_percentage: int
    hire_date: datetime
    leave_date: None
    inactive_status_code: str
    state_educator_id: str
    user_name: str
    email_address: str
    primary_aeries_school: int
    network_login_id: str
    alternate_email_address: str
    human_resources_system_id: str
    cell_phone: str
    notification_preference_code: int
    title: str


@dataclass
class Assignment:
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

@dataclass
class Teacher:
    class_calendar_sequence_number: int
    class_calendar: str
    user_code1: str
    user_code2: str
    user_code3: str
    user_code4: str
    user_code5: str
    user_code6: str
    user_code7: str
    user_code8: str
    low_grade: int
    high_grade: int
    school_code: int
    teacher_number: int
    display_name: str
    first_name: str
    last_name: str
    room: int
    email_address: str
    staff_id1: int
    staff_id2: int
    staff_id3: int
    state_course_code: str
    inactive_status_code: str
    highly_qualified_status_code1: str
    highly_qualified_status_code2: str
    highly_qualified_status_code3: str
    next_year_inactive_status_code: str
