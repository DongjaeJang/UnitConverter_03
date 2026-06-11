"""Track B — Domain RED 스켈레톤 (D-CNV-*)"""

import pytest


def test_d_cnv_01_one_feet_to_meter(conversion_ratios):
    # Given: 1 feet
    # When: to_meter(1.0, "feet", registry)
    # Then: ≈ 0.3048 m (±FLOAT_EPS)
    pytest.fail("RED: D-CNV-01 — 1 feet → 0.3048 m, 구현 없음")
