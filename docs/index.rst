.. Aeripy documentation master file, created by
   sphinx-quickstart on Wed Oct 12 12:26:00 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Aeripy
==================================


Aeripy is a Python adapter for the Aeries SIS API.
It is not difficult to use the ``requests`` library to interact with the Aeries API,
but Aeripy reduces the amount of boilerplate code needed to construct a request,
and turns most requests into a few lines of code (including the import statement).

For example, to get all of the staff from a district you simply:

.. code:: python3

   >>> from aeripy import Aeripy
   >>> aeries = Aeripy(hostname=hostname, api_key=api_key)
   >>> staff_list = aeries.get_staff()

Aeripy also uses dataclasses to model the data once it has been retrieved from the API. This allows for accessing attributes through dot notation and also for auto-completion in IDEs.

.. code:: python3

   >>> staff_list[55]
   StaffElement(school_access_permissions=[], extended_properties=[], early_childhood_certification_code='', gender='M', education_level_code=' ', ethnicity_code='Y', race_code1='700', race_code2='', race_code3='', race_code4='', race_code5='', position_status_code=' ', total_years_of_edu_service=31, total_years_in_this_district=31, previous_last_name='', previous_first_name='', previous_middle_name='', name_suffix=' ', address='', address_city='', address_state='CA', address_zip_code=' ', address_zip_ext=' ', home_phone='', emergency_contact_name='', emergency_contact_phone='', id=994748, first_name='James', last_name='Barrows', middle_name='', birth_year=1957, full_time_percentage=38, inactive_status_code=' ', state_educator_id='7777994748', user_name='', email_address='', primary_aeries_school=994, network_login_id='', alternate_email_address='', human_resources_system_id='', cell_phone='', notification_preference_code='1', title='', birth_date='1959-10-04T00:00:00', hire_date='1992-10-18T00:00:00', leave_date=None)

   >>> staff_list[55].name_last
   'Barrows'

   >>> staff_list[55].id
   994748

See the Code Samples section to see more examples of working with the data before and after interacting with the API.

Current State of Development
-----------------------------
Aeripy currently supports these methods:

* get_schools()
* get_school()
* get_staff()
* get_bell_schedules()
* get_terms()

Eventually, I plan on implementing methods to interact with all of the endpoints covered
in the Aeries documentation, but there is no firm roadmap. As of right now, the next feature will
be to enable query strings for filtering the requests.

There are a lack of tests in the code and a lack of error handling, which both must be addressed before
adding any more features.

.. _getting_started:

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   getting_started/installation
   getting_started/aeries_api

.. toctree::
   :maxdepth: 2
   :caption: Code Samples

   code_samples/csv

.. toctree::
   :maxdepth: 2
   :caption: Aeripy class:

   source/api/aeripy

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
