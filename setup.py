#!/usr/bin/env python

from distutils.core import setup

setup(name='MyPackage',
      version='1.0',
      description='A Python Package',
      author='Trent Robbins',
      author_email='robbintt@gmail.com',
      url='http://github.com/robbintt',

      # the generic project will use lib/__init__.py
      # package_dir = {'':'lib'}
      py_modules = ['lib']

      # packages sample:
      # packages=['mypackagedirectory', 'mypackagedirectory.mypackage'],

      # alternative, use a root directory:
      # package_dir = {'':'mypackagedirectory', 'mypackage':'mypackagedirectory.mypackage'}
      # note that each line implies all the packages in that directory, so 
      # any python files in the 'mypackagedirectory' will be installed in the
      # root space and accessible from mypackagename.mypythonfile

      # simplest alternative listing individual modules:
      # py_modules = ['mod1', 'pkg.mod2']
      
     )
