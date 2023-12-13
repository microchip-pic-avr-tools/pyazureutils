# pyazureutils
pyazureutils is a collection of utilities for interacting with Microsoft Azure.

![PyPI - Format](https://img.shields.io/pypi/format/pyazureutils)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyazureutils)
![PyPI - License](https://img.shields.io/pypi/l/pyazureutils)

## Overview
pyazureutils is available:

* install using pip from pypi: https://pypi.org/project/pyazureutils
* browse source code on github: https://github.com/microchip-pic-avr-tools/pyazureutils
* read API documentation on github: https://microchip-pic-avr-tools.github.io/pyazureutils
* read the changelog on github: https://github.com/microchip-pic-avr-tools/pyazureutils/blob/main/CHANGELOG.md


## Usage
pyazureutils is intended as a library as well as a stand-alone CLI.
Its primary consumer is iotprovision.
The CLI requires that the Azure CLI ('az') is installed.

## Command-line interface
pyazureutils CLI is invoked with one command, one action and optional switches.  See help and examples below for more details.

Getting help:
```bash
pyazureutils --help
```

Getting command-specific help (iotcentral command):
```bash
pyazureutils iotcentral --help
```

pyazureutils can optionally select the subscription to use:

Example:
```bash
pyazureutils --subscription "My Azure" iotcentral register-device
```

### iotcentral command
The iotcentral command supports device registration with Azure IoT Central

Example:
```bash
pyazureutils iotcentral register-device
```

Device registration can optionally include the switches:
```
--application-name <application name (URL) to register with>
--display-name <display name to use for the device registration>
--certificate-file <certificate to use for registration, if not read from a kit>
--device-template-name <device template to use for registration>
```

Example:
```bash
pyazureutils --subscription "My Azure" iotcentral register-device --app custom-227clcx93h8 --template "PIC-IoT WM" --display-name "My PIC-IoT Kit"
```

## Logging
This package uses the Python logging module for publishing log messages to library users.
A basic configuration can be used (see example below), but for best results a more thorough configuration is
recommended in order to control the verbosity of output from dependencies in the stack which also use logging.
```python
import logging
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)
```

## Dependencies
This package uses pyedbglib through other libraries for USB communications.  For more information see: https://pypi.org/project/pyedbglib/.

## Versioning
pyazureutils version can be determined by:
```python
from pyazureutils import __version__ as pyazureutils_version
print(f"pyazureutils version {pyazureutils_version}")
```