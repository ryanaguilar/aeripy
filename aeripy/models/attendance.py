from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from datetime import datetime

@dataclass
class PeriodTotal:
    period: int
    total: int

@dataclass
class HistoryDetail:
    code: str
    school_year: SchoolYear
    description: str
    all_day_total: int
    period_totals: List[PeriodTotal]
    school_code: int


@dataclass
class AttendanceHistoryElement:
    student_id: int
    history_details: List[HistoryDetail]

@dataclass
class AttendanceCodes:
    is_temporarily_not_enrolled: bool
    independent_study_code: str
    absence_code: str
    school_year: str
    title: str
    abbreviation: str
    type: int
    counts_for_ada: bool
    include_on_letters: bool
    include_in_parent_notifications: bool
    include_on_reports: bool
    count_on_report_card: bool
    is_suspension: bool
    is_partial_day_truant: bool
    school_code: int

class AttendanceCode(Enum):
    D = "D"
    EMPTY = ""
    I = "I"
    K = "K"
    O = "O"
    Q = "Q"
    S = "S"
    T = "T"
    U = "U"


@dataclass
class Class:
    section_number: int
    period: int
    attendance_code: AttendanceCode


@dataclass
class AttendanceDay:
    calendar_date: datetime
    all_day_attendance_code: AttendanceCode
    classes: List[Class]


@dataclass
class AttendanceElement:
    student_id: int
    attendance_days: List[AttendanceDay]
    school_code: int

class AttendanceProgramCode(Enum):
    EMPTY = ""
    I = "I"


class AttendanceProgramCodeAdditional1(Enum):
    EMPTY = ""
    X = "X"


class AttendanceProgramCodeAdditional2(Enum):
    EMPTY = ""
    Z = "Z"


@dataclass
class EnrollmentElement:
    student_id: int
    inter_intra_district_state_code: str
    nonpublic_school_state_code: str
    next_school_code: int
    reporting_school_code: int
    school_code: int
    student_number: int
    academic_year: int
    track: str
    attendance_program_code: AttendanceProgramCode
    attendance_program_code_additional1: AttendanceProgramCodeAdditional1
    attendance_program_code_additional2: AttendanceProgramCodeAdditional2
    grade: int
    elementary_teacher_number: int
    elementary_teacher_name: str
    enter_date: datetime
    exit_reason_code: str
    inter_intra_district_transfer_code: str
    leave_date: Optional[datetime] = None
