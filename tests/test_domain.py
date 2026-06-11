"""Track B -- Domain / Logic (Phase 1: D-CNV-01 ~ D-CNV-04)."""

from converter import to_meter


def test_d_cnv_01_to_meter_feet():
    result = to_meter("feet", 1)
    assert abs(result - 0.3048) < 1e-4
