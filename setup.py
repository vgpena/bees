import os
from setuptools import setup, find_packages

setup(
	name='bees',
	version=__import__('bees').__version__,
	description='I like my women like I like my coffee: covered in BEEEEEEEEEEES',
	packages=find_packages(),
	include_package_data=True,
)