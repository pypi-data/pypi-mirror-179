#!/usr/bin/env python3
from setuptools import setup, Extension

from distutils.command import build as build_module
import os
import platform
import sys
import unittest
import shutil

MAJOR_VERSION = 1
MINOR_VERSION = 1
POST_VERSION = 0

if POST_VERSION:
    VERSION_STRING = '%d.%d-%d' % (MAJOR_VERSION, MINOR_VERSION, POST_VERSION)
else:
    VERSION_STRING = '%d.%d' % (MAJOR_VERSION, MINOR_VERSION)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

compile_args = []
# Grab all the source files
source_files = []
for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.cpp') or file.endswith('.c'):
            source_files.append(os.path.join(root, file))

dev_ctl_extension = Extension(
    'slthost.dev_ctl',
    define_macros=[('STEAP_STATIC_LIB', None)],
    include_dirs=['include', '3rd\steap_api'],
    libraries=["steap_api"],
    library_dirs=['3rd\steap_api'],
    sources=source_files,
    extra_compile_args=compile_args)

setup(name='slthost',
      version=VERSION_STRING,
      description='Library for interfacing with Sealta devices in Python',
      long_description=read('README.rst'),
      license="MIT",
      author='yufan',
      author_email='1014720522@qq.com',
      maintainer='yufan',
      maintainer_email='1014720522@qq.com',
      url='',
      packages=['slthost'],
      include_package_data=True,
      ext_modules=[dev_ctl_extension],
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
      ],)
