#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages

with open('README.md', 'r') as file_handle:
	LONG_DESCRIPTION = file_handle.read()

with open('requirements.txt', 'r') as file_handle:
	DEPENDENCIES = file_handle.readlines()

setup(
	name                 = 'unchained',
	version              = '1.0.0',
	url                  = 'https://github.com/durandj/unchained',
	license              = 'MIT',
	description          = 'Tools for getting Django setup quickly',
	long_description     = LONG_DESCRIPTION,
	author               = 'James Durand',
	author_email         = 'james.durand@alumni.msoe.edu',
	packages             = find_packages(),
	include_package_data = True,
	package_data         = {
		'unchained': [
			os.path.join('templates', 'unchained', '*.html'),
		],
	},
	install_requires     = DEPENDENCIES,
)

