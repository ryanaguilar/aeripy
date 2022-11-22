from dataclasses import dataclass
from enum import Enum
from typing import List

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
