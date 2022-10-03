"""List of Aeries API endpoints
https://support.aeries.com/support/solutions/articles/14000070569-api-quick-reference-guide"""

API_PATH = {
    "system_info":          "/systeminfo",
    "schools":              "/schools",
    "school":               "/schools/{school_code}",
    "terms":                "/schools/{school_code}/terms",
    "bell_schedule":        "/schools/{school_code}/BellSchedule",
    "bell_schedule_date":    "/schools/{school_code}/BellSchedule/date/{date}"
}

