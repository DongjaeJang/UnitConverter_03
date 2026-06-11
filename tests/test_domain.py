"""Track B -- Domain / Logic (Phase 1: D-CNV-01 ~ D-CNV-04)."""

import pytest

from converter import convert_all, to_meter


def test_d_cnv_01_to_meter_feet():
    result = to_meter("feet", 1)
    assert abs(result - 0.3048) < 1e-4


def test_d_cnv_02_convert_all_feet():
    result = convert_all("meter", 2.5)
    assert abs(result["feet"] - 8.20210) < 1e-5


def test_d_cnv_03_feet_yard_consistency():
    pytest.fail("RED: D-CNV-03")


def test_d_cnv_04_convert_all_yard():
    pytest.fail("RED: D-CNV-04")

