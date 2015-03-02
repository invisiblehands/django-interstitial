#!/usr/bin/env python

from setuptools import setup
from setuptools import Command


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='interstitial',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A pluggable django application for configuring and displaying interstitials.',
    long_description=README,
    url='https://github.com/invisiblehands/django-interstitial/',
    author_email='cody@invisiblehands.ca',
    author='Cody Redmond',
    install_requires=[
        'Django>=1.6.0',
    ]
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License'
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
)
