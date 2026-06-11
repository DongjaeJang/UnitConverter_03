"""Track A — UI / Boundary (Phase 1: U-IN-01 ~ U-IN-03, U-OUT-01)."""

import pytest

def test_u_in_01_empty_input():
    pytest.fail("RED: U-IN-01 — 빈 입력 형식 오류, 구현 없음")

def test_u_in_02_no_colon():
    pytest.fail("RED: U-IN-02 — 콜론 없음 형식 오류, 구현 없음")

def test_u_in_03_reject_negative():
    pytest.fail("RED: U-IN-03 — 음수 거부, 구현 없음")

def test_u_in_04_unknown_unit():
    pytest.fail("RED: U-IN-04 — unknown unit 오류, 구현 없음")

@pytest.mark.parametrize("input_str", [pytest.param(":2.5", id="empty_unit"), pytest.param("meter:", id="empty_value")])
def test_u_in_05_empty_token(input_str):
    pytest.fail("RED: U-IN-05 — 빈 토큰 형식 오류, 구현 없음")

def test_u_out_01_meter_stdout():
    pytest.fail("RED: U-OUT-01 — meter:2.5 CLI 2줄 출력, 구현 없음")
