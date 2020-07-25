#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model.'
URL = 'https://github.com/darshikaf/house-price-predictor'
EMAIL = 'darshika58@gmail.com'
AUTHOR = 'darshikaf'
REQUIRES_PYTHON = '>=3.7.0'


def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

test_requirements = ["coverage", "pytest", "pytest-cov"]

class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args.split("|"))
        sys.exit(errno)

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
# try:
#     with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
#         long_description = '\n' + f.read()
# except FileNotFoundError:
#     long_description = DESCRIPTION

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    # long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'regression_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # entry_points={
    #     "console_scripts": ["housing = regression_model.cli:VERSION"]
    # },
    test_suite="tests",
    tests_require=test_requirements,
    cmdclass={"test": PyTest},
)