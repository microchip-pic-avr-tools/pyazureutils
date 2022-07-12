[![MCHP](images/microchip.png)](https://www.microchip.com)

# pyazureutils - Python Azure utils
pyazureutils is a collection of utilities for interacting with Microsoft Azure

Install using pip from [pypi.org](https://pypi.org/project/pyazureutils):
```bash
pip install pyazureutils
```

Browse source code on [github](https://github.com/microchip-pic-avr-tools/pyazureutils)

Read API documentation on [github](https://microchip-pic-avr-tools.github.io/pyazureutils)

Read the changelog on [github](https://github.com/microchip-pic-avr-tools/pyazureutils/blob/main/CHANGELOG.md)

## Usage
pyazureutils can be used as a command-line interface or a library

### Using the pyazureutils CLI
To get top level help
```bash
pyazureutils --help
```
To get help on specific command (in this example the `iotcentral` command)
```bash
pyazureutils iotcentral --help
```
To get the pyazureutils version
```bash
pyazureutils --version
```

For more CLI usage examples see pypi.md

### Using pyazureutils as a library package
pyazureutils can be used as a library.  Its primary consumer is [iotprovision](https://pypi.org/project/iotprovision)

For usage examples see pypi.md.

## Notes for Linux® systems
This package uses pyedbglib and other libraries for USB transport and some udev rules are required.  
For details see the pyedbglib package: https://pypi.org/project/pyedbglib
