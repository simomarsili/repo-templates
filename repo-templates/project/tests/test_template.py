# -*- coding: utf-8 -*-
"""Tests."""
import os


def tests_dir():
    """Return None is no tests dir."""
    cwd = os.getcwd()
    basename = os.path.basename(cwd)
    if basename == 'tests':
        return cwd
    tdir = os.path.join(cwd, 'tests')
    if os.path.exists(tdir):
        return tests_dir
    return None


def test_0():
    """Test template."""
    assert bool(1) is True
