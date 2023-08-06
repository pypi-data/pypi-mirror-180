#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Tigromag
:license: Apache license, Version 2.0, see LICENSE file
:copyright: (c) 2022 Tigromag
"""

version = "1.0.0"
'''
with open('README.md', encoding = 'utf-8') as f:
    long_description = f.read()
'''

long_description = '''Python module for convert numbers
(in various number systems)'''

setup(
    name='convert_api_Tigromag',
    version=version,

    author='Tigromag',
    author_email='tigromag010@gmail.com',

    description=(
        u'Python module for convert numbers'
        u'(in various number systems)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Tigromag/convert_api',
    download_url='https://github.com/Tigromag/convert_api/archive/refs/heads/main.zip',

    license='Apache license, Version 2.0, see LICENSE file',

    packages=['convert_api_Tigromag'],
    install_requires=['aiohttp', 'aiofiles'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
