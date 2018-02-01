#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='apistar_shell',
    version='1.0',
    packages=['apistar_shell'],
    url='https://github.com/bahattincinic/apistar_shell',
    license='BSD',
    description='API Star Shell inspired from Django',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    install_requires=['apistar', 'ipython'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
