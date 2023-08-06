
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='listfunctions_1',
  version='0.0.1',
  description='Functions to perform some basic list releated tasks',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Siddhant Gupta',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='list_functions', 
  packages=find_packages(),
  install_requires=[''] 
)