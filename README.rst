Aeripy
======
.. image:: https://img.shields.io/pypi/v/aeripy.svg
   :target: https://pypi.org/project/aeripy/

.. image:: https://img.shields.io/pypi/pyversions/aeripy.svg
   :target: https://pypi.org/project/aeripy/

Aeripy is a Python adapter for the Aeries SIS API.  It is essentially a wrapper for the popular `requests <https://github.com/psf/requests>`_ library.

Note: Aeripy is in no way affiliated with Aeries Software, Inc. This module is based on their publicly available documentation.

Installation
-------------

Aeripy is supported on Python 3.8+. The recommended way to install Aeripy is via pip.

.. code-block::

    pip install aeripy

Quickstart
___________

The following example uses the Aeries demo database URL and API key.
Both are found in their `documentation <https://support.aeries.com/support/solutions/articles/14000113681-aeries-api-building-a-request>`_.

To use this module with your own Aeries database, you will need your district's URL and API key.  See the `URL and API Key`_ section for details.

.. code-block:: python3

    from aeripy import Aeripy

    # Aeries Demo Database
    hostname = "demo.aeries.net/aeries/api"

    # Aeries Demo API Key
    api_key = "477abe9e7d27439681d62f4e0de1f5e1"

    aeries = Aeripy(hostname=hostname, api_key=api_key)

    # Get all staff
    staff = aeries.get_staff()

    staff
    # Output

URL and API Key
------------------------

You must have access to the Security section in Aeries Web to obtain or create the API key.


