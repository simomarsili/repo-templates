#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bump_version
============

Bump version number, updating the __init__.py file in the top-level package.
The __init__ module defines a __version__ string following the
 major.minor[.micro] scheme.

"""
import argparse
import sys
from pathlib import Path

from setuptools import find_packages

VALID_FIELD_NAMES = ['major', 'minor', 'micro']
NAME_PREFIX = 'v'


def get_command(description=None):
    """Command line args."""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description,
        epilog=' ')

    parser.add_argument(
        '-f',
        '--field',
        type=str,
        help='field to bump. valid options are: major minor micro)',
        default='micro')

    return parser.parse_args().field


def bump(string, target_field):
    """Parse version fields in string."""

    try:
        fds = [int(x) for x in string.split('.')]
    except TypeError:
        raise TypeError('Check __version__ (major.minor[.micro] scheme)')
    n_fields = len(fds)
    if n_fields not in [2, 3]:
        raise ValueError('Check __version__ (major.minor[.micro] scheme)')
    if n_fields == 2:
        n_fields += 1
        fds.append(0)
    try:
        target_field = VALID_FIELD_NAMES.index(target_field)
    except ValueError:
        raise ValueError('Valid field names are: %s' %
                         ', '.join(VALID_FIELD_NAMES))
    fds = [
        fds[k] + 1 if k == target_field else
        (fds[k] if k < target_field else 0) for k in range(3)
    ]
    # if the last field is zero, ignore it
    if fds[-1] == 0:
        fds.pop()
    string = '.'.join([str(fd) for fd in fds])
    print('Version bumped to %s' % string, file=sys.stderr)
    return string


def get_package_name():
    'The top-level package name.'
    top_level_packages = [
        p for p in find_packages(exclude=['tests']) if '.' not in p
    ]
    if len(top_level_packages) != 1:
        raise ValueError('Project must contain a single top-level package.')
    return top_level_packages[0]


if __name__ == '__main__':
    import os

    field_to_bump = get_command(description=__doc__)

    package = get_package_name()

    base_dir = Path(os.getcwd())
    init_file = base_dir / package / '__init__.py'

    project_info = {}
    with open(init_file, 'r') as fp:
        filedata = fp.read()

    exec(filedata, project_info)  # pylint:disable=exec-used

    try:
        old_version_number = project_info['__version__']
    except KeyError:
        # no version number in package.json
        raise KeyError('check %s: no version number' % init_file)
    else:
        new_version_number = bump(old_version_number, field_to_bump)
        old_version_name = NAME_PREFIX + old_version_number
        new_version_name = NAME_PREFIX + new_version_number

    # Replace the target version string
    filedata = filedata.replace(old_version_number, new_version_number)

    # update init file
    with open(init_file, 'w') as fp:
        print(filedata, file=fp)
