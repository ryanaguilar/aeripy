Aeries API
==================

The Aeries API is fairly standard as far as REST APIs go and the endpoint structure is relatively straightforward.
Although the `documentation <https://support.aeries.com/support/solutions/14000072323>`_ is a little scattered, it is pretty complete.

The documentation is grouped into roughly 7 sections:

* `School <https://support.aeries.com/support/solutions/articles/14000113682-aeries-api-school-related-end-points>`_
* `Student <https://support.aeries.com/support/solutions/articles/14000113683-aeries-api-student-related-end-points>`_
* `Attendance <https://support.aeries.com/support/solutions/articles/14000113684-aeries-api-attendance-and-enrollment-related-end-points>`_
* `Student Grades <https://support.aeries.com/support/solutions/articles/14000113685-aeries-api-student-grades-related-end-points>`_
* `Scheduling <https://support.aeries.com/support/solutions/articles/14000113686-aeries-api-scheduling-related-end-points>`_
* `Staff <https://support.aeries.com/support/solutions/articles/14000113687-aeries-api-staff-related-end-points>`_
* `Gradebook <https://support.aeries.com/support/solutions/articles/14000113688-aeries-api-gradebook-related-end-points>`_

However, all of the endpoints are extensions of these 3 base endpoints:

* /schools
* /staff
* /students

For example, gradebook related data can be found on the schools, staff and students endpoints:

* /api/v5/staff/{StaffID}/gradebooks
* /api/v5/schools/{SchoolCode}/sections/{SectionNumber}/gradebooks
* /api/v5/gradebooks/{GradebookNumber}

