#!/usr/bin/env python3
"""나만의 연구팀 — Lite (경량 변형, 저-중사양 노트북용).

원본 streamlit_research_team 의 경량 변형:
- 지원 모델 사다리 (자동 선택): gemma4:e4b (16GB+) → qwen2.5:3b (8GB) → gemma3:1b (4GB)
  설치된 것 중 최상위 자동 적용. 사용자가 RAM 에 맞게 하나만 pull 하면 됨.
- 에이전트별 모델 지정 기본 ON (세 역할 모두 active 모델로 시작 — 프롬프트 스왑만으로 역할 차별화)
- 완주 후 여력이 있으면 한 역할을 더 큰 모델(또는 다른 계열)로 교체해 '티키타카' 확장

핵심 메시지: 같은 경량 모델 · 같은 하네스 · 역할별 프롬프트 3개 만으로도
3-에이전트 파이프라인이 돈다. 모델 크기보다 역할 설계가 먼저다.
"""

from __future__ import annotations

import datetime
import re

import ollama
import streamlit as st

from agents import STAGE_PROMPTS, ADVISOR_PROMPT, ROLE_LABELS, get_prompt
from templates import (
    RESEARCH_FIELDS, RESEARCH_STAGES, REQUIRED_ITEMS,
    CONTEXT_PLACEHOLDER, KEYWORDS_PLACEHOLDER, EXTRA_PLACEHOLDER,
    RESOURCES_HELP, PROJECT_NAME_PLACEHOLDER,
    DOCX_HEADER, DOCX_DISCLAIMER, EXPORT_LABELS,
    DEMO_PROJECT_NAME, DEMO_INPUTS, DEMO_RESOURCE_PATH, DEMO_RESOURCE_FILENAME,
)
from resources import (
    ingest_uploads, build_resource_block, resources_manifest,
    count_grounding, MAX_FILES,
)
from sessions import (
    save_session, load_session, list_sessions,
    new_version_entry, append_version, latest_outputs, two_latest,
)
from exporters import EXPORT_REGISTRY, create_docx


# ═════════════════════════════════════════════════════════════════════
# CSS (동일; 일부 추가)
# ═════════════════════════════════════════════════════════════════════

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;600;700&family=Noto+Sans+KR:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
    --ink: #1a1a1a;
    --ink-light: #4a4a4a;
    --ink-muted: #8a8a8a;
    --paper: #faf8f5;
    --paper-warm: #f5f0e8;
    --paper-cool: #f0efe9;
    --accent: #2c5f7c;
    --accent-deep: #1a3d52;
    --accent-light: #e8f0f5;
    --verify-green: #2d6a4f;
    --verify-green-bg: #edf5f0;
    --warn-amber: #8b6914;
    --warn-amber-bg: #fdf6e3;
    --fail-red: #9b2c2c;
    --fail-red-bg: #fef2f2;
    --rule: #d4cfc4;
    --rule-light: #e8e4db;
}

.stApp { background-color: var(--paper) !important; }

section[data-testid="stSidebar"] {
    background-color: var(--paper-cool) !important;
    border-right: 1px solid var(--rule) !important;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.85rem !important;
    color: var(--ink-light) !important;
}

h1, h2, h3 {
    font-family: 'Noto Serif KR', 'Georgia', serif !important;
    color: var(--ink) !important;
    letter-spacing: -0.01em !important;
}
h1 { font-weight: 700 !important; font-size: 1.8rem !important; border-bottom: 2px solid var(--ink) !important; padding-bottom: 0.4rem !important; margin-bottom: 0.3rem !important; }
h2 { font-weight: 600 !important; font-size: 1.25rem !important; color: var(--accent-deep) !important; }
h3 { font-weight: 600 !important; font-size: 1.05rem !important; }

p, li, label, .stMarkdown {
    font-family: 'Noto Sans KR', sans-serif !important;
    color: var(--ink-light) !important;
    line-height: 1.7 !important;
}
code, .stCode, pre { font-family: 'IBM Plex Mono', monospace !important; }

hr { border: none !important; border-top: 1px solid var(--rule) !important; margin: 1.5rem 0 !important; }

.stButton > button[kind="primary"] {
    background-color: var(--accent-deep) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.65rem 1.5rem !important;
}
.stButton > button[kind="primary"]:hover { background-color: var(--accent) !important; }
.stButton > button:not([kind="primary"]) {
    background-color: transparent !important;
    color: var(--ink-light) !important;
    border: 1px solid var(--rule) !important;
    border-radius: 2px !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.85rem !important;
}

.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background-color: #fff !important;
    border: 1px solid var(--rule) !important;
    border-radius: 2px !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    color: var(--ink) !important;
    font-size: 0.9rem !important;
}

.streamlit-expanderHeader {
    font-family: 'Noto Sans KR', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    color: var(--ink) !important;
    background-color: var(--paper-warm) !important;
    border: 1px solid var(--rule-light) !important;
    border-radius: 2px !important;
}

.stAlert > div {
    border-radius: 2px !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 0.85rem !important;
}

.stDownloadButton > button {
    background-color: var(--verify-green) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    font-weight: 500 !important;
}

.masthead { padding: 0.2rem 0 0.8rem 0; margin-bottom: 1.2rem; }
.masthead-sub { font-family: 'IBM Plex Mono', monospace; font-size: 0.72rem; color: var(--ink-muted); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.3rem; }
.masthead-title { font-family: 'Noto Serif KR', serif; font-size: 1.9rem; font-weight: 700; color: var(--ink); line-height: 1.2; letter-spacing: -0.02em; margin: 0; }
.masthead-desc { font-family: 'Noto Sans KR', sans-serif; font-size: 0.88rem; color: var(--ink-light); margin-top: 0.5rem; line-height: 1.6; }
.masthead-rule { border: none; border-top: 2px solid var(--ink); margin: 0.8rem 0 0 0; width: 100%; }

.pipeline-step {
    background: var(--paper-warm);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 1rem 1.2rem;
    height: 100%;
}
.pipeline-step-num { font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; color: var(--ink-muted); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.25rem; }
.pipeline-step-name { font-family: 'Noto Serif KR', serif; font-size: 1.05rem; font-weight: 600; color: var(--ink); margin-bottom: 0.2rem; }
.pipeline-step-role { font-family: 'Noto Sans KR', sans-serif; font-size: 0.75rem; color: var(--ink-muted); line-height: 1.4; }
.pipeline-step-status { font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; margin-top: 0.5rem; padding: 0.15rem 0.5rem; border-radius: 1px; display: inline-block; }
.status-waiting { color: var(--ink-muted); background: var(--paper); border: 1px solid var(--rule-light); }
.status-active { color: var(--accent-deep); background: var(--accent-light); border: 1px solid var(--accent); animation: pulse-subtle 2s infinite; }
.status-done { color: var(--verify-green); background: var(--verify-green-bg); border: 1px solid #b7d7c2; }
@keyframes pulse-subtle { 0%,100% { opacity: 1;} 50% { opacity: 0.7; } }

.disclaimer-box {
    background: var(--paper-warm);
    border-left: 3px solid var(--warn-amber);
    padding: 0.6rem 1rem;
    margin: 0.8rem 0 1.2rem 0;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.8rem;
    color: var(--ink-light);
    border-radius: 0 2px 2px 0;
}

.result-header {
    font-family: 'Noto Serif KR', serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--ink);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 0.3rem;
    margin: 1.5rem 0 0.8rem 0;
}

.section-label { font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; color: var(--ink-muted); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 0.5rem; }

.completion-banner {
    background: var(--verify-green-bg);
    border: 1px solid #b7d7c2;
    border-left: 4px solid var(--verify-green);
    padding: 1rem 1.2rem;
    border-radius: 0 2px 2px 0;
    margin: 1rem 0;
}
.completion-banner-title { font-family: 'Noto Serif KR', serif; font-size: 1rem; font-weight: 600; color: var(--verify-green); margin-bottom: 0.3rem; }
.completion-banner-desc { font-family: 'Noto Sans KR', sans-serif; font-size: 0.82rem; color: var(--ink-light); }

.harness-note {
    background: var(--paper-cool);
    border: 1px solid var(--rule);
    padding: 0.8rem 1rem;
    margin: 1rem 0;
    border-radius: 2px;
}
.harness-note-title { font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; color: var(--accent); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.3rem; }
.harness-note-text { font-family: 'Noto Sans KR', sans-serif; font-size: 0.82rem; color: var(--ink-light); line-height: 1.6; }

.sidebar-brand { font-family: 'Noto Serif KR', serif; font-size: 1rem; font-weight: 600; color: var(--ink); margin-bottom: 0.1rem; }
.sidebar-brand-sub { font-family: 'IBM Plex Mono', monospace; font-size: 0.6rem; color: var(--ink-muted); letter-spacing: 0.1em; text-transform: uppercase; }

.sidebar-status {
    display: flex; align-items: center; gap: 0.4rem;
    padding: 0.4rem 0.6rem;
    border-radius: 2px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    margin: 0.5rem 0;
}
.sidebar-status-ok { background: var(--verify-green-bg); color: var(--verify-green); border: 1px solid #b7d7c2; }
.sidebar-status-err { background: var(--fail-red-bg); color: var(--fail-red); border: 1px solid #f5c6c6; }

.footer-note {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.6rem;
    color: var(--ink-muted);
    text-align: center;
    margin-top: 2rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--rule-light);
    letter-spacing: 0.05em;
}

/* v2 추가 */
.ledger-card {
    background: var(--paper-warm);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 0.6rem 0.9rem;
    margin: 0.5rem 0;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--ink-light);
}
.ledger-grounded { color: var(--verify-green); font-weight: 500; }
.ledger-speculated { color: var(--warn-amber); font-weight: 500; }

.resource-chip {
    display: inline-block;
    background: var(--accent-light);
    color: var(--accent-deep);
    border: 1px solid var(--accent);
    border-radius: 999px;
    padding: 0.1rem 0.7rem;
    margin: 0.1rem 0.2rem 0.1rem 0;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
}

/* ───────── 반응형 / 오버플로우 방지 ───────── */

/* 긴 문자열이 있는 어떤 요소도 창 밖으로 밀어내지 못하게 */
.stMarkdown, .stMarkdown *, div[data-testid="stMarkdownContainer"] {
    max-width: 100% !important;
    overflow-wrap: break-word !important;
    word-break: break-word !important;
}

/* 코드 블록: 가로 스크롤로 처리 (넘친다고 레이아웃 깨지지 않게) */
.stCode, pre, code {
    max-width: 100% !important;
    overflow-x: auto !important;
    white-space: pre !important;
}

/* 마크다운 테이블이 expander 안에서 오버플로우 나는 경우 */
div[data-testid="stExpander"] table,
.stMarkdown table {
    display: block !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    border-collapse: collapse !important;
}

/* 파이프라인 카드 — 좁은 화면에서 최소 높이만 확보하고 자유롭게 wrap */
.pipeline-step {
    min-height: 0 !important;
    word-break: keep-all !important;
}

/* 귀퉁이 배너들 (Lite 안내·웹검색 안내·배지) 모바일 조정 */
@media (max-width: 820px) {
    h1 { font-size: 1.45rem !important; }
    h2 { font-size: 1.1rem !important; }
    h3 { font-size: 1rem !important; }
    .masthead-title { font-size: 1.4rem !important; }
    .pipeline-step {
        padding: 0.75rem 0.85rem !important;
    }
    .pipeline-step-name { font-size: 0.95rem !important; }
    .pipeline-step-role { font-size: 0.7rem !important; }
    /* 본문 배너·카드 내부 여백 축소 */
    div[style*="padding:14px 18px"],
    div[style*="padding:10px 14px"],
    div[style*="padding:12px 16px"] {
        padding: 10px 12px !important;
        font-size: 0.78rem !important;
    }
    /* Streamlit 이 좁은 뷰에서 columns 를 자동 stack 하지만 gap 이 커서 */
    div[data-testid="column"] { padding: 0.25rem 0 !important; }
}

@media (max-width: 560px) {
    /* 사이드바: 완전히 넓은 오버레이로 */
    section[data-testid="stSidebar"] > div { padding: 0.5rem !important; }
    /* 메인 콘텐츠 좌우 여백 축소 */
    section[data-testid="stMain"] .block-container,
    .main .block-container {
        padding-left: 0.6rem !important;
        padding-right: 0.6rem !important;
    }
    /* 배너 inline 스타일 오버라이드 — 제목 크기 더 줄임 */
    div[style*="font-size:0.95rem;font-weight:600"] { font-size: 0.85rem !important; }
}

/* 긴 URL · 모델명 등이 박스를 밀어내지 않게 */
code, .stCode span { overflow-wrap: anywhere !important; }

/* 다운로드·실행 버튼이 좁은 화면에서 잘리지 않게 */
.stButton > button, .stDownloadButton > button {
    white-space: normal !important;
    min-height: 2.4rem !important;
    line-height: 1.3 !important;
}
</style>
"""


# ═════════════════════════════════════════════════════════════════════
# Ollama 연결 & 모델 목록 — 한 번의 호출로 병합
# ═════════════════════════════════════════════════════════════════════

def fetch_ollama_state():
    """Return (connected, models_list). models_list is [(name, size_gb), ...].
    Dedupes tags pointing to the same digest (e.g. gemma4:26b is an alias for
    gemma4:26b-a4b-it-q4_K_M — we show the shorter tag only)."""
    try:
        result = ollama.list()
    except Exception:
        return False, []

    models_raw = []
    if hasattr(result, "models"):
        models_raw = [
            (m.model, getattr(m, "size", 0), getattr(m, "digest", "") or "")
            for m in result.models
        ]
    elif isinstance(result, dict) and "models" in result:
        models_raw = [
            (m["name"], m.get("size", 0), m.get("digest", ""))
            for m in result["models"]
        ]

    # Dedupe by digest — keep the shortest tag name per digest (most canonical)
    by_digest: dict = {}
    no_digest: list = []
    for name, size, digest in models_raw:
        if "embed" in name.lower() or "nomic" in name.lower():
            continue
        if not digest:
            no_digest.append((name, size))
            continue
        current = by_digest.get(digest)
        if current is None or len(name) < len(current[0]):
            by_digest[digest] = (name, size)

    models = [(name, (size / (1024 ** 3)) if size else 0)
              for name, size in list(by_digest.values()) + no_digest]
    models.sort(key=lambda x: x[1], reverse=True)
    return True, models


def format_model_size(gb: float) -> str:
    if gb < 1:
        return f"{gb * 1024:.0f}MB"
    return f"{gb:.1f}GB"


# ═════════════════════════════════════════════════════════════════════
# Ollama 호출 — 스트리밍
# ═════════════════════════════════════════════════════════════════════

THINKING_TIMEOUT_HINT = (
    "⚠️ 모델이 최종 응답을 생성하기 전에 예산이 소진되었습니다. "
    "사고 모드를 끄거나(⚡ 빠른 모드) num_predict 를 더 크게 설정하세요."
)


def run_streamed(stream_iter, content_placeholder, thinking_placeholder=None):
    """Consume a stream_ollama iterator, routing chunks to placeholders.
    Returns the accumulated content text (thinking is shown separately but not stored
    in the final artifact — only final 'content' is persisted)."""
    content = ""
    thinking = ""
    for chunk in stream_iter:
        if chunk["kind"] == "thinking" and thinking_placeholder is not None:
            thinking += chunk["text"]
            # Truncate thinking display to last ~800 chars to keep it bounded
            tail = thinking[-800:]
            thinking_placeholder.markdown(
                f"<div style='background:#f0efe9;border-left:3px solid #8a8a8a;"
                f"padding:0.5rem 0.8rem;margin:0.3rem 0;font-family:IBM Plex Mono,monospace;"
                f"font-size:0.72rem;color:#4a4a4a;white-space:pre-wrap;max-height:180px;"
                f"overflow-y:auto;'>🧠 사고 중…<br>{tail}</div>",
                unsafe_allow_html=True,
            )
        elif chunk["kind"] == "content":
            content += chunk["text"]
            content_placeholder.markdown(content + " ●")
    content_placeholder.markdown(content)
    return content


def stream_ollama(model: str, system_prompt: str, user_prompt: str,
                  think: bool = False, num_predict: int = 4096,
                  keep_alive: int = 0):
    """Stream chat chunks. Yields dicts: {'kind': 'content'|'thinking', 'text': str}.
    When think=False, only 'content' is yielded. When think=True, 'thinking' chunks
    stream first (reasoning), then 'content' chunks (final answer).
    keep_alive=0 unloads the model after the call — lets downstream agents load fresh
    without VRAM thrashing (sequential orchestration hygiene)."""
    # Thinking needs a lot more headroom — verified empirically: 3500 tokens wasn't
    # enough for a 1-sentence prompt, 10K thinking chars were generated then cut off.
    # Bump to 12K when thinking is on so final content has room to emerge.
    effective_budget = max(num_predict, 12288) if think else num_predict
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        think=think,
        options={"temperature": 0.3, "top_p": 0.9, "num_predict": effective_budget},
        keep_alive=keep_alive,
        stream=True,
    )
    total_content = 0
    for chunk in response:
        msg = chunk.message if hasattr(chunk, "message") else chunk.get("message")
        if msg is None:
            continue
        content = (msg.content if hasattr(msg, "content") else msg.get("content")) or ""
        thinking = (msg.thinking if hasattr(msg, "thinking") else msg.get("thinking")) or ""
        if thinking:
            yield {"kind": "thinking", "text": thinking}
        if content:
            total_content += len(content)
            yield {"kind": "content", "text": content}
    if total_content == 0:
        yield {"kind": "content", "text": "\n\n" + THINKING_TIMEOUT_HINT}


# ═════════════════════════════════════════════════════════════════════
# 파이프라인 시각화
# ═════════════════════════════════════════════════════════════════════

PIPELINE_ROLES = [
    ("Step I",   "수연", "탐색",   "scout",    "주제/문헌/RQ 후보 도출"),
    ("Step II",  "준호", "검증",   "critic",   "논리·근거·반증가능성 공격"),
    ("Step III", "지은", "총괄",   "director", "종합·확정·체크리스트"),
]


def render_pipeline(step: int, advisor_mode: bool) -> None:
    """Render 3 (or 4) pipeline steps. step: 1=scout running .. 5=done."""
    cols = st.columns(4 if advisor_mode else 3)

    items = list(PIPELINE_ROLES)
    if advisor_mode:
        items.append(("Step IV", "한민수", "지도교수", "advisor", "메타 질문 + 회의 1p"))

    for i, (label, name, role_label, role_key, desc) in enumerate(items):
        s = i + 1
        if step > s:
            status_class, status_text = "status-done", "COMPLETE"
        elif step == s:
            status_class, status_text = "status-active", "PROCESSING..."
        else:
            status_class, status_text = "status-waiting", "STANDBY"
        with cols[i]:
            st.markdown(
                f'<div class="pipeline-step">'
                f'<div class="pipeline-step-num">{label}</div>'
                f'<div class="pipeline-step-name">{name} ({role_label})</div>'
                f'<div class="pipeline-step-role">{desc}</div>'
                f'<div class="pipeline-step-status {status_class}">{status_text}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )


# ═════════════════════════════════════════════════════════════════════
# 근거 원장 (grounding ledger) 렌더
# ═════════════════════════════════════════════════════════════════════

def render_ledger(text: str) -> None:
    stats = count_grounding(text)
    if stats["grounded_total"] == 0 and stats["speculated_total"] == 0:
        return
    parts = []
    parts.append(f'<span class="ledger-grounded">근거 {stats["grounded_total"]}건</span>')
    parts.append(f'<span class="ledger-speculated">추측 {stats["speculated_total"]}건</span>')
    if stats["by_file"]:
        files_part = " · ".join(
            f"{f}×{n}" for f, n in sorted(stats["by_file"].items(), key=lambda x: -x[1])[:5]
        )
        parts.append(f'<span style="color:var(--ink-muted)">{files_part}</span>')
    st.markdown(
        f'<div class="ledger-card">근거 원장: {" · ".join(parts)}</div>',
        unsafe_allow_html=True,
    )


# ═════════════════════════════════════════════════════════════════════
# 사용자 프롬프트 조립
# ═════════════════════════════════════════════════════════════════════

def build_user_payload(inputs: dict, resources: list, resource_override: list = None) -> str:
    rs = resource_override if resource_override is not None else resources
    resource_block = build_resource_block(rs)
    return (
        resource_block
        + "=== 연구 맥락 ===\n"
        + f"연구 분야: {inputs['field']}\n"
        + f"연구 단계: {inputs['stage']}\n"
        + f"키워드: {inputs['keywords']}\n"
        + f"상세 맥락: {inputs['context']}\n"
        + "=== 맥락 끝 ===\n\n"
        + f"=== 추가 요청 ===\n{inputs.get('extra') or '없음'}\n=== 요청 끝 ===\n\n"
        + "★ 위 맥락의 모든 정보를 결과물에 직접 반영하세요. "
        "업로드 자료에서 근거를 찾을 수 있으면 [근거: 파일명] 태그를, "
        "없으면 [추측] 태그를 붙이세요."
    )


def build_critic_payload(inputs, resources, scout_output) -> str:
    base = build_user_payload(inputs, resources)
    return (
        f"=== 수연의 탐색 결과 ===\n{scout_output}\n=== 결과 끝 ===\n\n"
        + base
        + "\n\n★ 최우선: 수연의 결과에서 근거 부실·논리 비약·반증불가 지점을 공격하세요. "
        "기존 주장에 동의하지 마세요."
    )


def build_director_payload(inputs, resources, scout_output, critic_output) -> str:
    base = build_user_payload(inputs, resources)
    return (
        f"=== 수연의 탐색 결과 ===\n{scout_output}\n=== 탐색 끝 ===\n\n"
        f"=== 준호의 검증 결과 ===\n{critic_output}\n=== 검증 끝 ===\n\n"
        + base
        + "\n\n★ 최종 검증: 준호의 ❌/⚠️ 항목을 모두 반영하고, "
        "업로드 자료가 있으면 근거 무결성을 재확인하세요."
    )


def build_advisor_payload(inputs, director_output) -> str:
    return (
        f"=== 학생이 준비한 연구 설계 ===\n{director_output}\n=== 설계 끝 ===\n\n"
        f"=== 학생 배경 ===\n분야: {inputs['field']} / 단계: {inputs['stage']}\n"
        f"키워드: {inputs['keywords']}\n=== 배경 끝 ===\n\n"
        "★ 지도교수로서 10개 메타 질문 + 회의 준비 1p 를 생성하세요."
    )


# ═════════════════════════════════════════════════════════════════════
# 세션 상태 초기화/리셋
# ═════════════════════════════════════════════════════════════════════

DEFAULT_STATE = {
    "step": 0,                      # 0=idle, 1..4=running scout/critic/director/advisor, 5=done
    "scout_output": "",
    "critic_output": "",
    "director_output": "",
    "advisor_output": "",
    "resources": [],                # [{filename, text}]
    "inputs_snapshot": {},          # frozen at pipeline start
    "advisor_mode": False,
    "think_mode": False,            # 🧠 thinking mode — slower but deeper reasoning
    "session_path": None,           # existing session JSON path, if resumed
    "project_name": "",
    "session_state_dict": None,     # the full saved-state dict
    "refine_target": "",            # role key for refinement ('scout'/'critic'/'director'/'advisor')
    "refine_feedback": "",
    "refine_running": False,
    "refine_version_marker": False, # True when latest version was a refinement (for v1↔v2 tabs)
    "model": "",
    # A/B 대조 실행 — 동일 파이프라인을 자료 없이 한 번 더 돌려 차이를 시각화
    "ab_step": 0,                   # 0=idle, 1=scout, 2=critic, 3=director, 4=done
    "ab_scout_output": "",
    "ab_critic_output": "",
    "ab_director_output": "",
    # Lite 기본값 — 에이전트별 모델 지정 항상 ON,
    # 세 역할 모두 e4b 로 시작. (사용자가 사이드바에서 한 역할만 교체하며 '티키타카' 실험)
    "per_agent_mode": True,
    "agent_models": {
        "scout":    "gemma4:e4b",
        "critic":   "gemma4:e4b",
        "director": "gemma4:e4b",
        "advisor":  "gemma4:e4b",
    },
}

# Lite 지원 모델 사다리 — 품질 > 필요 RAM 순.
# 16GB 이상 사용자는 gemma4:e4b, 8GB 사용자는 qwen2.5:3b, 구형/저가 머신은 gemma3:1b.
# 설치된 것 중 최상위 모델을 자동 선택. 기본 경험은 단일 모델 × 3 역할.
LITE_ALLOWED_MODELS = [
    # (model_tag,       disk_size,  recommended_ram,  note_ko)
    ("gemma4:e4b",      "9.6GB",    "16GB+",   "권장 · 한국어·추론 모두 강함"),
    ("qwen2.5:3b",      "2GB",      "8GB+",    "8GB 대안 · 한국어 OK"),
    ("gemma3:1b",       "0.8GB",    "4GB+",    "최소 사양 · 짧은 응답 위주"),
]
# Default (when nothing installed) — shown in the install prompt
LITE_PREFERRED_MODEL = LITE_ALLOWED_MODELS[0][0]


def lite_model_pick(installed):
    """Return the first allowed model that is installed, along with metadata.

    Returns (tag, disk_size, ram_hint, note_ko) or None if none installed.
    Matches both 'gemma4:e4b' and 'gemma4:e4b-...' suffixed variants.
    """
    if not installed:
        return None
    names = [m[0] for m in installed]
    for tag, size, ram, note in LITE_ALLOWED_MODELS:
        for n in names:
            if n == tag or n.startswith(tag + "-"):
                return (n, size, ram, note)
    return None


# Back-compat shim for older references / smoke test
LITE_REQUIRED_MODEL = LITE_PREFERRED_MODEL

def lite_model_available(installed) -> bool:
    """Return True iff any of the allowed Lite models is installed."""
    return lite_model_pick(installed) is not None


ROLE_ORDER = ["scout", "critic", "director", "advisor"]


def pick_model(role: str, fallback: str) -> str:
    """Return the model to use for a given role. If per_agent_mode is off,
    returns the shared fallback (the sidebar's primary model pick)."""
    if not st.session_state.get("per_agent_mode"):
        return fallback
    return st.session_state.agent_models.get(role, fallback)


def init_state():
    for k, v in DEFAULT_STATE.items():
        if k not in st.session_state:
            st.session_state[k] = v if not isinstance(v, (list, dict)) else (list(v) if isinstance(v, list) else dict(v))


def reset_pipeline_outputs():
    st.session_state.step = 0
    st.session_state.scout_output = ""
    st.session_state.critic_output = ""
    st.session_state.director_output = ""
    st.session_state.advisor_output = ""


def reset_session():
    for k, v in DEFAULT_STATE.items():
        st.session_state[k] = v if not isinstance(v, (list, dict)) else (list(v) if isinstance(v, list) else dict(v))


def load_demo_scenario():
    """Populate text fields with the 고령자 식품불안정 scenario.

    Lite 방침: **가상/생성된 선행연구 자료는 로드하지 않습니다.**
    이유: LLM 환각을 우회하기 위해 도입한 근거 태깅이, 데모를 위해 강사가 지어낸
    가상 논문 위에서 '[근거: kim_2023.pdf]' 같은 태그를 붙이면 그 자체가
    환각을 시연하는 모양이 됩니다. 학술 워크숍에서 특히 부적절.

    따라서 이 버튼은 입력 필드만 채우고, 업로드 PDF 는 사용자가 본인 논문을
    직접 올리도록 유도합니다. '자료 없음' 상태로 실행하면 수연/준호/지은이
    전부 '[추측]' 태깅을 달고 나오는데, 그것 자체가 '왜 실제 자료가 필요한가'
    라는 교훈의 일부입니다.
    """
    reset_session()
    st.session_state.project_name = DEMO_PROJECT_NAME
    st.session_state.inputs_snapshot = dict(DEMO_INPUTS)
    st.session_state.resources = []  # 가상 자료 로드하지 않음 (사용자 업로드 유도)


# ═════════════════════════════════════════════════════════════════════
# 세션 저장/복원
# ═════════════════════════════════════════════════════════════════════

def persist_current_version(note: str = "") -> None:
    """Snapshot current pipeline outputs as a new version entry in the state dict, save to disk."""
    state = st.session_state.session_state_dict or {
        "project_name": st.session_state.project_name or "untitled",
        "inputs": dict(st.session_state.inputs_snapshot),
        "resources_manifest": resources_manifest(st.session_state.resources),
        "versions": [],
    }
    state["inputs"] = dict(st.session_state.inputs_snapshot)
    state["resources_manifest"] = resources_manifest(st.session_state.resources)
    # Record per-agent model split if advanced mode was in use
    if st.session_state.per_agent_mode:
        state["agent_models"] = dict(st.session_state.agent_models)
    else:
        state.pop("agent_models", None)

    model_descriptor = st.session_state.model or ""
    if st.session_state.per_agent_mode and st.session_state.agent_models:
        model_descriptor = "mixed: " + " · ".join(
            f"{r}={m}" for r, m in st.session_state.agent_models.items()
        )
    entry = new_version_entry(
        stage=st.session_state.inputs_snapshot.get("stage", ""),
        model=model_descriptor,
        outputs={
            "scout": st.session_state.scout_output,
            "critic": st.session_state.critic_output,
            "director": st.session_state.director_output,
            "advisor": st.session_state.advisor_output,
        },
        note=note,
    )
    append_version(state, entry)

    path = save_session(state["project_name"], state, existing_path=st.session_state.session_path)
    st.session_state.session_path = path
    st.session_state.session_state_dict = state


def hydrate_from_session(path: str) -> None:
    data = load_session(path)
    reset_session()
    st.session_state.session_path = path
    st.session_state.session_state_dict = data
    st.session_state.project_name = data.get("project_name", "")
    st.session_state.inputs_snapshot = data.get("inputs", {})
    st.session_state.advisor_mode = bool(data.get("inputs", {}).get("advisor_mode", False))
    if "agent_models" in data:
        st.session_state.agent_models = dict(data["agent_models"])
        st.session_state.per_agent_mode = True
    latest = latest_outputs(data)
    st.session_state.scout_output = latest.get("scout", "")
    st.session_state.critic_output = latest.get("critic", "")
    st.session_state.director_output = latest.get("director", "")
    st.session_state.advisor_output = latest.get("advisor", "")
    st.session_state.step = 5 if st.session_state.director_output else 0


# ═════════════════════════════════════════════════════════════════════
# 최종 연구 설계 텍스트 추출 (지은 출력 중 '📋 최종 연구 설계' 섹션)
# ═════════════════════════════════════════════════════════════════════

def extract_final_doc(director_output: str) -> str:
    """Return the body under the 📋 heading (최종 연구 설계 / 확정 RQ / 선행연구 종합 메모).
    Falls back to full output if the expected section bars aren't found."""
    if not director_output:
        return ""
    # Section pattern: 📋 heading → ━ separator → body → next ━ (or end)
    specific = r"📋[^\n]*\n━+\s*\n(.*?)(?=\n━+|\Z)"
    m = re.search(specific, director_output, re.DOTALL)
    if m and m.group(1).strip():
        return m.group(1).strip()
    # Fallback: any 📋 heading and everything after it
    loose = r"📋[^\n]*\n(.*?)(?=\n━+|\Z)"
    m = re.search(loose, director_output, re.DOTALL)
    if m and m.group(1).strip():
        return m.group(1).strip()
    return director_output.strip()


# ═════════════════════════════════════════════════════════════════════
# 메인 앱
# ═════════════════════════════════════════════════════════════════════

def main():
    st.set_page_config(
        page_title="연구팀 Lite — single model × 3 roles",
        page_icon=None,
        layout="wide",
    )
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    init_state()

    # ── Ollama 연결 + 모델 목록 (단일 호출) ──
    is_connected, installed = fetch_ollama_state()

    # ─────────────────────────────────────────────
    # 사이드바
    # ─────────────────────────────────────────────
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">연구팀 · Lite</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="sidebar-brand-sub">single model × 3 roles · 4-16GB friendly</div>',
            unsafe_allow_html=True,
        )
        st.markdown("---")

        # Ollama 상태
        if is_connected:
            st.markdown('<div class="sidebar-status sidebar-status-ok">Ollama 연결됨</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="sidebar-status sidebar-status-err">Ollama 연결 실패</div>', unsafe_allow_html=True)
            st.code("ollama serve", language="bash")

        # Lite 전용 모델 상태 카드 — 사다리 자동 선택
        st.markdown('<div class="section-label">Lite 모델</div>', unsafe_allow_html=True)
        pick = lite_model_pick(installed)
        has_lite = pick is not None

        if has_lite:
            active_tag, active_size, active_ram, active_note = pick
            # Is this the top (권장) choice, or a lower-rung fallback?
            is_preferred = active_tag == LITE_PREFERRED_MODEL or active_tag.startswith(LITE_PREFERRED_MODEL + "-")
            selected_model = active_tag
            # 녹색 "정상" 배지 — 사다리 내 어느 위치인지 명시
            tier_note = "" if is_preferred else "  · fallback"
            st.markdown(
                f'<div style="background:#e8f5e9;border:1px solid #a5d6a7;'
                f'border-radius:6px;padding:10px 12px;margin:4px 0 8px;'
                f'font-family:IBM Plex Mono,monospace;font-size:0.75rem;line-height:1.6;">'
                f'<span style="color:#2e7d32;font-weight:600;">✓ {active_tag}</span>'
                f'<span style="color:#5a7a5d;font-size:0.68rem;">'
                f' &nbsp;{active_size} · {active_ram}{tier_note}</span>'
                f'<br><span style="color:#5a7a5d;font-size:0.68rem;">'
                f'{active_note} · 세 역할(수연·준호·지은) 모두 이 모델로 실행'
                f'</span></div>',
                unsafe_allow_html=True,
            )
            # If user ALSO has a higher-rung model installed, ignore (we picked the best)
            # If user has lower-rung fallbacks also installed, show compact info
            other_allowed = [
                m[0] for m in installed
                if any(m[0] == t or m[0].startswith(t + "-") for t, _, _, _ in LITE_ALLOWED_MODELS)
                and m[0] != active_tag and not m[0].startswith(active_tag + "-")
            ]
            if other_allowed:
                st.markdown(
                    f'<div style="font-family:IBM Plex Mono,monospace;font-size:0.6rem;'
                    f'color:#8a8a8a;margin-top:-4px;">'
                    f'대안 설치됨: {", ".join(other_allowed)} (역할별 드롭다운에서 교체 가능)'
                    f'</div>',
                    unsafe_allow_html=True,
                )
        else:
            selected_model = LITE_PREFERRED_MODEL
            # 주황 "미설치" 경고 + 사다리 전체 노출
            st.markdown(
                '<div style="background:#fff4e5;border:1px solid #ffb74d;'
                'border-radius:6px;padding:10px 12px;margin:4px 0 8px;'
                'font-family:Noto Sans KR,sans-serif;font-size:0.78rem;line-height:1.6;">'
                '<b style="color:#e65100;">⚠ Lite 지원 모델 미설치</b><br>'
                '<span style="font-size:0.72rem;color:#5a4a3a;">'
                '노트북 RAM 에 맞는 모델 하나를 pull 후 페이지 새로고침:'
                '</span></div>',
                unsafe_allow_html=True,
            )
            ladder_lines = []
            for tag, size, ram, note in LITE_ALLOWED_MODELS:
                ladder_lines.append(f"# {ram:<6} ({size}) — {note}")
                ladder_lines.append(f"ollama pull {tag}")
                ladder_lines.append("")
            st.code("\n".join(ladder_lines).rstrip(), language="bash")
            if installed:
                other_names = ", ".join(m[0] for m in installed[:4])
                st.markdown(
                    f'<div style="font-family:IBM Plex Mono,monospace;font-size:0.62rem;'
                    f'color:#8a8a8a;margin-top:0.3rem;">설치됨 (Lite 지원 외): {other_names}</div>',
                    unsafe_allow_html=True,
                )

        st.session_state.model = selected_model

        # 역할별 모델 — Lite 는 항상 ON, 체크박스 대신 섹션으로
        st.markdown("---")
        st.markdown('<div class="section-label">역할별 모델 (티키타카)</div>',
                    unsafe_allow_html=True)
        st.session_state.per_agent_mode = True  # Lite 는 항상 ON

        if has_lite and installed:
            model_opts = [m[0] for m in installed]
            # 처음 렌더 전에 세션 상태에 key 를 심어둔다
            # (st.selectbox 의 `index=` 는 세션 key 가 이미 있으면 무시되기 때문)
            # 기본값 = 사다리에서 선택된 active model (사용자 RAM 에 맞는 것)
            for role in ROLE_ORDER:
                widget_key = f"agent_model_{role}"
                if widget_key not in st.session_state:
                    st.session_state[widget_key] = selected_model
                # 설치 목록에서 사라진 모델을 가리키고 있으면 리셋
                if st.session_state[widget_key] not in model_opts:
                    st.session_state[widget_key] = selected_model

            st.markdown(
                f'<div style="font-family:Noto Sans KR,sans-serif;font-size:0.72rem;'
                f'color:#5a5a5a;margin:0 0 6px;line-height:1.5;">'
                f'기본: 세 역할 모두 <code style="font-size:0.82em;">{selected_model}</code> · '
                f'한 역할만 다른 모델로 바꿔 비판/생성 차이 비교'
                '</div>',
                unsafe_allow_html=True,
            )

            for role in ROLE_ORDER:
                if role == "advisor" and not st.session_state.advisor_mode:
                    continue
                label_ko = ROLE_LABELS[role].split(" ")[0]
                emoji = {"scout": "🔍", "critic": "🔬", "director": "📋", "advisor": "🎓"}.get(role, "")
                picked = st.selectbox(
                    f"{emoji} {label_ko}",
                    model_opts,
                    key=f"agent_model_{role}",
                )
                st.session_state.agent_models[role] = picked

            # 시각적 안내: 몇 개가 Lite 기본(= 현재 선택된 active model)에서 벗어났는지
            swapped = [
                r for r in ["scout", "critic", "director"]
                if st.session_state.agent_models.get(r) != selected_model
            ]
            if swapped:
                st.markdown(
                    f'<div style="background:#fff8e1;border-left:3px solid #ffc107;'
                    f'padding:6px 10px;margin-top:8px;font-size:0.7rem;'
                    f'font-family:Noto Sans KR,sans-serif;color:#6d5b1d;">'
                    f'🔀 <b>티키타카 모드</b> · {len(swapped)}개 역할이 다른 모델로 교체됨'
                    f'</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div style="font-family:Noto Sans KR,sans-serif;font-size:0.75rem;'
                'color:#8a8a8a;padding:8px 4px;">'
                '모델 미설치 상태. 위 명령어 실행 후 새로고침.'
                '</div>',
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # 세션 선택
        st.markdown('<div class="section-label">세션</div>', unsafe_allow_html=True)
        sessions = list_sessions()
        session_choices = ["새 프로젝트"] + [
            f"▸ {s['project_name']} (v{s['version_count']}) — {s['updated_at'][:16]}"
            for s in sessions
        ]
        session_idx = st.selectbox(
            "세션 선택",
            list(range(len(session_choices))),
            format_func=lambda i: session_choices[i],
            label_visibility="collapsed",
            key="session_select",
        )
        if session_idx > 0:
            candidate_path = sessions[session_idx - 1]["path"]
            if candidate_path != st.session_state.session_path:
                if st.button("이 세션 재개", key="resume_btn", use_container_width=True):
                    hydrate_from_session(candidate_path)
                    st.rerun()
        if st.button("새 세션 시작", key="new_btn", use_container_width=True):
            reset_session()
            st.rerun()

        st.markdown("---")

        # 지도교수 모드 토글
        advisor_on = st.checkbox(
            "🎓 지도교수 모드 (4번째 에이전트)",
            value=st.session_state.advisor_mode,
            help="파이프라인 말미에 '한민수 지도교수'가 10개 메타 질문 + 회의 1p를 생성합니다.",
        )
        st.session_state.advisor_mode = advisor_on

        # 사고 모드 토글 — qwen3/deepseek-r1/gemma4 의 thinking 기능 활성화
        think_on = st.checkbox(
            "🧠 사고 모드 (thinking)",
            value=st.session_state.think_mode,
            help="모델의 내부 추론 과정(<think>)을 활성화. 깊은 반증·방법론 검토에 유리하지만 "
                 "속도가 2-5배 느려지고 예산이 부족하면 응답이 비어 나올 수 있습니다. "
                 "qwen3·deepseek-r1 같은 사고 계열 모델에서 특히 효과적.",
        )
        st.session_state.think_mode = think_on

        st.markdown("---")

        # 단계별 필수 항목 가이드
        st.markdown('<div class="section-label">단계별 필수 항목</div>', unsafe_allow_html=True)
        guide_stage = st.selectbox(
            "참고할 단계", RESEARCH_STAGES, key="guide_stage", label_visibility="collapsed"
        )
        if guide_stage in REQUIRED_ITEMS:
            for item in REQUIRED_ITEMS[guide_stage]:
                st.markdown(f"- {item}")

        st.markdown(
            '<div class="footer-note">'
            "Harness Engineering Demo<br>"
            "같은 하네스, 다른 프롬프트<br>"
            '<a href="https://www.youtube.com/watch?v=t7JjQTEnKOo" '
            'style="color:#8a8a8a">원본: 나만의 법무팀</a>'
            "</div>",
            unsafe_allow_html=True,
        )

    # ─────────────────────────────────────────────
    # 메인 영역 — Masthead
    # ─────────────────────────────────────────────
    st.markdown(
        """
        <div class="masthead">
            <div class="masthead-sub">Yonsei University · College of Human Ecology · v2</div>
            <div class="masthead-title">나만의 연구팀</div>
            <div class="masthead-desc">
                3-에이전트 하네스 × 3개 연구 단계 = 상황별 최적화된 파이프라인. 로컬 LLM 기반, 자료 외부 전송 없음.<br>
                대학원생의 반복 연구 작업을 위한 로컬 컴패니언.
            </div>
            <hr class="masthead-rule">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="disclaimer-box">'
        "본 도구의 출력은 AI가 생성한 초안이며, 학술적 효력을 보장하지 않습니다. "
        "연구 진행 전 반드시 지도교수의 검토를 받으세요. "
        "업로드 파일은 로컬 메모리에만 보관되며 외부로 전송되지 않습니다."
        "</div>",
        unsafe_allow_html=True,
    )

    # Lite 모드 안내 배너 (현재 active 모델을 반영)
    st.markdown(
        f'<div style="background:linear-gradient(135deg,#eef5ff 0%,#f5f0ff 100%);'
        f'border:1px solid #c5d9f1;border-radius:8px;'
        f'padding:14px 18px;margin:8px 0 14px;'
        f'font-family:Noto Sans KR,sans-serif;font-size:0.84rem;line-height:1.7;'
        f'color:#2c3e50;">'
        f'<div style="font-size:0.95rem;font-weight:600;margin-bottom:6px;">'
        f'🪶 Lite 모드'
        f'</div>'
        f'<div>'
        f'<b>1단계 · 기본 시연</b>: '
        f'<code style="background:#fff;padding:1px 6px;border-radius:3px;'
        f'font-size:0.82em;">{selected_model}</code> 단일 모델 × 세 역할 '
        f'(🔍 수연 · 🔬 준호 · 📋 지은) — 프롬프트 스왑만으로 역할 차별화.'
        f'</div>'
        f'<div style="margin-top:4px;">'
        f'<b>2단계 · 티키타카 (선택)</b>: '
        f'사이드바에서 한 역할만 다른 모델로 교체해 모델 간 차이 비교.'
        f'</div>'
        f'<div style="margin-top:6px;font-size:0.74rem;color:#6c7b8a;">'
        f'사다리 자동 선택: gemma4:e4b (16GB+) → qwen2.5:3b (8GB) → gemma3:1b (4GB) · 완전 오프라인'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ─────────────────────────────────────────────
    # 프로젝트명 + 빠른 시작
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">프로젝트</div>', unsafe_allow_html=True)
    pn_col, demo_col = st.columns([4, 1])
    with pn_col:
        project_name = st.text_input(
            "프로젝트 이름",
            value=st.session_state.project_name,
            placeholder=PROJECT_NAME_PLACEHOLDER,
            label_visibility="collapsed",
        )
    with demo_col:
        if st.button("🎯 예시로 시작", help="고령자 식품불안정 시나리오 + 샘플 논문을 자동 로드합니다.", use_container_width=True):
            load_demo_scenario()
            st.rerun()
    st.session_state.project_name = project_name

    # ─────────────────────────────────────────────
    # 오프라인 도구 경계 · 워크플로우 안내
    # ─────────────────────────────────────────────
    st.markdown(
        '<div style="background:#f6f7f9;border-left:4px solid #5a6c8a;'
        'border-radius:4px;padding:12px 16px;margin:10px 0;'
        'font-family:Noto Sans KR,sans-serif;font-size:0.82rem;line-height:1.7;'
        'color:#3a4556;">'
        '<b style="color:#2c3e50;">이 도구는 웹검색을 하지 않습니다</b> · 100% 오프라인 (Ollama 로컬).<br>'
        '<b>권장 워크플로우</b>:<br>'
        '&nbsp;&nbsp;1️⃣ Claude.ai · Gemini Deep Research · Perplexity 등 <b>웹 AI 에서 논문 탐색</b><br>'
        '&nbsp;&nbsp;2️⃣ 관심 논문 PDF 를 본인 노트북에 다운로드<br>'
        '&nbsp;&nbsp;3️⃣ 여기 <b>로컬 자료</b>에 업로드 → 세 에이전트가 근거 태깅과 함께 정리<br>'
        '<span style="font-size:0.74rem;color:#6c7b8a;">*미발표 원고·IRB 민감 자료는 1-2 단계 건너뛰고 3 단계부터 — 이 도구의 강점.</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    # ─────────────────────────────────────────────
    # 로컬 자료 업로더
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">로컬 자료 (논문 PDF · 연구 노트)</div>',
                unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        RESOURCES_HELP,
        type=["pdf", "md", "txt"],
        accept_multiple_files=True,
        key="resource_uploader",
    )
    if uploaded_files:
        resources, errors = ingest_uploads(uploaded_files)
        st.session_state.resources = resources
        if errors:
            for err in errors:
                st.warning(err)
    if st.session_state.resources:
        def _human_size(text: str) -> str:
            n = len(text.encode("utf-8"))
            if n < 1024:
                return f"{n}B"
            return f"{n / 1024:.1f}KB"
        chips = "".join(
            f'<span class="resource-chip">📎 {r["filename"]} ({_human_size(r.get("text") or "")})</span>'
            for r in st.session_state.resources
        )
        st.markdown(chips, unsafe_allow_html=True)
    else:
        st.caption("자료 없이 실행 가능. 모든 에이전트 출력이 [추측] 태깅됩니다 — "
                   "왜 자료가 필요한지 체감하는 장면.")

    # ─────────────────────────────────────────────
    # 연구 맥락 입력 폼
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">연구 맥락 입력</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        # 연구 분야 — 자유 입력 기본 + 프리셋 칩 원클릭 채우기
        current_field = st.session_state.inputs_snapshot.get("field", "")
        # 프리셋 칩 중 하나가 클릭되면 session_state 에 기록해 text_input 에 반영
        preset_presets = [f for f in RESEARCH_FIELDS if f != "기타 (직접 입력)"]
        if "field_chip_click" in st.session_state:
            current_field = st.session_state.pop("field_chip_click")

        field = st.text_input(
            "연구 분야",
            value=current_field,
            placeholder="예: 식품영양 / 노화과학 / 본인 세부 분야 자유 입력",
            help="프리셋에 없는 분야도 자유롭게 입력하세요. 아래 버튼은 빠른 채우기용.",
        )
        # 빠른 채우기 칩 — 한 줄 compact 버튼 그리드
        st.markdown(
            '<div style="font-family:IBM Plex Mono,monospace;font-size:0.62rem;'
            'color:#8a8a8a;letter-spacing:0.1em;margin:0.2rem 0 0.3rem;">QUICK FILL</div>',
            unsafe_allow_html=True,
        )
        chip_cols = st.columns(len(preset_presets))
        for i, preset in enumerate(preset_presets):
            with chip_cols[i]:
                if st.button(preset, key=f"field_chip_{i}", use_container_width=True):
                    st.session_state.field_chip_click = preset
                    st.rerun()
    with col2:
        current_stage = st.session_state.inputs_snapshot.get("stage", RESEARCH_STAGES[0])
        stage = st.selectbox(
            "연구 단계",
            RESEARCH_STAGES,
            index=RESEARCH_STAGES.index(current_stage) if current_stage in RESEARCH_STAGES else 0,
            help="단계별로 3-에이전트 프롬프트 트리오가 자동 전환됩니다 (Harness Engineering).",
        )
        # 단계별 안내 (특히 선행연구 정리는 PDF 업로드 전제)
        stage_notes = {
            "주제 탐색": "💡 업로드 자료 없어도 작동 · 가장 빠른 시연 경로",
            "선행연구 정리": "📎 논문 PDF 3-5개 업로드 전제 · 자료 없으면 모두 [추측]",
            "Research Question 도출": "🎯 🧠 사고 모드(사이드바) 권장 · 16GB 에선 느림",
        }
        if stage in stage_notes:
            st.markdown(
                f'<div style="font-family:Noto Sans KR,sans-serif;font-size:0.72rem;'
                f'color:#6a7a8c;margin-top:0.2rem;line-height:1.5;">'
                f'{stage_notes[stage]}</div>',
                unsafe_allow_html=True,
            )

    keywords = st.text_input(
        "관심 키워드 (쉼표로 구분)",
        value=st.session_state.inputs_snapshot.get("keywords", ""),
        placeholder=KEYWORDS_PLACEHOLDER,
    )
    context_input = st.text_area(
        "연구 맥락",
        value=st.session_state.inputs_snapshot.get("context", ""),
        height=140,
        placeholder=CONTEXT_PLACEHOLDER,
        help="소속, 학위 과정, 사용 가능한 데이터, 선호 방법론 등",
    )
    extra_input = st.text_area(
        "추가 조건 (선택)",
        value=st.session_state.inputs_snapshot.get("extra", ""),
        height=70,
        placeholder=EXTRA_PLACEHOLDER,
    )

    # 실행 버튼
    if st.button("연구팀 실행", type="primary", use_container_width=True):
        if not is_connected:
            st.error("Ollama에 연결할 수 없습니다. 터미널에서 `ollama serve`를 실행하세요.")
        elif not keywords.strip() or not context_input.strip():
            st.error("키워드와 연구 맥락은 반드시 입력해야 합니다.")
        elif not project_name.strip():
            st.error("프로젝트 이름을 입력하세요 (세션 저장에 사용됩니다).")
        else:
            reset_pipeline_outputs()
            st.session_state.inputs_snapshot = {
                "field": field,
                "stage": stage,
                "keywords": keywords,
                "context": context_input,
                "extra": extra_input,
                "advisor_mode": st.session_state.advisor_mode,
            }
            st.session_state.step = 1
            st.rerun()

    # ─────────────────────────────────────────────
    # 파이프라인 실행 + 시각화
    # ─────────────────────────────────────────────
    step = st.session_state.step
    advisor_on = st.session_state.advisor_mode
    inputs = st.session_state.inputs_snapshot
    resources = st.session_state.resources

    st.markdown("---")
    st.markdown(
        f'<div class="section-label">파이프라인 · {inputs.get("stage") or stage}</div>',
        unsafe_allow_html=True,
    )
    render_pipeline(step, advisor_on)

    stage_in_use = inputs.get("stage") or stage
    current_model = selected_model

    # ── Step 1: 수연 (scout) ──
    if step == 1 and inputs:
        model_for_step = pick_model("scout", current_model)
        st.markdown(
            f'<div class="result-header">Step I — 수연 (탐색/합성/RQ후보) <span style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;color:#8a8a8a;">· {model_for_step}</span></div>',
            unsafe_allow_html=True,
        )
        think_slot = st.empty() if st.session_state.think_mode else None
        placeholder = st.empty()
        try:
            output = run_streamed(
                stream_ollama(
                    model_for_step,
                    get_prompt(stage_in_use, "scout"),
                    build_user_payload(inputs, resources),
                    think=st.session_state.think_mode,
                ),
                placeholder,
                think_slot,
            )
            st.session_state.scout_output = output
            st.session_state.step = 2
            st.rerun()
        except Exception as e:
            st.error(f"오류: {e}")
            st.session_state.step = 0

    if step >= 2:
        with st.expander("Step I 결과 — 수연", expanded=False):
            st.markdown(st.session_state.scout_output)
            render_ledger(st.session_state.scout_output)

    # ── Step 2: 준호 (critic) ──
    if step == 2 and inputs:
        model_for_step = pick_model("critic", current_model)
        st.markdown(
            f'<div class="result-header">Step II — 준호 (검증) <span style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;color:#8a8a8a;">· {model_for_step}</span></div>',
            unsafe_allow_html=True,
        )
        think_slot = st.empty() if st.session_state.think_mode else None
        placeholder = st.empty()
        try:
            output = run_streamed(
                stream_ollama(
                    model_for_step,
                    get_prompt(stage_in_use, "critic"),
                    build_critic_payload(inputs, resources, st.session_state.scout_output),
                    think=st.session_state.think_mode,
                ),
                placeholder,
                think_slot,
            )
            st.session_state.critic_output = output
            st.session_state.step = 3
            st.rerun()
        except Exception as e:
            st.error(f"오류: {e}")
            st.session_state.step = 0

    if step >= 3:
        with st.expander("Step II 결과 — 준호", expanded=False):
            st.markdown(st.session_state.critic_output)
            render_ledger(st.session_state.critic_output)

    # ── Step 3: 지은 (director) ──
    if step == 3 and inputs:
        model_for_step = pick_model("director", current_model)
        st.markdown(
            f'<div class="result-header">Step III — 지은 (총괄) <span style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;color:#8a8a8a;">· {model_for_step}</span></div>',
            unsafe_allow_html=True,
        )
        think_slot = st.empty() if st.session_state.think_mode else None
        placeholder = st.empty()
        try:
            output = run_streamed(
                stream_ollama(
                    model_for_step,
                    get_prompt(stage_in_use, "director"),
                    build_director_payload(inputs, resources, st.session_state.scout_output, st.session_state.critic_output),
                    think=st.session_state.think_mode,
                ),
                placeholder,
                think_slot,
            )
            st.session_state.director_output = output
            st.session_state.step = 4 if advisor_on else 5
            if not advisor_on:
                persist_current_version("파이프라인 v1 완료")
            st.rerun()
        except Exception as e:
            st.error(f"오류: {e}")
            st.session_state.step = 0

    if step >= 4:
        with st.expander("Step III 결과 — 지은", expanded=(step == 5)):
            st.markdown(st.session_state.director_output)
            render_ledger(st.session_state.director_output)

    # ── Step 4: 한민수 (advisor, optional) ──
    if step == 4 and inputs and advisor_on:
        model_for_step = pick_model("advisor", current_model)
        st.markdown(
            f'<div class="result-header">Step IV — 한민수 (지도교수) <span style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;color:#8a8a8a;">· {model_for_step}</span></div>',
            unsafe_allow_html=True,
        )
        think_slot = st.empty() if st.session_state.think_mode else None
        placeholder = st.empty()
        try:
            output = run_streamed(
                stream_ollama(
                    model_for_step,
                    ADVISOR_PROMPT,
                    build_advisor_payload(inputs, st.session_state.director_output),
                    think=st.session_state.think_mode,
                ),
                placeholder,
                think_slot,
            )
            st.session_state.advisor_output = output
            st.session_state.step = 5
            persist_current_version("파이프라인 v1 + 지도교수 모드 완료")
            st.rerun()
        except Exception as e:
            st.error(f"오류: {e}")
            st.session_state.step = 5

    if step >= 5 and advisor_on and st.session_state.advisor_output:
        with st.expander("Step IV 결과 — 한민수 (지도교수)", expanded=True):
            st.markdown(st.session_state.advisor_output)
            render_ledger(st.session_state.advisor_output)

    # ─────────────────────────────────────────────
    # A/B 대조 실행 — 자료 없이 동일 파이프라인 재실행
    # ─────────────────────────────────────────────
    ab_step = st.session_state.ab_step
    if ab_step in (1, 2, 3) and inputs:
        ab_role = {1: "scout", 2: "critic", 3: "director"}[ab_step]
        role_label = {1: "수연 (탐색)", 2: "준호 (검증)", 3: "지은 (총괄)"}[ab_step]
        model_for_step = pick_model(ab_role, current_model)
        st.markdown(
            f'<div class="result-header">A/B 대조 — {role_label} · 자료 없이 실행 중… <span style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;color:#8a8a8a;">· {model_for_step}</span></div>',
            unsafe_allow_html=True,
        )
        think_slot = st.empty() if st.session_state.think_mode else None
        placeholder = st.empty()
        try:
            if ab_step == 1:
                system = get_prompt(stage_in_use, "scout")
                user = build_user_payload(inputs, [])
            elif ab_step == 2:
                system = get_prompt(stage_in_use, "critic")
                user = build_critic_payload(inputs, [], st.session_state.ab_scout_output)
            else:
                system = get_prompt(stage_in_use, "director")
                user = build_director_payload(inputs, [], st.session_state.ab_scout_output, st.session_state.ab_critic_output)
            out = run_streamed(
                stream_ollama(model_for_step, system, user, think=st.session_state.think_mode),
                placeholder, think_slot,
            )
            target = f"ab_{ab_role}_output"
            st.session_state[target] = out
            st.session_state.ab_step = ab_step + 1 if ab_step < 3 else 4
            st.rerun()
        except Exception as e:
            st.error(f"A/B {role_label} 오류: {e}")
            st.session_state.ab_step = 0

    # ─────────────────────────────────────────────
    # 완료 시: 배너 · v1↔v2 비교 · 정제 대화 · 산출물 메뉴
    # ─────────────────────────────────────────────
    if step == 5:
        render_completion(inputs, current_model)


# ═════════════════════════════════════════════════════════════════════
# 완료 화면 분리
# ═════════════════════════════════════════════════════════════════════

def render_completion(inputs: dict, model: str) -> None:
    state = st.session_state.session_state_dict or {}
    versions = state.get("versions", [])

    st.markdown(
        '<div class="completion-banner">'
        '<div class="completion-banner-title">파이프라인 완료 · 세션 저장됨</div>'
        '<div class="completion-banner-desc">'
        f".sessions/ 에 프로젝트가 저장되었습니다 (v{len(versions)}). "
        "아래에서 정제 대화·산출물을 이어가세요. 탭에서 v1/v2 비교 가능."
        "</div></div>",
        unsafe_allow_html=True,
    )

    # v1↔v2 비교 탭
    if len(versions) >= 2:
        latest2 = two_latest(state)
        tabs = st.tabs([f"v{v['version']} — {v['ts'][:16]}" for v in latest2])
        for tab, v in zip(tabs, latest2):
            with tab:
                if v.get("note"):
                    st.caption(v["note"])
                st.markdown("### 📋 지은 (총괄)")
                st.markdown(v["outputs"].get("director", "") or "_(없음)_")
                if v["outputs"].get("advisor"):
                    st.markdown("### 🎓 한민수 (지도교수)")
                    st.markdown(v["outputs"]["advisor"])

    # A/B 대조: 자료 포함 vs 자료 없음
    has_resources = bool(st.session_state.resources)
    ab_done = st.session_state.ab_step == 4 and st.session_state.ab_director_output
    ab_running = st.session_state.ab_step in (1, 2, 3)
    if has_resources and not ab_done and not ab_running:
        st.markdown(
            '<div class="result-header">A/B 대조 실행 (자료 효과 검증)</div>',
            unsafe_allow_html=True,
        )
        st.caption(
            "⚠️ 업로드 자료를 **빼고** 동일 파이프라인을 한 번 더 돌려 차이를 비교합니다. "
            "Track A '맥락(자료)의 효과'를 시각적으로 확인할 수 있습니다. "
            "약 3-6분 추가 소요."
        )
        if st.button("🅰🅱 자료 없이 재실행", key="ab_run_btn"):
            st.session_state.ab_step = 1
            st.rerun()
    elif ab_done:
        st.markdown(
            '<div class="result-header">A/B 대조 결과 — 자료 포함 vs 자료 없음</div>',
            unsafe_allow_html=True,
        )
        ab_tabs = st.tabs(["📎 자료 포함 (원본)", "🅱 자료 없음 (대조)"])
        with ab_tabs[0]:
            ledger_with = count_grounding(st.session_state.director_output)
            st.caption(f"근거 {ledger_with['grounded_total']}건 / 추측 {ledger_with['speculated_total']}건")
            st.markdown(st.session_state.director_output)
        with ab_tabs[1]:
            ledger_without = count_grounding(st.session_state.ab_director_output)
            st.caption(f"근거 {ledger_without['grounded_total']}건 / 추측 {ledger_without['speculated_total']}건")
            st.markdown(st.session_state.ab_director_output)
        st.caption(
            "💡 추측 태그 수가 자료 없는 쪽에서 눈에 띄게 늘고, 구체적 수치·근거가 줄어드는 것을 확인해보세요."
        )

    # 정제 대화 블록
    st.markdown('<div class="result-header">정제 대화 — 특정 단계만 재실행</div>', unsafe_allow_html=True)
    st.caption("예: '준호, 실행 가능성을 6개월 기준으로 재비판' → Step II 만 재실행, 버전 증가.")

    c1, c2 = st.columns([1, 3])
    with c1:
        target_label = st.radio(
            "대상 에이전트",
            options=[ROLE_LABELS["scout"], ROLE_LABELS["critic"], ROLE_LABELS["director"]]
                    + ([ROLE_LABELS["advisor"]] if st.session_state.advisor_mode else []),
            label_visibility="collapsed",
            key="refine_target_radio",
        )
    with c2:
        feedback = st.text_area(
            "보완 요청",
            placeholder="이 에이전트에게 어떤 식으로 다시 해달라고 할지 구체적으로 적으세요.",
            key="refine_feedback_area",
            height=100,
            label_visibility="collapsed",
        )
    if st.button("해당 단계만 재실행", type="primary"):
        target = {v: k for k, v in ROLE_LABELS.items()}.get(target_label, "critic")
        if feedback.strip():
            # Use the per-agent model for the selected role if advanced mode is on
            refine_model = pick_model(target, model)
            run_refinement(target, feedback, inputs, refine_model)
        else:
            st.warning("보완 요청 내용을 입력하세요.")

    # 산출물 메뉴
    st.markdown('<div class="result-header">산출물 내보내기</div>', unsafe_allow_html=True)
    render_exports(model)

    # Harness note
    if st.session_state.per_agent_mode and st.session_state.agent_models:
        split = " / ".join(
            f"<b>{r}</b>={m}" for r, m in st.session_state.agent_models.items() if m
        )
        harness_body = (
            f"현재 단계 ({inputs.get('stage')}) × 3개 역할 트리오가 활성화되었고, "
            f"역할마다 다른 모델이 할당되었습니다: {split}. "
            "같은 파이프라인 코드가 프롬프트(단계별)와 모델(역할별) 두 축으로 재사용됩니다. "
            "이것이 Harness Engineering 의 두 번째 증거입니다."
        )
    else:
        harness_body = (
            f"현재 단계 ({inputs.get('stage')}) × 3개 역할 트리오가 활성화되었습니다. "
            "단계 드롭다운을 바꾸면 동일한 3-에이전트 코드가 다른 프롬프트 트리오로 재사용됩니다. "
            "이것이 '같은 하네스, 다른 프롬프트'의 실체입니다. "
            "사이드바의 '⚙️ 에이전트별 모델 지정'을 켜면 역할별 모델 축도 추가됩니다."
        )
    st.markdown(
        '<div class="harness-note">'
        '<div class="harness-note-title">Harness Engineering</div>'
        f'<div class="harness-note-text">{harness_body}</div></div>',
        unsafe_allow_html=True,
    )


# ═════════════════════════════════════════════════════════════════════
# 정제 실행 (해당 단계만 재실행 + 버전 append)
# ═════════════════════════════════════════════════════════════════════

def run_refinement(role: str, feedback: str, inputs: dict, model: str) -> None:
    stage_in_use = inputs.get("stage") or RESEARCH_STAGES[0]
    resources = st.session_state.resources

    # 기존 해당 역할 출력 + 피드백을 user payload에 붙임
    feedback_block = (
        f"=== 사용자 보완 요청 ===\n{feedback}\n=== 요청 끝 ===\n\n"
        f"이 요청을 반드시 반영하여 해당 역할 결과물을 재작성하세요."
    )

    if role == "scout":
        system = get_prompt(stage_in_use, "scout")
        user = build_user_payload(inputs, resources) + "\n\n" + feedback_block
        target_key = "scout_output"
    elif role == "critic":
        system = get_prompt(stage_in_use, "critic")
        user = build_critic_payload(inputs, resources, st.session_state.scout_output) + "\n\n" + feedback_block
        target_key = "critic_output"
    elif role == "director":
        system = get_prompt(stage_in_use, "director")
        user = build_director_payload(inputs, resources, st.session_state.scout_output, st.session_state.critic_output) + "\n\n" + feedback_block
        target_key = "director_output"
    elif role == "advisor":
        system = ADVISOR_PROMPT
        user = build_advisor_payload(inputs, st.session_state.director_output) + "\n\n" + feedback_block
        target_key = "advisor_output"
    else:
        st.error(f"알 수 없는 역할: {role}")
        return

    st.markdown(f'<div class="result-header">정제 실행 — {ROLE_LABELS.get(role, role)}</div>', unsafe_allow_html=True)
    think_slot = st.empty() if st.session_state.think_mode else None
    placeholder = st.empty()
    try:
        output = run_streamed(
            stream_ollama(model, system, user, think=st.session_state.think_mode),
            placeholder,
            think_slot,
        )
        st.session_state[target_key] = output
        persist_current_version(f"정제 v{_next_version_num()}: {role} — {feedback[:40]}")
        st.success(f"{ROLE_LABELS.get(role, role)} 재실행 완료. 버전이 추가되었습니다.")
        st.rerun()
    except Exception as e:
        st.error(f"정제 실행 오류: {e}")


def _next_version_num() -> int:
    state = st.session_state.session_state_dict or {}
    return len(state.get("versions", [])) + 1


# ═════════════════════════════════════════════════════════════════════
# 산출물 메뉴
# ═════════════════════════════════════════════════════════════════════

def render_exports(model: str) -> None:
    director_output = st.session_state.director_output
    advisor_output = st.session_state.advisor_output

    if not director_output:
        st.info("지은 (총괄) 결과가 없으면 내보내기를 생성할 수 없습니다.")
        return

    choice = st.radio(
        "포맷 선택",
        options=list(EXPORT_LABELS.keys()),
        format_func=lambda k: EXPORT_LABELS[k],
        horizontal=False,
        key="export_radio",
    )

    if st.button("산출물 생성", key="export_btn"):
        reg = EXPORT_REGISTRY[choice]
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{reg['filename']}_{stamp}.{reg['ext']}"

        if reg["kind"] == "docx":
            # Include ALL three agents' outputs, not just the director's 📋 section.
            # The director's output alone misses 수연's exploration + 준호's critique.
            scout_out = st.session_state.scout_output or ""
            critic_out = st.session_state.critic_output or ""
            inputs = st.session_state.inputs_snapshot or {}
            stage = inputs.get("stage", "")

            final_design = extract_final_doc(director_output) or director_output

            parts = []
            # 1. 최종 연구 설계 (가장 먼저 — 지도교수에게 보여줄 것)
            parts.append("# 1. 최종 연구 설계 (지은)")
            parts.append(final_design)
            parts.append("")
            # 2. 탐색 단계 원문
            if scout_out:
                parts.append("# 2. 수연의 탐색 결과 (원문)")
                parts.append(scout_out)
                parts.append("")
            # 3. 검증 단계 원문
            if critic_out:
                parts.append("# 3. 준호의 검증 결과 (원문)")
                parts.append(critic_out)
                parts.append("")
            # 4. 지은 전체 (최종 섹션 외 나머지: 검증 결과, 검토 의견, 주의사항)
            if director_output and director_output.strip() != final_design.strip():
                parts.append("# 4. 지은의 총괄 전체 (원문)")
                parts.append(director_output)
                parts.append("")
            # 5. 지도교수 (있으면)
            if advisor_output:
                parts.append("# 5. 지도교수 (한민수) 의견")
                parts.append(advisor_output)
                parts.append("")
            # 6. 입력 맥락 — 재현성
            parts.append("# 부록. 입력 맥락")
            parts.append(f"- 연구 분야: {inputs.get('field', '')}")
            parts.append(f"- 단계: {stage}")
            parts.append(f"- 키워드: {inputs.get('keywords', '')}")
            parts.append(f"- 맥락: {inputs.get('context', '')}")
            if inputs.get("extra"):
                parts.append(f"- 추가조건: {inputs.get('extra', '')}")
            parts.append(f"- 모델: {model}")

            full_doc = "\n".join(parts)
            buf = create_docx(full_doc, DOCX_HEADER, DOCX_DISCLAIMER)
            st.download_button(
                label=f"⬇ {filename} 내려받기",
                data=buf,
                file_name=filename,
                mime=reg["mime"],
                type="primary",
            )
        else:
            fn = reg["fn"]
            with st.spinner(f"{EXPORT_LABELS[choice]} 생성 중... (로컬 Ollama)"):
                if choice == "advisor_sheet":
                    content = fn(model, director_output, advisor_output)
                else:
                    content = fn(model, director_output)
            st.text_area("생성된 산출물 미리보기", value=content, height=260)
            st.download_button(
                label=f"⬇ {filename} 내려받기",
                data=content.encode("utf-8"),
                file_name=filename,
                mime=reg["mime"],
                type="primary",
            )


if __name__ == "__main__":
    main()
