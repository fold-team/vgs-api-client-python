import os

from setuptools import setup

VERSION = os.environ.get("LIB_VERSION", "0.0.38")

setup(version=VERSION)
