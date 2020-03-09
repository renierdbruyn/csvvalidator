#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages

requires = [
      'python-dateutil',
]

setup(name='csvvalidator',
      version='1.4-SNAPSHOT',
      author='Alistair Miles',
      author_email='alimanfoo@googlemail.com',
      url='https://github.com/alimanfoo/csvvalidator',
      license='MIT License',
      py_modules=['csvvalidator'],
      description='A simple library for validating data contained in CSV files or similar row-oriented data sources.',
      long_description=open('README.txt').read(),
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'
                   ],
      find_packages=find_packages(),
      install_requires=requires,
      )
