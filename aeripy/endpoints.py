"""List of Aeries API endpoints
https://support.aeries.com/support/solutions/articles/14000070569-api-quick-reference-guide"""

API_PATH = {
    "system_info":          "/systeminfo",
    "schools":              "/schools",
    "school":               "/schools/{school_code}",
    "terms":                "/schools/{school_code}/terms",
    "bell_schedule":        "/schools/{school_code}/BellSchedule",
    "bell_schedule_date":   "/schools/{school_code}/BellSchedule/date/{date}",
    "calendar":             "/schools/{school_code}/calendar",
    "absence_codes":        "/schools/{school_code}/AbsenceCodes",
    "absence_code":         "/schools/{school_code}/AbsenceCodes/{AbsenceCode}",
    "staff":                "/staff/",
    "staff_id":             "/staff/{staff_id}",
    "staff_hrid":           "/staff/hrid/{hr_id}",
    "assignments":          "/staff/{staff_id}/assignments",
    "assignments_type":     "/staff/{staff_id}/assignments/{assignment_type}",
    "assignments_sequence": "/staff/{staff_id}/assignments/{assignment_type}/{sequence_number}"
}

