from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from aeripy import AeripyException


class Result:
    def __init__(self, status_code: int, headers: CaseInsensitiveDict, message: str = '', data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.headers = headers
        self.message = str(message)
        self.data = data if data else []

@dataclass
class SystemInfo:
    AeriesVersion: str
    DatabaseYear: str
    AvailableDatabaseYears: List[str]
    LocalTimeZoneName: str
    CurrentDateTime: datetime

@dataclass
class Term:
    FirstHalfEndDate: None
    SecondHalfStartDate: None
    TrackTerms: List[Any]
    TermCode: str
    TermDescription: str
    StartDate: datetime
    EndDate: datetime


@dataclass
class School:
    RegionCode: str
    StateCharterNumber: str
    CharterStatusCode: str
    FederalTaxID: str
    FederalInformationProcessingStandardsCode: str
    QualityRatingAndImprovementSystemParticipationCode: str
    AccreditationStatusCode: str
    SchoolWebsite: str
    OrganizationCategoryCode: str
    SchoolCategoryCode: str
    LocalEducationAgencyTypeCode: str
    TitleIPartACode: str
    NSLPStatusCode: str
    NCESSchoolID: str
    CollegeBoardSchoolCode: int
    CampusEnrollmentTypeCode: str
    PreKSchoolTypeCode: str
    EarlyCollegeHighSchoolIndicator: bool
    ScienceTechnologyEngineeringAndMathematicsIndicator: bool
    PathwaysInTechnologyIndicator: bool
    ShortName: str
    Terms: List[Term]
    SchoolCode: int
    Name: str
    InactiveStatusCode: str
    Address: str
    AddressCity: str
    AddressState: str
    AddressZipCode: int
    AddressZipExt: str
    DoNotReport: bool
    StateCountyID: int
    StateDistrictID: int
    StateSchoolID: str
    LowGradeLevel: int
    HighGradeLevel: int
    PrincipalName: str
    PrincipalEmailAddress: str
    AttendancePeriod: int
    Tracks: int
    ScheduleType: str
    SessionType: str
    AttendanceType: str
    AttendanceReporting: str
    ScheduleBasis: str
    PhoneNumber: str
