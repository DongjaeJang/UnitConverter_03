"""Track A -- UI / Boundary (Phase 1)."""

import pytest

from validator import FORMAT_ERROR, NEGATIVE_ERROR, ValidationError, validate


def test_u_in_01_empty_input():
    with pytest.raises(ValidationError, match=FORMAT_ERROR):
        validate("")


def test_u_in_02_no_colon():
    with pytest.raises(ValidationError, match=FORMAT_ERROR):
        validate("meter")


def test_u_in_03_reject_negative():
    with pytest.raises(ValidationError, match=NEGATIVE_ERROR):
        validate("meter:-1")


def test_u_out_01_meter_stdout():
    pytest.fail("RED: U-OUT-01")


def test_u_in_04_unknown_unit():
    pytest.fail("RED: U-IN-04")


@pytest.mark.parametrize("input_str", [pytest.param(":2.5", id="empty_unit"), pytest.param("meter:", id="empty_value")])
def test_u_in_05_empty_token(input_str):
    pytest.fail("RED: U-IN-05")
