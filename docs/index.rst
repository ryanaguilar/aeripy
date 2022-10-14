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

   from aeripy import Aeripy
   aeries = Aeripy(hostname=hostname, api_key=api_key)
   aeries.get_staff()

Current State of Development
-----------------------------
Aeripy currently supports these methods:

* get_schools()
* get_school()
* get_staff()
* get_bell_schedules()
* get_terms()

Eventually, I plan on implementing methods to interact with all of the endpoints covered
in Aeries documentation, but there is no firm roadmap. As of right now, the next feature will
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
