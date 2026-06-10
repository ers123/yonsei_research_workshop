# 04. Codex Multi-Thread 고급예시

이 폴더는 기본 워크플로가 아닙니다.

학생이 ChatGPT, Claude, Gemini 중 하나의 유료 LLM만 가지고 있어도 `01_학생용_핵심가이드.md`와 `03_prompts_appendix/`로 논문 초안 패키지를 만들 수 있습니다.

이 폴더는 다음 상황에서만 봅니다.

- 자료가 많아서 한 대화창에 모두 넣기 어렵다.
- 문헌 검토, evidence binding, outline, draft, critique를 분리하고 싶다.
- Codex multi-thread, Claude Code subagents/team, Antigravity workflow처럼 여러 작업 단위를 병렬 또는 순차로 맡길 수 있는 도구를 쓴다.

## 학생용 읽는 순서

이 폴더만 처음 보면 다소 추상적으로 보일 수 있습니다. 다음 순서로 보면 이해하기 쉽습니다.

1. 이 README에서 전체 구조를 본다.
2. `thread_model.md`에서 supervisor + worker 구조를 본다.
3. `codex_supervisor_prompt.md`를 복사해 team-lead room을 시작하는 법을 본다.
4. `../03_prompts_appendix/09_research_AGENTS.md`를 실제 프로젝트 루트의 `AGENTS.md`로 옮겨 반복 운영 규칙을 저장한다.
5. `thread-map.md`와 `supervisor-merge-report.md`는 이미 실행된 예시로만 참고한다.

핵심은 04번 폴더의 모든 파일을 외우는 것이 아니라, `AGENTS.md`에 팀장 방/담당자 방/phase gate/완료 보고 규칙을 저장해 두는 것입니다.

## 핵심 모델

```text
Supervisor thread
  -> Materials Mapper
  -> Literature Mapper
  -> Evidence Binder
  -> Outline Architect
  -> Critic / Verifier
  -> Supervisor merge
  -> Human decision
```

worker를 10개 이상 계속 늘리는 방식이 아닙니다. 연구실 워크숍에서는 4-5개 worker가 가장 설명하기 쉽고, 결과도 합치기 쉽습니다.

영상의 표현으로 바꾸면, supervisor thread는 "팀장 방"이고 worker thread는 "담당자 방"입니다. 팀장 방은 직접 논문을 쓰지 않고, 담당자 방의 완료 보고를 취합한 뒤 phase마다 멈춰서 사람에게 다음 진행 여부를 묻습니다.

## 파일 설명

| 파일 | 용도 |
|---|---|
| `thread_model.md` | supervisor + 4-5 worker 구조 설명 |
| `codex_supervisor_prompt.md` | Codex에서 supervisor thread를 시작할 때 쓰는 프롬프트 |
| `AGENTS.md.example` | 연구 프로젝트용 agent memory 예시 |
| `claude_code_subagents_note.md` | `presentation.html`을 참고한 Claude Code subagents 적용 노트 |
| `antigravity_workflow_note.md` | Antigravity workflow로 같은 사고방식을 옮기는 방법 |

## 기존 참고 자료

루트의 `presentation.html`은 Claude Code subagents 개념을 참고하기 위해 둔 자료입니다. 이 워크숍의 메인 발표 자료가 아니라, 04번 고급예시를 설명할 때만 보조로 참고하시기 바랍니다.

이미 만들어진 thread 관련 산출물도 함께 보관했습니다.

- `compact-parallel-research-lab-prompt-pack.md`
- `compact-thread-model.md`
- `supervisor-merge-report.md`
- `thread-explosion-postmortem.md`
- `thread-map.md`
