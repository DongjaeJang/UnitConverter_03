"""Track A -- UI / Boundary (Phase 1)."""

import re

import pytest

from validator import FORMAT_ERROR, ValidationError, validate


def test_u_in_01_empty_input():
    with pytest.raises(ValidationError, match=re.escape(FORMAT_ERROR)):
        validate("")