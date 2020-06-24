#!/usr/bin/env python

from setuptools import setup

setup(
    name="ezplot",
    version="0.0.1",
    py_modules=["ezplot"],
    entry_points={"console_scripts": ["ezplot=ezplot:main"]},
)
