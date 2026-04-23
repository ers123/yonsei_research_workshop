#!/usr/bin/env python3
"""연구팀 Lite — 스모크 테스트.

Ollama · Streamlit 서버 없이 구조 정합성만 확인:
  1. 핵심 모듈 임포트
  2. 프롬프트 스왑 로직 (주제 탐색 / 선행연구 / RQ 세 단계 × 3 역할 = 9개 프롬프트)
  3. Lite 전용 기본값 (per_agent_mode, agent_models, preferred model)
  4. 템플릿 · 예시 시나리오 로드
  5. 세션 영속성 round-trip (JSON 저장/복원)
  6. 산출물 레지스트리 (EXPORT_REGISTRY) 일관성

사용:
    python smoke_test.py

종료 코드:
    0  — 전부 통과
    1+ — 실패 개수
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path


PASSED = 0
FAILED = 0
FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASSED, FAILED
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {label}" + (f"  — {detail}" if detail else ""))
    if cond:
        PASSED += 1
    else:
        FAILED += 1
        FAILURES.append(f"{label} — {detail}")


def section(title: str) -> None:
    print(f"\n── {title} ──")


def main() -> int:
    here = Path(__file__).parent
    sys.path.insert(0, str(here))

    print("=" * 60)
    print("  연구팀 Lite — Smoke Test")
    print("=" * 60)

    # ── 1. 임포트 ─────────────────────────────────────────
    section("1. 핵심 모듈 임포트")
    try:
        import agents  # noqa: F401
        check("agents.py import", True)
    except Exception as e:
        check("agents.py import", False, str(e))
        return _report()

    try:
        import templates  # noqa: F401
        check("templates.py import", True)
    except Exception as e:
        check("templates.py import", False, str(e))

    try:
        import resources  # noqa: F401
        check("resources.py import", True)
    except Exception as e:
        check("resources.py import", False, str(e))

    try:
        import sessions  # noqa: F401
        check("sessions.py import", True)
    except Exception as e:
        check("sessions.py import", False, str(e))

    try:
        import exporters  # noqa: F401
        check("exporters.py import", True)
    except Exception as e:
        check("exporters.py import", False, str(e))

    # ── 2. 프롬프트 스왑 로직 ─────────────────────────────
    section("2. 프롬프트 스왑 (3 stages × 3 roles = 9)")
    from agents import STAGE_PROMPTS, get_prompt, ROLE_LABELS, ADVISOR_PROMPT

    expected_stages = ["주제 탐색", "선행연구 정리", "Research Question 도출"]
    for stage in expected_stages:
        check(f"STAGE_PROMPTS has '{stage}'", stage in STAGE_PROMPTS)
        if stage in STAGE_PROMPTS:
            for role in ["scout", "critic", "director"]:
                p = STAGE_PROMPTS[stage][role]
                check(
                    f"  {stage} / {role} prompt non-empty",
                    isinstance(p, str) and len(p) > 100,
                    f"len={len(p) if isinstance(p, str) else 'NA'}",
                )

    # Grounding rule propagated to all prompts
    for stage in expected_stages:
        for role in ["scout", "critic", "director"]:
            p = STAGE_PROMPTS[stage][role]
            check(
                f"  {stage} / {role} contains grounding rule",
                "근거 태깅" in p or "[근거:" in p,
            )

    # get_prompt dispatcher
    check(
        "get_prompt('주제 탐색', 'scout') matches STAGE_PROMPTS",
        get_prompt("주제 탐색", "scout") == STAGE_PROMPTS["주제 탐색"]["scout"],
    )
    check(
        "get_prompt falls back on unknown stage",
        get_prompt("모르는단계", "scout") == STAGE_PROMPTS["주제 탐색"]["scout"],
    )

    # ROLE_LABELS covers 4 roles
    for role in ["scout", "critic", "director", "advisor"]:
        check(f"ROLE_LABELS['{role}'] exists", role in ROLE_LABELS)

    check("ADVISOR_PROMPT non-empty", isinstance(ADVISOR_PROMPT, str) and len(ADVISOR_PROMPT) > 100)

    # ── 3. Lite 기본값 ────────────────────────────────────
    section("3. Lite 전용 기본값")
    app_text = (here / "app.py").read_text(encoding="utf-8")

    check(
        'per_agent_mode default = True',
        '"per_agent_mode": True' in app_text,
    )
    check(
        'agent_models default has gemma4:e4b',
        'gemma4:e4b' in app_text,
    )
    check(
        'LITE_ALLOWED_MODELS ladder exists',
        'LITE_ALLOWED_MODELS' in app_text and '("gemma4:e4b"' in app_text,
    )
    check(
        'Ladder includes 3 tiers (16GB, 8GB, 4GB)',
        'gemma4:e4b' in app_text and 'qwen2.5:3b' in app_text and 'gemma3:1b' in app_text,
    )
    check(
        'lite_model_pick helper exists',
        'def lite_model_pick' in app_text,
    )
    check(
        'lite_model_available back-compat shim',
        'def lite_model_available' in app_text,
    )
    check(
        'Sidebar brand shows Lite',
        '연구팀 · Lite' in app_text,
    )
    check(
        'Banner: 1단계 / 2단계 두 단계 안내',
        '1단계 · 기본 시연' in app_text and '2단계 · 티키타카' in app_text,
    )
    check(
        'Sidebar: missing-model warning with pull command',
        '미설치' in app_text and 'ollama pull' in app_text,
    )
    check(
        'Sidebar: installed-model green badge',
        '세 역할(수연·준호·지은) 모두' in app_text,
    )
    check(
        'Per-agent widget keys set pre-render (session_state pre-populate)',
        'if widget_key not in st.session_state' in app_text,
    )

    # Runtime behavior check via actual import (no streamlit context needed for helpers)
    from app import lite_model_pick, lite_model_available
    check(
        'lite_model_pick — both tiers installed → prefers e4b',
        lite_model_pick([("gemma4:e4b", 9.6), ("qwen2.5:3b", 2.0)])[0] == "gemma4:e4b",
    )
    check(
        'lite_model_pick — 8GB fallback → qwen2.5:3b',
        lite_model_pick([("qwen2.5:3b", 2.0), ("ex", 5.0)])[0] == "qwen2.5:3b",
    )
    check(
        'lite_model_pick — 4GB fallback → gemma3:1b',
        lite_model_pick([("gemma3:1b", 0.8)])[0] == "gemma3:1b",
    )
    check(
        'lite_model_pick — suffix variant (e4b-it-q4)',
        lite_model_pick([("gemma4:e4b-it-q4_K_M", 9.6)]) is not None,
    )
    check(
        'lite_model_pick — none of allowed → None',
        lite_model_pick([("gemma4:26b", 16.8), ("deepseek-r1:14b", 8.4)]) is None,
    )
    check(
        'lite_model_available back-compat — True when any tier installed',
        lite_model_available([("qwen2.5:3b", 2.0)]) is True,
    )
    check(
        'lite_model_available back-compat — False when none',
        lite_model_available([]) is False,
    )

    # ── 4. 템플릿 · 예시 ─────────────────────────────────
    section("4. 템플릿 · 예시 시나리오")
    from templates import (
        RESEARCH_FIELDS, RESEARCH_STAGES, DEMO_INPUTS,
        DEMO_PROJECT_NAME, DEMO_RESOURCE_PATH, EXPORT_LABELS,
    )

    check("RESEARCH_STAGES == STAGE_PROMPTS keys",
          set(RESEARCH_STAGES) == set(STAGE_PROMPTS.keys()))
    check("RESEARCH_FIELDS non-empty", len(RESEARCH_FIELDS) > 0)
    check("DEMO_INPUTS has field/stage/keywords/context",
          all(k in DEMO_INPUTS for k in ["field", "stage", "keywords", "context"]))
    check("DEMO_PROJECT_NAME non-empty", bool(DEMO_PROJECT_NAME))
    check("DEMO_RESOURCE_PATH points to sample file",
          os.path.exists(DEMO_RESOURCE_PATH),
          f"path={DEMO_RESOURCE_PATH}")

    # ── 5. 세션 영속성 round-trip ─────────────────────────
    section("5. 세션 영속성 round-trip")
    from sessions import save_session, load_session, new_version_entry

    with tempfile.TemporaryDirectory() as tmpdir:
        # Patch SESSIONS_DIR for isolation
        import sessions as sess_mod
        original_dir = sess_mod.SESSIONS_DIR
        sess_mod.SESSIONS_DIR = Path(tmpdir)
        try:
            version = new_version_entry(
                stage="주제 탐색",
                model="gemma4:e4b",
                outputs={
                    "scout": "수연 출력 더미",
                    "critic": "준호 출력 더미",
                    "director": "지은 출력 더미",
                    "advisor": "",
                },
                note="smoke",
            )
            state = {
                "project_name": "smoke_test",
                "inputs": {"field": "식품영양", "stage": "주제 탐색"},
                "resources_manifest": [],
                "versions": [version],
                "agent_models": {"scout": "gemma4:e4b", "critic": "gemma4:e4b", "director": "gemma4:e4b"},
            }
            path = save_session("smoke_test", state, None)
            check("save_session returns non-empty path", bool(path))
            check("session file exists on disk", Path(path).exists())

            loaded = load_session(path)
            check("load_session preserves project_name",
                  loaded.get("project_name") == "smoke_test")
            check("load_session preserves versions list",
                  len(loaded.get("versions", [])) == 1)
            check("load_session preserves agent_models",
                  loaded.get("agent_models", {}).get("scout") == "gemma4:e4b")
        finally:
            sess_mod.SESSIONS_DIR = original_dir

    # ── 6. 산출물 레지스트리 ─────────────────────────────
    section("6. EXPORT_REGISTRY")
    from exporters import EXPORT_REGISTRY

    expected_exports = ["docx", "advisor_sheet", "search_queries", "irb_card", "bibtex_seed"]
    for key in expected_exports:
        check(f"EXPORT_REGISTRY has '{key}'", key in EXPORT_REGISTRY)
        check(f"EXPORT_LABELS has '{key}'", key in EXPORT_LABELS)

    # ── 결과 ────────────────────────────────────────────
    return _report()


def _report() -> int:
    print()
    print("=" * 60)
    print(f"  RESULT: {PASSED} passed, {FAILED} failed")
    print("=" * 60)
    if FAILURES:
        print("\nFailures:")
        for f in FAILURES:
            print(f"  ✗ {f}")
    return FAILED


if __name__ == "__main__":
    sys.exit(main())
