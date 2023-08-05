Joseki
======

*Reference atmospheric thermophysical properties for radiative transfer
applications in Earth's atmosphere.*

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/joseki.svg
   :target: https://pypi.org/project/joseki/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/joseki
   :target: https://pypi.org/project/joseki
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/joseki
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/joseki/latest.svg?label=Read%20the%20Docs
   :target: https://joseki.readthedocs.io/
   :alt: Read the documentation at https://joseki.readthedocs.io/
.. |Tests| image:: https://github.com/nollety/joseki/workflows/Tests/badge.svg
   :target: https://github.com/nollety/joseki/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/nollety/joseki/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/nollety/joseki
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

This package gathers together data sets of thermophysical properties of the
Earth's atmosphere relevant for radiative transfer applications, and provides
utilities to compute common caracteristic quantities as well as to perform
different operations, such as interpolation and rescaling, on a data set.

Features
--------

* *AFGL Atmospheric Constituent Profiles (0-120 km)* data sets in
  `csv <https://en.wikipedia.org/wiki/Comma-separated_values>`_ and
  `netCDF <https://www.unidata.ucar.edu/software/netcdf/>`_ formats.
* Atmospheric profiles from the
  `Reference Forward Model <http://eodg.atm.ox.ac.uk/RFM/>`_
* U.S. Standard Atmosphere, 1976
* Atmospheric profile interpolation on altitude.
* Projection of the nodes-based profile on the corresponding centers-based altitude mesh.
* Command-line interface.
* Python API.


Requirements
------------

* Python 3.8+


Installation
------------

You can install *Joseki* via pip_ from PyPI_:

.. code:: console

   $ pip install joseki


Python API
----------

Please see the `User Guide`_ for basic use.
For more details, refer to the `API Reference`_.


Command-line interface
----------------------

Please see the `Command-line Reference`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*Joseki* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s
`Hypermodern Python Cookiecutter`_ template.


.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/nollety/joseki/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Command-line Reference: https://joseki.readthedocs.io/en/latest/cli.html
.. _User Guide: https://joseki.readthedocs.io/en/latest/user_guide.html
.. _API Reference: https://joseki.readthedocs.io/en/latest/reference.html
