#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup, find_packages

import djangosphinx
from six.moves import map

setup(
    name='django-sphinx',
    version=".".join(map(str, djangosphinx.__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-sphinx',
    install_requires=['django'],
    description = 'An integration layer bringing Django and Sphinx Search together.',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
