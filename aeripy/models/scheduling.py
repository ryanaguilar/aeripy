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
