"""
pyazureutils is a collection of utilities for interacting with Microsoft Azure.
"""
from time import strftime
from os import path
from os import chdir
from os import popen
# To use a consistent encoding
from codecs import open
# Always prefer setuptools over distutils
from setuptools import setup, find_namespace_packages

here = path.abspath(path.dirname(__file__))
chdir(here)

# Get the long description from the pypi file
# Using UTF8 and single newlines
with open(path.join(here, 'pypi.md'), 'rb') as f:
    long_description = f.read().decode("utf-8").replace('\r\n', '\n')

# Set the package name:
name = 'pyazureutils'

"""
Package version :
The version number follow the format major.minor.patch.build
major, minor and patch are set manually according to semantic versioning 2.0.0: https://semver.org
build is an incrementing number set by a build server
in case of installing from source, a Local Version Identifier (see PEP 440) is added
"""

# Package version setup
PACKAGE_VERSION = {
    "major": 1,
    "minor": 0,
    "patch": 0,
    # Will be replaced by build number from Jenkins. For local builds the build number is 0 and the 'snapshot' is
    # added as Local Version Identifier
    "build": '32',
}

version = "{}.{}.{}.{}".format(PACKAGE_VERSION['major'], PACKAGE_VERSION['minor'],
                               PACKAGE_VERSION['patch'], PACKAGE_VERSION['build'])
print("Building {} version: {}".format(name, version))

# Create a "version.py" file in the package
fname = "{}/version.py".format(name)
with open(path.join(here, fname), 'w') as f:
    f.write("\"\"\" This file was generated when {} was built \"\"\"\n".format(name))
    f.write("VERSION = '{}'\n".format(version))
    # The command below can fail if git command not available, or not in a git workspace folder
    result = popen("git rev-parse HEAD").read()
    commit_id = result.splitlines()[0] if result else "N/A"
    f.write("COMMIT_ID = '{}'\n".format(commit_id))
    f.write("BUILD_DATE = '{}'\n".format(strftime("%Y-%m-%d %H:%M:%S %z")))

# Read in requirements (dependencies) file
with open('requirements.txt') as f:
    install_requires = f.read()

setup(
    name=name,
    version=version,
    description='A collection of utilities for interacting with Microsoft Azure',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/microchip-pic-avr-tools/pyazureutils',
    license='MIT',
    author='Microchip Technology',
    author_email='support@microchip.com',
    keywords=['Microchip', 'Azure', 'PIC-IOT'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Embedded Systems',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    packages=find_namespace_packages(exclude=['tests']),

    # List of packages required to use this package
    install_requires=install_requires,

    # List of packages required to develop and test this package
    extras_require={
        'dev': ['pylint', 'pytest', 'mock'],
    },

    # Include files from MANIFEST.in
    include_package_data=True,

    # Installable CLI entry point
    entry_points={
        "console_scripts": [
            "pyazureutils=pyazureutils.cli_pyazureutils:main",
        ]
    },
)
