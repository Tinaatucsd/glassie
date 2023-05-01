"""
Unit and regression test for the glassie package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import glassie


def test_glassie_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "glassie" in sys.modules
