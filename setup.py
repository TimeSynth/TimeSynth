import sys
import logging
from setuptools import setup
from setuptools import find_packages
import subprocess


# Manage requirments
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


# Install
setup(name='timesynth',
      version='0.2.3',
      description='Library for creating synthetic time series',
      url='https://github.com/TimeSynth/TimeSynth',
      author='Abhishek Malali, Reinier Maat, Pavlos Protopapas',
      author_email='anon@anon.com',
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      install_requires=requirements,
      tests_require=['pytest'],
      setup_requires=["pytest-runner"])
