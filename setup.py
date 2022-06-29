import os

from setuptools import setup

VERSION = os.environ.get("LIB_VERSION", "0.0.40")

setup(version=VERSION)
