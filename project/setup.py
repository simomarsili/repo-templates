# -*- coding: utf-8 -*-
"""
Setup template.
The repo should contain a single top-level package or module
 **WITH THE SAME NAME OF THE PROJECT**.
Any additional packages and modules are contained in the top level package.
"""
import codecs
import json
from os import path
from setuptools import setup
from setuptools import find_packages


def get_package_info(source):
    """ Retrieve package info."""
    with open(source, 'r') as fp:
        info = json.load(fp)
    try:
        version = info['version']
    except KeyError:
        # no version number in version.json
        raise KeyError("check package.json file: no version number")
    try:
        name = info['name']
    except KeyError:
        # no version number in version.json
        raise KeyError("check package.json file: no project name")
    return name, version


def get_long_description(readme):
    """Get the long description from the README file."""
    with codecs.open(readme, encoding='utf-8') as _rf:
        return _rf.read()


HERE = path.abspath(path.dirname(__file__))
# package.json and README are in the project root
PACKAGE_FILE = path.join(HERE, 'package.json')
README_FILE = path.join(HERE, 'README.rst')


PROJECT_NAME, VERSION = get_package_info(PACKAGE_FILE)
LONG_DESCRIPTION = get_long_description(README_FILE)

PACKAGES = find_packages(exclude=['tests'])
# PACKAGES = []
# MODULES = []

SETUP_REQUIRES = []
INSTALL_REQUIRES = [
    # # this is an example of URL based requirement (see PEP508):
    # 'repo @ http://github.com/user/repo/archive/master.tar.gz',
]
EXTRAS_REQUIRES = {'test': ['pytest']}


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description='A template project with packages',
    long_description=LONG_DESCRIPTION,
    author='Simone Marsili',
    author_email='simo.marsili@gmail.com',
    url='https://github.com/simomarsili/' + PROJECT_NAME,
    # py_modules=MODULES,
    packages=PACKAGES,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    license='BSD 3-Clause',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
