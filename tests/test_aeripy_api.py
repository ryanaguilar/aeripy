from unittest import TestCase
from unittest.mock import MagicMock
from aeripy.aeripy_api import AeripyApi
from aeripy.models import School, SystemInfo, Result, Term, BellScheduleElement, StaffElement


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
                                                                    }
                                                                ])
        terms = self.aeripyapi.get_terms(994)
        for term in terms:
            self.assertIsInstance(term, Term)

    def test_get_bell_schedules_school_day(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data=[
                                                                    {
                                                                        "SchoolCode": 994,
                                                                        "Period": "0",
                                                                        "StartTime": "1907-12-30T07:05:00",
                                                                        "EndTime": "1907-12-30T07:55:00",
                                                                        "CalendarDate": None
                                                                    },
                                                                    {
                                                                        "SchoolCode": 994,
                                                                        "Period": "1",
                                                                        "StartTime": "1907-12-30T08:00:00",
                                                                        "EndTime": "1907-12-30T08:50:00",
                                                                        "CalendarDate": None
                                                                    }
                                                                ])
        bell_schedules_list = self.aeripyapi.get_bell_schedules(994)
        for bell_schedule in bell_schedules_list:
            self.assertIsInstance(bell_schedule, BellScheduleElement)

    def test_get_bell_schedule_school_day(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data=[
                                                                    {
                                                                        "SchoolCode": 994,
                                                                        "Period": "0",
                                                                        "StartTime": "1907-12-30T07:05:00",
                                                                        "EndTime": "1907-12-30T07:55:00",
                                                                        "CalendarDate": None
                                                                    },
                                                                    {
                                                                        "SchoolCode": 994,
                                                                        "Period": "1",
                                                                        "StartTime": "1907-12-30T08:00:00",
                                                                        "EndTime": "1907-12-30T08:50:00",
                                                                        "CalendarDate": None
                                                                    }
                                                                ])
        bell_schedules_list = self.aeripyapi.get_bell_schedules(994, '10-04-2022')
        for bell_schedule in bell_schedules_list:
            self.assertIsInstance(bell_schedule, BellScheduleElement)

    def test_get_bell_schedules_non_school_day(self):
        pass

    def test_get_all_staff(self):
        self.aeripyapi._rest_adapter.get.return_value = Result(200,
                                                               headers={},
                                                               data=[
                                                                    {
                                                                        "SchoolAccessPermissions": [],
                                                                        "ExtendedProperties": [],
                                                                        "EarlyChildhoodCertificationCode": "",
                                                                        "Gender": "",
                                                                        "EducationLevelCode": " ",
                                                                        "EthnicityCode": "",
                                                                        "RaceCode1": "",
                                                                        "RaceCode2": "",
                                                                        "RaceCode3": "",
                                                                        "RaceCode4": "",
                                                                        "RaceCode5": "",
                                                                        "PositionStatusCode": " ",
                                                                        "TotalYearsOfEduService": 0,
                                                                        "TotalYearsInThisDistrict": 0,
                                                                        "PreviousLastName": "",
                                                                        "PreviousFirstName": "",
                                                                        "PreviousMiddleName": "",
                                                                        "NameSuffix": " ",
                                                                        "Address": "",
                                                                        "AddressCity": "",
                                                                        "AddressState": "CA",
                                                                        "AddressZipCode": " ",
                                                                        "AddressZipExt": " ",
                                                                        "HomePhone": "",
                                                                        "EmergencyContactName": "",
                                                                        "EmergencyContactPhone": "",
                                                                        "ID": 990900,
                                                                        "FirstName": "Grade 0",
                                                                        "LastName": "",
                                                                        "MiddleName": "",
                                                                        "BirthYear": 0,
                                                                        "BirthDate": None,
                                                                        "FullTimePercentage": 0,
                                                                        "HireDate": None,
                                                                        "LeaveDate": None,
                                                                        "InactiveStatusCode": " ",
                                                                        "StateEducatorID": "7777990900",
                                                                        "UserName": "",
                                                                        "EmailAddress": "",
                                                                        "PrimaryAeriesSchool": 990,
                                                                        "NetworkLoginID": "",
                                                                        "AlternateEmailAddress": "",
                                                                        "HumanResourcesSystemID": "",
                                                                        "CellPhone": "",
                                                                        "NotificationPreferenceCode": "1",
                                                                        "Title": ""
                                                                    },
                                                                    {
                                                                        "SchoolAccessPermissions": [],
                                                                        "ExtendedProperties": [],
                                                                        "EarlyChildhoodCertificationCode": "",
                                                                        "Gender": "",
                                                                        "EducationLevelCode": " ",
                                                                        "EthnicityCode": "",
                                                                        "RaceCode1": "",
                                                                        "RaceCode2": "",
                                                                        "RaceCode3": "",
                                                                        "RaceCode4": "",
                                                                        "RaceCode5": "",
                                                                        "PositionStatusCode": " ",
                                                                        "TotalYearsOfEduService": 0,
                                                                        "TotalYearsInThisDistrict": 0,
                                                                        "PreviousLastName": "",
                                                                        "PreviousFirstName": "",
                                                                        "PreviousMiddleName": "",
                                                                        "NameSuffix": " ",
                                                                        "Address": "",
                                                                        "AddressCity": "",
                                                                        "AddressState": "CA",
                                                                        "AddressZipCode": " ",
                                                                        "AddressZipExt": " ",
                                                                        "HomePhone": "",
                                                                        "EmergencyContactName": "",
                                                                        "EmergencyContactPhone": "",
                                                                        "ID": 990905,
                                                                        "FirstName": "Grade 5",
                                                                        "LastName": "",
                                                                        "MiddleName": "",
                                                                        "BirthYear": 0,
                                                                        "BirthDate": None,
                                                                        "FullTimePercentage": 0,
                                                                        "HireDate": None,
                                                                        "LeaveDate": None,
                                                                        "InactiveStatusCode": " ",
                                                                        "StateEducatorID": "7777990905",
                                                                        "UserName": "",
                                                                        "EmailAddress": "",
                                                                        "PrimaryAeriesSchool": 990,
                                                                        "NetworkLoginID": "",
                                                                        "AlternateEmailAddress": "",
                                                                        "HumanResourcesSystemID": "",
                                                                        "CellPhone": "",
                                                                        "NotificationPreferenceCode": "1",
                                                                        "Title": ""
                                                                    },
                                                                    {
                                                                        "SchoolAccessPermissions": [
                                                                            {
                                                                                "SchoolCode": 884,
                                                                                "ReadOnlyAccess": False,
                                                                                "CommunicationGroup": True
                                                                            }
                                                                        ],
                                                                        "ExtendedProperties": [],
                                                                        "EarlyChildhoodCertificationCode": "",
                                                                        "Gender": "M",
                                                                        "EducationLevelCode": "2",
                                                                        "EthnicityCode": "N",
                                                                        "RaceCode1": "700",
                                                                        "RaceCode2": "",
                                                                        "RaceCode3": "",
                                                                        "RaceCode4": "",
                                                                        "RaceCode5": "",
                                                                        "PositionStatusCode": "1",
                                                                        "TotalYearsOfEduService": 9,
                                                                        "TotalYearsInThisDistrict": 9,
                                                                        "PreviousLastName": "",
                                                                        "PreviousFirstName": "",
                                                                        "PreviousMiddleName": "",
                                                                        "NameSuffix": " ",
                                                                        "Address": "",
                                                                        "AddressCity": "",
                                                                        "AddressState": "",
                                                                        "AddressZipCode": "",
                                                                        "AddressZipExt": "",
                                                                        "HomePhone": "",
                                                                        "EmergencyContactName": "",
                                                                        "EmergencyContactPhone": "",
                                                                        "ID": 884616,
                                                                        "FirstName": "Dario",
                                                                        "LastName": "Abbott",
                                                                        "MiddleName": "Maxwell",
                                                                        "BirthYear": 1986,
                                                                        "BirthDate": "1988-02-22T00:00:00",
                                                                        "FullTimePercentage": 100,
                                                                        "HireDate": "2013-08-30T00:00:00",
                                                                        "LeaveDate": None,
                                                                        "InactiveStatusCode": "",
                                                                        "StateEducatorID": "7777884616",
                                                                        "UserName": "Teacher884-8",
                                                                        "EmailAddress": "dario.abbott@example.com",
                                                                        "PrimaryAeriesSchool": 884,
                                                                        "NetworkLoginID": "dario.abbott",
                                                                        "AlternateEmailAddress": "",
                                                                        "HumanResourcesSystemID": "",
                                                                        "CellPhone": "",
                                                                        "NotificationPreferenceCode": "1",
                                                                        "Title": ""
                                                                    }])
        staff_list = self.aeripyapi.get_staff()
        for staff in staff_list:
            self.assertIsInstance(staff, StaffElement)

    def test_insert_staff(self):
        self.aeripyapi._rest_adapter.post.return_value = Result(201,
                                                                headers={},
                                                                data=
                                                                    {
                                                                        "SchoolAccessPermissions": [],
                                                                        "ExtendedProperties": [],
                                                                        "EarlyChildhoodCertificationCode": "",
                                                                        "Gender": "",
                                                                        "EducationLevelCode": "",
                                                                        "EthnicityCode": "",
                                                                        "RaceCode1": "",
                                                                        "RaceCode2": "",
                                                                        "RaceCode3": "",
                                                                        "RaceCode4": "",
                                                                        "RaceCode5": "",
                                                                        "PositionStatusCode": "",
                                                                        "TotalYearsOfEduService": 0,
                                                                        "TotalYearsInThisDistrict": 0,
                                                                        "PreviousLastName": "",
                                                                        "PreviousFirstName": "",
                                                                        "PreviousMiddleName": "",
                                                                        "NameSuffix": "",
                                                                        "Address": "",
                                                                        "AddressCity": "",
                                                                        "AddressState": "",
                                                                        "AddressZipCode": "",
                                                                        "AddressZipExt": "",
                                                                        "HomePhone": "",
                                                                        "EmergencyContactName": "",
                                                                        "EmergencyContactPhone": "",
                                                                        "ID": 19480317,
                                                                        "FirstName": "Richard",
                                                                        "LastName": "Wintermute",
                                                                        "MiddleName": "",
                                                                        "BirthYear": 0,
                                                                        "BirthDate": None,
                                                                        "FullTimePercentage": 0,
                                                                        "HireDate": None,
                                                                        "LeaveDate": None,
                                                                        "InactiveStatusCode": "",
                                                                        "StateEducatorID": "",
                                                                        "UserName": "",
                                                                        "EmailAddress": "",
                                                                        "PrimaryAeriesSchool": 0,
                                                                        "NetworkLoginID": "",
                                                                        "AlternateEmailAddress": "",
                                                                        "HumanResourcesSystemID": "",
                                                                        "CellPhone": "",
                                                                        "NotificationPreferenceCode": "",
                                                                        "Title": ""
                                                                    })
        data = {
            "id":           "19480317",
            "FirstName":    "Richard",
            "LastName":     "Wintermute"
        }
        staff = self.aeripyapi.insert_staff(data=data)
        self.assertIsInstance(staff, StaffElement)

    def test_update_staff_with_id(self):
        self.aeripyapi._rest_adapter.put.return_value = Result(200,
                                                                 headers={},
                                                                 data={
                                                                "SchoolAccessPermissions": [
                                                                    {
                                                                        "SchoolCode": 884,
                                                                        "ReadOnlyAccess": False,
                                                                        "CommunicationGroup": True
                                                                    }
                                                                ],
                                                                "ExtendedProperties": [],
                                                                "EarlyChildhoodCertificationCode": "",
                                                                "Gender": "M",
                                                                "EducationLevelCode": "2",
                                                                "EthnicityCode": "N",
                                                                "RaceCode1": "700",
                                                                "RaceCode2": "",
                                                                "RaceCode3": "",
                                                                "RaceCode4": "",
                                                                "RaceCode5": "",
                                                                "PositionStatusCode": "1",
                                                                "TotalYearsOfEduService": 9,
                                                                "TotalYearsInThisDistrict": 9,
                                                                "PreviousLastName": "",
                                                                "PreviousFirstName": "",
                                                                "PreviousMiddleName": "",
                                                                "NameSuffix": " ",
                                                                "Address": "",
                                                                "AddressCity": "",
                                                                "AddressState": "",
                                                                "AddressZipCode": "",
                                                                "AddressZipExt": "",
                                                                "HomePhone": "",
                                                                "EmergencyContactName": "",
                                                                "EmergencyContactPhone": "",
                                                                "ID": 884616,
                                                                "FirstName": "Dario",
                                                                "LastName": "Abbott",
                                                                "MiddleName": "Maxwell",
                                                                "BirthYear": 1986,
                                                                "BirthDate": "1988-02-22T00:00:00",
                                                                "FullTimePercentage": 100,
                                                                "HireDate": "2013-08-30T00:00:00",
                                                                "LeaveDate": None,
                                                                "InactiveStatusCode": "",
                                                                "StateEducatorID": "7777884616",
                                                                "UserName": "Teacher884-8",
                                                                "EmailAddress": "dario.abbott@example.com",
                                                                "PrimaryAeriesSchool": 884,
                                                                "NetworkLoginID": "dario.abbott",
                                                                "AlternateEmailAddress": "",
                                                                "HumanResourcesSystemID": "",
                                                                "CellPhone": "",
                                                                "NotificationPreferenceCode": "1",
                                                                "Title": ""
                                                            })
        data = {
            "id":           "884616",
            "first_name":   "Dario",
            "last_name":    "Abbot"
        }
        staff = self.aeripyapi.update_staff(data=data)
        self.assertIsInstance(staff, StaffElement)

    def test_update_staff_no_match_autogen_off(self):
        self.aeripyapi._rest_adapter.put.return_value = Result(201,
                                                                 headers={},
                                                                 data={
                                                                "SchoolAccessPermissions": [
                                                                    {
                                                                        "SchoolCode": 884,
                                                                        "ReadOnlyAccess": False,
                                                                        "CommunicationGroup": True
                                                                    }
                                                                ],
                                                                "ExtendedProperties": [],
                                                                "EarlyChildhoodCertificationCode": "",
                                                                "Gender": "M",
                                                                "EducationLevelCode": "2",
                                                                "EthnicityCode": "N",
                                                                "RaceCode1": "700",
                                                                "RaceCode2": "",
                                                                "RaceCode3": "",
                                                                "RaceCode4": "",
                                                                "RaceCode5": "",
                                                                "PositionStatusCode": "1",
                                                                "TotalYearsOfEduService": 9,
                                                                "TotalYearsInThisDistrict": 9,
                                                                "PreviousLastName": "",
                                                                "PreviousFirstName": "",
                                                                "PreviousMiddleName": "",
                                                                "NameSuffix": " ",
                                                                "Address": "",
                                                                "AddressCity": "",
                                                                "AddressState": "",
                                                                "AddressZipCode": "",
                                                                "AddressZipExt": "",
                                                                "HomePhone": "",
                                                                "EmergencyContactName": "",
                                                                "EmergencyContactPhone": "",
                                                                "ID": 90210,
                                                                "FirstName": "Dylan",
                                                                "LastName": "McKay",
                                                                "MiddleName": "Maxwell",
                                                                "BirthYear": 1986,
                                                                "BirthDate": "1988-02-22T00:00:00",
                                                                "FullTimePercentage": 100,
                                                                "HireDate": "2013-08-30T00:00:00",
                                                                "LeaveDate": None,
                                                                "InactiveStatusCode": "",
                                                                "StateEducatorID": "7777884616",
                                                                "UserName": "Teacher884-8",
                                                                "EmailAddress": "dario.abbott@example.com",
                                                                "PrimaryAeriesSchool": 884,
                                                                "NetworkLoginID": "dario.abbott",
                                                                "AlternateEmailAddress": "",
                                                                "HumanResourcesSystemID": "",
                                                                "CellPhone": "",
                                                                "NotificationPreferenceCode": "1",
                                                                "Title": ""
                                                            })
        data = {
            "id":           "90210",
            "first_name":   "Dylan",
            "last_name":    "McKay"
        }
        staff = self.aeripyapi.update_staff(data=data)
        self.assertIsInstance(staff, StaffElement)

