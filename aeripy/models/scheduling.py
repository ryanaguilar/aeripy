from dataclasses import dataclass


@dataclass
class ClassCalendar:
    sequence_number: int
    school_code: int
    academic_year: str
    short_title: str
    description: str
