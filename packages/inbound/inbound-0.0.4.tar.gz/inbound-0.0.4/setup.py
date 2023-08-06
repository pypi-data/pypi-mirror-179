#!/usr/bin/env python
import os
import re
import sys
from codecs import open
from glob import glob
from itertools import chain
from os import path

if sys.version_info < (3, 8):
    print("Error: inbound does not support this version of Python.")
    print("Please upgrade to Python 3.8 or higher.")
    sys.exit(1)

from setuptools import find_packages, setup

name = "inbound"
here = path.abspath(path.dirname(__file__))

PANDAS = "pandas>=0.24"

# get package version
with open(path.join(here, name, "__init__.py"), encoding="utf-8") as f:
    result = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not result:
        raise ValueError("Can't find the version in inbound/__init__.py")

    version = result.group(1)

# get dependencies
with open("requirements.txt", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]


def _collect_requirements(requires):
    return sorted(set(chain.from_iterable(requires.values())))


# get test dependencies and installs
with open("requirements-test.txt", encoding="utf-8") as f:
    test_requires = [x.strip() for x in f if x.strip() and not x.startswith("-r")]

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

dbt_require = {
    "dbt": [
        "Jinja2==2.11.3",
        "click>=8,<9",
        'dataclasses>=0.6,<0.9;python_version<"3.8"',
        "isodate>=0.6,<0.7",
        "logbook>=1.5,<1.6",
        "packaging>=20.9,<22.0",
        "sqlparse>=0.2.3,<0.5",
        "typing-extensions>=3.7.4,<3.11",
    ]
}

snowflake_require = {
    "snowflake": [
        # match snowflake-connector-python
        "requests<3.0.0",
        "idna>=2.5,<4",
        "cffi>=1.9,<2.0.0",
    ]
}

extras_require = {
    "dbt": _collect_requirements(dbt_require),
    "snowflake": _collect_requirements(snowflake_require),
}

extras_require["all"] = _collect_requirements(extras_require)

setup(
    name=name,
    version=version,
    description="declarative data ingestion.",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="data ingestion, data loading, data pipelines",
    author="Virksomhetsdatalaget",
    author_email="paul.bencze@nav.no",
    url="https://github.com/navikt/inbound",
    packages=find_packages(exclude=["docs*", "tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    tests_require=test_requires,
    install_requires=requires,
    entry_points={"console_scripts": ["inbound = inbound.framework.cli:main"]},
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    extras_require=extras_require,
)
