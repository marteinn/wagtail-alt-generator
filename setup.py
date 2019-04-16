#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
from setuptools import setup, find_packages


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


with open("README.md") as f:
    readme = f.read()

# Convert markdown to rst
try:
    from pypandoc import convert

    long_description = convert("README.md", "rst")
except:  # NOQA
    long_description = ""

version = ""
with open("wagtailaltgenerator/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

setup(
    name="wagtailaltgenerator",
    version=version,
    description=(
        "Insert image description and tags with the help of computer vision"
    ),  # NOQA
    long_description=long_description,
    author="marteinn",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/wagtail-alt-generator",
    packages=find_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "example*")
    ),
    include_package_data=True,
    install_requires=["requests", "wagtail>=1.12"],
    extras_require={
        "rekognition": ["boto3>=1.4,<1.5"],
        "google_vision": ["google-api-python-client>=1.5.5"],
        "google_translate": ["google-cloud-translate"],
    },
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Framework :: Django",
        "Topic :: Utilities",
    ],
)
