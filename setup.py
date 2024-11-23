# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='David Hartman Python Template',
    long_description=readme,
    author='David Hartman',
    author_email='dhartman@challengetaker.com',
    url='TBD',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

