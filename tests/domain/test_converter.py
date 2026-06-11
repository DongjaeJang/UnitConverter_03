"""Track B — Domain RED 스켈레톤 (D-CNV-*)"""

import pytest


def test_d_cnv_01_one_feet_to_meter(conversion_ratios):
    # Given: 1 feet
    # When: to_meter(1.0, "feet", registry)
    # Then: ≈ 0.3048 m (±FLOAT_EPS)
    pytest.fail("RED: D-CNV-01 — 1 feet → 0.3048 m, 구현 없음")


def test_d_cnv_02_convert_all_from_meter(conversion_ratios):
    # Given: 2.5 meter, registry 3 units
    # When: convert_all(2.5, "meter", registry)
    # Then: feet=8.20210 (5 decimal places)
    pytest.fail("RED: D-CNV-02 — 2.5 m → 8.20210 ft, 구현 없음")


def test_d_cnv_03_feet_to_yard_via_meter(conversion_ratios):
    # Given: feet input, registry with meter/feet/yard
    # When: convert feet value to yard via meter
    # Then: cross-conversion matches meter-based ratio
    pytest.fail("RED: D-CNV-03 — feet→yard meter 경유 일치, 구현 없음")
