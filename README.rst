Aeripy
======

Aeripy is a Python adapter for the Aeries SIS API.

Installation
-------------

Aeripy is supported on Python 3.8+. The recommended way to install Aeripy is via pip.

.. code-block::

    pip install aeripy

Quickstart
___________

.. code-block:: python3

    from aeripy import AeripyApi

    # Aeries Demo Database
    hostname = "demo.aeries.net/aeries/api"

    # Aeries Demo API Key
     api_key = "477abe9e7d27439681d62f4e0de1f5e1"

    aeries = Aeripy(hostname=hostname, api_key=api_key)

    # Get all staff
    staff = aeries.get_staff()

