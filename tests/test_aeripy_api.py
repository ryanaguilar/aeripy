from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import AeripyApi
from aeripy.models import School, SystemInfo, Result, Term


class TestAeripyApi(TestCase):
    def setUp(self) -> None:
        self.aeripyapi = AeripyApi()
        self.aeripyapi._rest_adapter = MagicMock()

    def test_get_system_info(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200, headers={},
                                                               data={
                                                                   "AeriesVersion": "9.21.2.25",
                                                                    "DatabaseYear": "2020-2021",
                                                                    "AvailableDatabaseYears": ["2020-2021", "2019-2020"],
                                                                    "LocalTimeZoneName": "(UTC-0:8:00) Pacific Time (US & Canada)",
                                                                    "CurrentDateTime": "2021-03-03T11:13:38.9539491-08:00"
                                                               })
        sysinfo = self.aeripyapi.get_system_info()
        self.assertIsInstance(sysinfo, SystemInfo )

    def test_get_schools(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data=[{
                                                                    "RegionCode": "",
                                                                    "StateCharterNumber": "",
                                                                    "CharterStatusCode": "",
                                                                    "FederalTaxID": "",
                                                                    "FederalInformationProcessingStandardsCode": "",
                                                                    "QualityRatingAndImprovementSystemParticipationCode": "",
                                                                    "AccreditationStatusCode": "",
                                                                    "SchoolWebsite": "",
                                                                    "OrganizationCategoryCode": "",
                                                                    "SchoolCategoryCode": "",
                                                                    "LocalEducationAgencyTypeCode": "",
                                                                    "TitleIPartACode": "",
                                                                    "NSLPStatusCode": "",
                                                                    "NCESSchoolID": "",
                                                                    "CollegeBoardSchoolCode": "123994",
                                                                    "CampusEnrollmentTypeCode": "",
                                                                    "PreKSchoolTypeCode": "",
                                                                    "EarlyCollegeHighSchoolIndicator": False,
                                                                    "ScienceTechnologyEngineeringAndMathematicsIndicator": False,
                                                                    "PathwaysInTechnologyIndicator": False,
                                                                    "ShortName": "",
                                                                    "UsingSectionStaffInMasterSchedule": False,
                                                                    "UsingSectionStaffInScheduling": False,
                                                                    "Terms": [
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "1",
                                                                            "TermDescription": "1st Quarter",
                                                                            "StartDate": "2022-07-04T00:00:00",
                                                                            "EndDate": "2022-10-14T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "2",
                                                                            "TermDescription": "2nd Quarter",
                                                                            "StartDate": "2022-10-17T00:00:00",
                                                                            "EndDate": "2022-12-21T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "3",
                                                                            "TermDescription": "3rd Quarter",
                                                                            "StartDate": "2023-01-02T00:00:00",
                                                                            "EndDate": "2023-03-24T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "4",
                                                                            "TermDescription": "4th Quarter",
                                                                            "StartDate": "2023-03-27T00:00:00",
                                                                            "EndDate": "2023-08-04T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "F",
                                                                            "TermDescription": "Fall",
                                                                            "StartDate": "2022-07-04T00:00:00",
                                                                            "EndDate": "2022-12-21T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "S",
                                                                            "TermDescription": "Spring",
                                                                            "StartDate": "2023-01-02T00:00:00",
                                                                            "EndDate": "2023-08-04T00:00:00"
                                                                        },
                                                                        {
                                                                            "FirstHalfEndDate": None,
                                                                            "SecondHalfStartDate": None,
                                                                            "TrackTerms": [],
                                                                            "TermCode": "Y",
                                                                            "TermDescription": "Year",
                                                                            "StartDate": "2022-07-04T00:00:00",
                                                                            "EndDate": "2023-08-04T00:00:00"
                                                                        }
                                                                    ],
                                                                    "SchoolCode": 994,
                                                                    "Name": "Screaming Eagle High School",
                                                                    "InactiveStatusCode": "",
                                                                    "Address": "6336 Eagle Crag Lane",
                                                                    "AddressCity": "Eagle Rock",
                                                                    "AddressState": "CA",
                                                                    "AddressZipCode": "95994",
                                                                    "AddressZipExt": "",
                                                                    "DoNotReport": False,
                                                                    "StateCountyID": "65",
                                                                    "StateDistrictID": "99999",
                                                                    "StateSchoolID": "9999994",
                                                                    "LowGradeLevel": 9,
                                                                    "HighGradeLevel": 12,
                                                                    "PrincipalName": "Mr John Smith",
                                                                    "PrincipalEmailAddress": "",
                                                                    "AttendancePeriod": 0,
                                                                    "Tracks": 0,
                                                                    "ScheduleType": "MasterSchedule",
                                                                    "SessionType": "Regular",
                                                                    "AttendanceType": "Period",
                                                                    "AttendanceReporting": "Negative",
                                                                    "ScheduleBasis": "Semester",
                                                                    "PhoneNumber": "9995559994"
                                                                }])
        schools = self.aeripyapi.get_schools()
        for school in schools:
            self.assertIsInstance(school, School)

    def test_get_school(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data={
                                                                   "RegionCode": "",
                                                                   "StateCharterNumber": "",
                                                                   "CharterStatusCode": "",
                                                                   "FederalTaxID": "",
                                                                   "FederalInformationProcessingStandardsCode": "",
                                                                   "QualityRatingAndImprovementSystemParticipationCode": "",
                                                                   "AccreditationStatusCode": "",
                                                                   "SchoolWebsite": "",
                                                                   "OrganizationCategoryCode": "",
                                                                   "SchoolCategoryCode": "",
                                                                   "LocalEducationAgencyTypeCode": "",
                                                                   "TitleIPartACode": "",
                                                                   "NSLPStatusCode": "",
                                                                   "NCESSchoolID": "",
                                                                   "CollegeBoardSchoolCode": "123994",
                                                                   "CampusEnrollmentTypeCode": "",
                                                                   "PreKSchoolTypeCode": "",
                                                                   "EarlyCollegeHighSchoolIndicator": False,
                                                                   "ScienceTechnologyEngineeringAndMathematicsIndicator": False,
                                                                   "PathwaysInTechnologyIndicator": False,
                                                                   "ShortName": "",
                                                                   "UsingSectionStaffInMasterSchedule": False,
                                                                   "UsingSectionStaffInScheduling": False,
                                                                   "Terms": [
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "1",
                                                                           "TermDescription": "1st Quarter",
                                                                           "StartDate": "2022-07-04T00:00:00",
                                                                           "EndDate": "2022-10-14T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "2",
                                                                           "TermDescription": "2nd Quarter",
                                                                           "StartDate": "2022-10-17T00:00:00",
                                                                           "EndDate": "2022-12-21T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "3",
                                                                           "TermDescription": "3rd Quarter",
                                                                           "StartDate": "2023-01-02T00:00:00",
                                                                           "EndDate": "2023-03-24T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "4",
                                                                           "TermDescription": "4th Quarter",
                                                                           "StartDate": "2023-03-27T00:00:00",
                                                                           "EndDate": "2023-08-04T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "F",
                                                                           "TermDescription": "Fall",
                                                                           "StartDate": "2022-07-04T00:00:00",
                                                                           "EndDate": "2022-12-21T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "S",
                                                                           "TermDescription": "Spring",
                                                                           "StartDate": "2023-01-02T00:00:00",
                                                                           "EndDate": "2023-08-04T00:00:00"
                                                                       },
                                                                       {
                                                                           "FirstHalfEndDate": None,
                                                                           "SecondHalfStartDate": None,
                                                                           "TrackTerms": [],
                                                                           "TermCode": "Y",
                                                                           "TermDescription": "Year",
                                                                           "StartDate": "2022-07-04T00:00:00",
                                                                           "EndDate": "2023-08-04T00:00:00"
                                                                       }
                                                                   ],
                                                                   "SchoolCode": 994,
                                                                   "Name": "Screaming Eagle High School",
                                                                   "InactiveStatusCode": "",
                                                                   "Address": "6336 Eagle Crag Lane",
                                                                   "AddressCity": "Eagle Rock",
                                                                   "AddressState": "CA",
                                                                   "AddressZipCode": "95994",
                                                                   "AddressZipExt": "",
                                                                   "DoNotReport": False,
                                                                   "StateCountyID": "65",
                                                                   "StateDistrictID": "99999",
                                                                   "StateSchoolID": "9999994",
                                                                   "LowGradeLevel": 9,
                                                                   "HighGradeLevel": 12,
                                                                   "PrincipalName": "Mr John Smith",
                                                                   "PrincipalEmailAddress": "",
                                                                   "AttendancePeriod": 0,
                                                                   "Tracks": 0,
                                                                   "ScheduleType": "MasterSchedule",
                                                                   "SessionType": "Regular",
                                                                   "AttendanceType": "Period",
                                                                   "AttendanceReporting": "Negative",
                                                                   "ScheduleBasis": "Semester",
                                                                   "PhoneNumber": "9995559994"
                                                               })
        school = self.aeripyapi.get_school(0)
        self.assertIsInstance(school, School)


    def test_get_terms(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data=[
                                                                   {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "1",
                                                                        "TermDescription": "1st Quarter",
                                                                        "StartDate": "2022-07-04T00:00:00",
                                                                        "EndDate": "2022-10-14T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "2",
                                                                        "TermDescription": "2nd Quarter",
                                                                        "StartDate": "2022-10-17T00:00:00",
                                                                        "EndDate": "2022-12-21T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "3",
                                                                        "TermDescription": "3rd Quarter",
                                                                        "StartDate": "2023-01-02T00:00:00",
                                                                        "EndDate": "2023-03-24T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "4",
                                                                        "TermDescription": "4th Quarter",
                                                                        "StartDate": "2023-03-27T00:00:00",
                                                                        "EndDate": "2023-08-04T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "F",
                                                                        "TermDescription": "Fall",
                                                                        "StartDate": "2022-07-04T00:00:00",
                                                                        "EndDate": "2022-12-21T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "S",
                                                                        "TermDescription": "Spring",
                                                                        "StartDate": "2023-01-02T00:00:00",
                                                                        "EndDate": "2023-08-04T00:00:00"
                                                                    },
                                                                    {
                                                                        "FirstHalfEndDate": None,
                                                                        "SecondHalfStartDate": None,
                                                                        "TrackTerms": [],
                                                                        "TermCode": "Y",
                                                                        "TermDescription": "Year",
                                                                        "StartDate": "2022-07-04T00:00:00",
                                                                        "EndDate": "2023-08-04T00:00:00"
                                                                    }
                                                                ])
        terms = self.aeripyapi.get_terms(994)
        for term in terms:
            self.assertIsInstance(term, Term)g