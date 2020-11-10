from setuptools import setup
from setuptools import find_packages

setup(name='timesynth',
      version='0.2.4',
      description='Library for creating synthetic time series',
      url='https://github.com/TimeSynth/TimeSynth',
      author='Abhishek Malali, Reinier Maat, Pavlos Protopapas',
      author_email='anon@anon.com',
      license='MIT',
      include_package_data=True,
      packages=find_packages(),
      install_requires=['numpy', 'scipy', 'sympy', 'symengine>=0.4', 'jitcdde==1.4', 'jitcxde_common==1.4.1'],
      tests_require=['pytest'],
      setup_requires=["pytest-runner"])
