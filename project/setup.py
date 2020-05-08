# -*- coding: utf-8 -*-
"""
Setup for repo template.
The project should contain a **single top-level package**.
Any additional packages and modules are contained in the top level package.
"""

import codecs
import json
from os import path
from setuptools import setup
from setuptools import find_packages


def get_info(source):
    """ Retrieve project info."""
    with open(source, 'r') as fp:
        info = json.load(fp)
    if 'version' not in info:
        raise KeyError("check project.json file: no version number")
    if 'name' not in info:
        raise KeyError("check project.json file: no project name")
    return info


def get_long_description(readme):
    """Get the long description from the README file."""
    with codecs.open(readme, encoding='utf-8') as _rf:
        return _rf.read()


def get_package_name():
    top_level_packages = [p for p in find_packages(exclude=['tests'])
                          if '.' not in p]
    if len(top_level_packages) != 1:
        raise ValueError('Project must contain a single top-level package.')
    return top_level_packages[0]


HERE = path.abspath(path.dirname(__file__))
PROJECT_FILE = path.join(HERE, 'project.json')
README_FILE = path.join(HERE, 'README.rst')

project_info = get_info(PROJECT_FILE)

project_name = project_info['name']
version = project_info['version']
package_name = get_package_name()
long_description = get_long_description(README_FILE)

packages = find_packages(exclude=['tests'])
modules = []

SETUP_REQUIRES = []
INSTALL_REQUIRES = [
    # # this is an example of URL based requirement (see PEP508):
    # 'repo @ http://github.com/user/repo/archive/master.tar.gz',
]
EXTRAS_REQUIRES = {'test': ['pytest']}

print(
    HERE,
    PROJECT_FILE,
    README_FILE,
    project_info,
    project_name,
    version,
    package_name,
    packages
)

setup(
    name=project_name,
    version=version,
    description='A template project with packages',
    long_description=long_description,
    author='Simone Marsili',
    author_email='simo.marsili@gmail.com',
    url='https://github.com/simomarsili/' + project_name,
    py_modules=modules,
    packages=packages,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    package_data={'my_project': ['project.json']},
    include_package_data=True,
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
