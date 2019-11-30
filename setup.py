""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.

References:
https://github.com/pypa/sampleproject/blob/master/setup.py
https://github.com/biopython/biopython/blob/master/setup.py
http://python-packaging.readthedocs.io/en/latest/index.html
"""
# Modules Used
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import os
import sys

# Set the home path of the setup script/package
__version__ = '0.1.0'
project_path = os.path.dirname(os.path.abspath(__file__))
project_name = os.path.basename(project_path)
project_url = 'https://github.com/sdhutchins/jxn-open-data-api'


def readme():
    """Get the long description from the README file."""
    with open(path.join(project_path, 'README.rst'), encoding='utf-8') as f:
        return f.read()

# Setup the package by adding information to these parameters


setup(
    name=project_name,
    author='Shaurita D. Hutchins',
    author_email='shaurita.d.hutchins@gmail.com',
    description="Access Jackson, MS open government data using a python API wrapper.",
    version=__version__,
    long_description=readme(),
    url=project_url,
    license='MIT',
    keywords='open-data api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Framework :: Cookiecutter'
    ],
    # Packages will be automatically found if not in this list.
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    entry_points={
    },
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
