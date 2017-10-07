#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

Version = 0.1
setup ( name='django_rest_mockup',
        version = Version,
        install_requires='jsonfield',
        description = "TODO",
        long_description = "TODO",
        author = "Jose Miguel Lopez",
        author_email = "josmilope@gmail.com",
        url = "https://github.com/josemlp91/django_rest_mockup",
        packages = ['django_rest_mockup',],
        license = 'MIT',
        platforms = 'Posix; MacOS X;',
        classifiers = [
            
        ],
     )
