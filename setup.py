import os
import logging
from setuptools import setup
from setuptools import find_packages

setup(name='timesynth',
      version='0.1',
      description='Library for creating synthetic time series',
      url='https://github.com/TimeSynth/TimeSynth',
      author='Abhishek Malali, Reinier Maat, Pavlos Protopapas',
      author_email='anon@anon.com',
      license='MIT',
      dependency_links=['git+https://github.com/neurophysik/jitcdde.git@697fb23#egg=jitcdde'],  # for jitcdde
      include_package_data=True,
      packages=find_packages(),
      install_requires=['numpy', 'scipy', 'nose', 'jitcdde'])
