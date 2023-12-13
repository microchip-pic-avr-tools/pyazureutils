"""
Python Utilities for Microsoft Azure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyazureutils is a collection of utilities for interacting with Microsoft Azure.

pyazureutils can be used as a library by instantiating any of the contained classes.

Overview
~~~~~~~~

pyazureutils is available:
    * install using pip from pypi: https://pypi.org/project/pyazureutils
    * browse source code on github: https://github.com/microchip-pic-avr-tools/pyazureutils
    * read API documentation on github: https://microchip-pic-avr-tools.github.io/pyazureutils
    * read the changelog on github: https://github.com/microchip-pic-avr-tools/pyazureutils/blob/main/CHANGELOG.md

Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This package uses the Python logging module for publishing log messages to library users.
A basic configuration can be used (see example), but for best results a more thorough configuration is
recommended in order to control the verbosity of output from dependencies in the stack which also use logging.
"""

# Build number part of version will be replaced by build number from Jenkins.
# For local builds the build number is 0 and the 'snapshot' is added as Local Version Identifier
__version__ = "1.1.4.9"

# The GIT commit ID and build date are generated by Jenkins when building the package
COMMIT_ID = 'c773612d04e4e2d0a68d3d795ad132fc498ed70e'
BUILD_DATE = '2023-12-12 12:44:14'

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
