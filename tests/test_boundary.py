"""Track A -- UI / Boundary (Phase 1)."""

import re

import pytest

from validator import FORMAT_ERROR, NEGATIVE_ERROR, ValidationError, validate


def test_u_in_01_empty_input():
    with pytest.raises(ValidationError, match=re.escape(FORMAT_ERROR)):
        validate("")


def test_u_in_02_no_colon():
    with pytest.raises(ValidationError, match=re.escape(FORMAT_ERROR)):
        validate("meter")


def test_u_in_03_reject_negative():
    with pytest.raises(ValidationError, match=NEGATIVE_ERROR):
        validate("meter:-1")