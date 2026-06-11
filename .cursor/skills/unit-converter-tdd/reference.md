# UnitConverter_03 — Test ID Reference

> SSOT: `docs/PRD.md` §7 C2C · §8 Dual-Track RED 설계표

**표시/내부 정밀도 SSOT:** Domain `D-CNV-*` 소수 **5자리**; CLI `U-OUT-01`·FR-02 소수 **1자리** (8.2 feet, 2.7 yard).

## Track · Phase

| Track | Layer | TC | RED 순서 |
|-------|-------|-----|----------|
| B | Domain | `D-*` | **1번째** |
| A | Boundary | `U-*` | **2번째** |

## Phase 1 — Core (10 TC)

| Test ID | Given → Then |
|---------|--------------|
| D-CNV-01 | 1 feet → 0.3048 m (±ε) |
| D-CNV-02 | 2.5 m → 8.20210 ft |
| D-CNV-03 | feet → yard, meter 경유 일관 |
| D-CNV-04 | 2.5 m → 2.73403 yard |
| U-IN-01 | `""` → Format error |
| U-IN-02 | `meter` → Format error |
| U-IN-03 | `meter:-1` → Reject negative |
| U-IN-04 | `mile:1` → Unknown unit |
| U-IN-05 | `:2.5` / `meter:` → Format error |
| U-OUT-01 | `meter:2.5` → stdout 2줄(feet·yard, 소수 1자리); meter 자기변환 줄 없음 |

## Phase 2 — Extension (P1)

| Test ID | Given → Then |
|---------|--------------|
| D-CFG-01 | 손상 JSON → ConfigError |
| D-REG-01 | cubit=0.4572 m 등록 → 변환 가능 |
| U-OUT-02 | `--format json` → 유효 JSON |

상세: `docs/PRD.md` · `docs/ARCHITECTURE.md`
