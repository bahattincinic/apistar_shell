#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='apistar_shell',
    version='0.1',
    packages=['apistar_shell'],
    url='https://github.com/bahattincinic/apistar_shell',
    license='BSD',
    description='API Star Shell inspired from Django',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    install_requires=['apistar', 'ipython'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: API Star',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
