from dataclasses import dataclass
from datetime import datetime

@dataclass
class ClassCalendar:
    sequence_number: int
    school_code: int
    academic_year: str
    short_title: str
    description: str


@dataclass
class FlexPeriod:
    sequence_number: int
    school_code: int
    academic_year: str
    short_title: str
    description: str
    start_time: datetime
    end_time: datetime
    type_code: str


@dataclass
class ClassSchedule:
    student_id: int
    school_code: int
    sequence_number: int
    section_number: int
    course_id: str
    date_started: datetime
    date_ended: datetime


@dataclass
class Course:
    vocational_education_subject_area_code: str
    vocational_education_course_level_code: str
    course_level_code: str
    course_type_code: str
    next_course: str
    term_sequence: int
    year_sequence: int
    traditional_gender: str
    nclb_core_code: str
    nclb_core_area1_code: str
    nclb_core_area2_code: str
    content_group_code: str
    nces_code: str
    cip_code: str
    board_adoption_date: None
    last_revision_date: None
    revision_type_code: str
    inactive_date: None
    academic_weight: int
    meets_algebra_i_requirement: bool
    algebra_i_credit_required: int
    service_id_code: str
    population_served_code: str
    class_type_code: str
    course_sequence_code: str
    non_campus_based_instruction_code: str
    on_ramps_dual_enrollment_indicator: str
    include_for_extracurricular_activity_eligibility_indicator: str
    hours_for_completion: int
    cost_of_course: int
    content_subcategory_code: str
    standards_grade_range_code: str
    content_standards_alignment_code: str
    charter_non_core_indicator: str
    advanced_course_state_code: str
    college_state_course_code: str
    middle_school_core_indicator: str
    correspondence_language_code1: str
    title_for_language1: str
    correspondence_language_code2: str
    title_for_language2: str
    correspondence_language_code3: str
    title_for_language3: str
    correspondence_language_code4: str
    title_for_language4: str
    correspondence_language_code5: str
    title_for_language5: str
    correspondence_language_code6: str
    title_for_language6: str
    user_code1: str
    user_code2: str
    user_code3: str
    user_code4: str
    user_code5: str
    user_code6: str
    user_code7: str
    user_code8: str
    id: str
    title: str
    long_description: str
    notes: str
    content_description: str
    non_academic_or_honors_code: str
    subject_area1_code: str
    subject_area2_code: str
    subject_area3_code: str
    department_code: str
    state_course_code: int
    csf_course_list: str
    college_prep_indicator_code: str
    credit_default: int
    credit_max: int
    term_type_code: str
    low_grade: int
    high_grade: int
    csu_subject_area_code: str
    csu_rule_can_be_an_elective: str
    csu_rule_honors_code: str
    csu_rule_validation_level_code: str
    uc_subject_area_code: str
    uc_rule_can_be_an_elective: str
    uc_rule_honors_code: str
    uc_rule_validation_level_code: int
    teacher_aide_indicator: bool
    physical_education_indicator: bool
    inactive_status_code: str
    prerequisite_course: str
    alternate_course: str
    default_max_students: int
    next_year_inactive_status_code: str
