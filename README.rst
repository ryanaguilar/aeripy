AeriPy
======

AeriPy is a Python adapter for the Aeries SIS API.

Installation
-------------

AeriPy is supported on Python 3.8+. The recommended way to install AeriPy is via pip.

.. code-block:: bash

    pip install aeripy

Quickstart
___________

The below example uses the Aeries demo database API_KEY and API url.  Both are found in their `documentation <https://support.aeries.com/support/solutions/articles/14000113681-aeries-api-building-a-request>`_.


.. code-block:: python

    from aeripy import AeripyApi
    aeries = AeripyApi(hostname='demo.aeries.net/aeries/api/', api_key='477abe9e7d27439681d62f4e0de1f5e1')

    # Get all staff
    staff = aeries.get_staff()
