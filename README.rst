============================================================================
pandas-frequency-prettyprinter - Pretty print pandas time series frequencies
============================================================================

.. image:: https://travis-ci.org/openmeteo/pandas-frequency-prettyprinter?branch=master
    :alt: Build button
    :target: https://travis-ci.org/openmeteo/pandas-frequency-prettyprinter

Before we go into technical details, a note about the license: It's
GPLv3. This practically means that if you use this module, your
program needs to be GPLv3. Sorry about that.

This package has only one function, ``pprint()``::

   from pandas_frequency_prettyprinter import pprint

   pprint('15T')  # Returns "15 minutes"
   pprint('A-FEB')  # Returns "Annual, anchored at 1 February"
   pprint('AS-MAR')  # Returns "Annual, anchored at end of March"

See the unit tests for a complete list of the possibilities.

Compatible with Python 2 and 3.


License
=======

Copyright (C) 2015 Antonis Christofides.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
