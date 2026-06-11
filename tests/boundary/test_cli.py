"""Track A — Boundary RED 스켈레톤 (U-*)"""

import pytest


def test_u_in_01_empty_input():
    # Given: "" (empty input)
    # When: parse/validate input
    # Then: format error message
    pytest.fail("RED: U-IN-01 — 빈 입력 형식 오류, 구현 없음")


def test_u_in_02_missing_colon():
    # Given: "meter" (no colon)
    # When: parse input
    # Then: format error message
    pytest.fail("RED: U-IN-02 — 콜론 없음 형식 오류, 구현 없음")


def test_u_in_03_negative_value():
    # Given: "meter:-1"
    # When: validate value
    # Then: reject negative
    pytest.fail("RED: U-IN-03 — 음수 거부, 구현 없음")


def test_u_out_01_meter_output(sample_input):
    # Given: "meter:2.5"
    # When: run converter CLI
    # Then: output lines for feet and yard
    pytest.fail("RED: U-OUT-01 — meter:2.5 전 단위 출력, 구현 없음")
