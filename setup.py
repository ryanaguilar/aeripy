# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="aeripy",
    version="0.2.16",
    description="Aeries API Python Adapter",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://aeripy.readthedocs.io/",
    author="Ryan Aguilar",
    author_email="ryanaguilar323@gmail.com",
    license="Simplified BSD License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["aeripy"],
    include_package_data=True,
    install_requires=["requests"]
)
