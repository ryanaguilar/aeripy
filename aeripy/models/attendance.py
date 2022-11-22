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
