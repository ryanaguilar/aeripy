from dataclasses import dataclass
from typing import List, Dict, Any, Union, Optional
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from enum import Enum


@dataclass
class Result:
    """
    Result returned from low-level RestAdapter
    :param status_code: Standard HTTP Status code
    :param message: Human readable result
    :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
    """
    status_code: int
    headers: dict
    data: Optional[List[Dict]]
    message: str = ''


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


class HolidayCode(Enum):
    EMPTY = ""
    HOLIDAY_CODE = "#"
    PURPLE = "@"


@dataclass
class CalendarElement:
    track_holidays: List[Any]
    school_code: int
    calendar_day_number: int
    calendar_date: datetime
    holiday_code: HolidayCode
    attendance_month: int
    total_apportionment: int
    total_enrollment: int
    period_block_pattern: str
    ab_day: str
    attendance_month_locked: bool


class ColorCode(Enum):
    BE212_F = "be212f"
    E2_AA26 = "e2aa26"
    EMPTY = ""
    F1_D89_C = "f1d89c"


class IndependentStudyCode(Enum):
    C = "C"
    EMPTY = ""
    I = "I"


@dataclass
class AbsenceCodeElement:
    is_temporarily_not_enrolled: bool
    independent_study_code: IndependentStudyCode
    color_code: ColorCode
    school_code: int
    absence_code: str
    title: str
    abbreviation: str
    type_code: int
    type_description: str
    counts_for_ada: bool
    include_on_letters: bool
    include_in_parent_notifications: bool
    include_on_reports: bool
    count_on_report_card: bool
    is_suspension: bool
    is_partial_day_truant: bool


@dataclass
class SchoolAccessPermission:
    school_code: int
    read_only_access: bool
    communication_group: bool


@dataclass
class StaffElement:
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


@dataclass
class AssignmentElement:
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
class Student:
    student_id: int
    old_student_id: int
    correspondence_language_code: str
    counselor_number: int
    student_personal_email_address: str
    school_code: int
    student_number: int
    state_student_id: int
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

@dataclass
class Contact:
    student_id: int
    administrative_lock_code: str
    enrolled_the_student_indicator: str
    birthdate: None
    occupation: str
    tuberculosis_test_status_code: str
    tuberculosis_test_expiration_date: None
    fingerprint_status_code: str
    fingerprint_date: None
    user_code1: str
    user_code2: str
    user_code3: str
    user_code4: str
    user_code5: str
    user_code6: str
    user_code7: str
    user_code8: str
    misc_code: str
    mail_tag_code: str
    address_type_code: int
    additional_communication_type_code1: str
    additional_communication_type_code2: str
    additional_communication_type_code3: str
    additional_communication_type_code4: str
    additional_communication_detail1: str
    additional_communication_detail2: str
    additional_communication_detail3: str
    additional_communication_detail4: str
    address_verification_date: None
    record_added_date: datetime
    military_user_field_code1: str
    military_user_field_code2: str
    military_user_field_code3: str
    military_user_field_code4: str
    military_user_field_code5: str
    primary_contact1_field: str
    primary_contact2_field: str
    primary_contact1_description: str
    primary_contact2_description: str
    educational_rights_holder: str
    attendance_notification: str
    primary_contact: str
    school_code: int
    sequence_number: int
    mailing_name: str
    name_prefix: str
    first_name: str
    last_name: str
    middle_name: str
    name_suffix: str
    address: str
    address_city: str
    address_state: str
    address_zip_code: int
    address_zip_ext: str
    relationship_to_student_code: int
    lives_with_student_indicator: str
    red_flag: bool
    home_phone: str
    work_phone: str
    work_phone_ext: str
    cell_phone: str
    pager: str
    email_address: str
    access_to_portal: str
    contact_order: int
    correspondance_language_code: str
    employer_name: str
    employer_location: str
    military_branch_code: str
    military_rank_code: str
    military_supervisor_name: str
    military_supervisor_phone: str
    military_status_code: str
    notification_preference_code: int
    comments: str

@dataclass
class Activity:
    student_id: int
    school_code: int
    sequence_number: int
    date_entered: datetime
    type_code: str
    activity_or_award_code: str
    name: str
    start_date: None
    end_date: None
    hours: int
    reason_code: str
    season_code: str
    status_code: str
    transportation_date: None
    transportation_status_code: str
    career_pathway_code: str
    comment: str

@dataclass
class Authorizations:
    student_id: int
    school_code: int
    sequence_number: int
    date_entered: datetime
    type_code: int
    misc_code: str
    status: int
    status_date: datetime
    effective_end_date: datetime
    comment: str
    test_administration: str
    source: str
