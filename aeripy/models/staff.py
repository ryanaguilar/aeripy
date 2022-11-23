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
