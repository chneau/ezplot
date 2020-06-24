#!/usr/bin/env python

from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ezplot",
    version="0.0.1",
    install_requires=requirements,
    py_modules=["ezplot"],
    entry_points={"console_scripts": ["ezplot=ezplot:main"]},
)
