#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="pandas_frequency_prettyprinter",
    version="dev",
    license="GPL3",
    description="Pretty print Pandas timeseries frequencies",
    author="Antonis Christofides",
    author_email="anthony@itia.ntua.gr",
    url="https://github.com/openmeteo/pandas_frequency_prettyprinter",
    packages=find_packages(),
    test_suite="tests",
    install_requires=[
    ],
)
