# 06. Claude Code / Antigravity용 Harness 확장

## 한 줄 설명

Codex thread 연구실의 핵심은 Codex 자체가 아니라, supervisor가 역할별 worker를 나누고 반환 파일을 병합하는 운영 방식입니다. Claude Code와 Antigravity에서도 같은 논리를 재현할 수 있습니다.

## 왜 별도 항목으로 다루는가

연구실 구성원마다 사용하는 AI coding/research assistant가 다를 수 있습니다.

- Codex 사용자는 thread를 나누어 supervisor-worker 구조를 직접 운영할 수 있습니다.
- Claude Code 사용자는 `revfactory/harness`로 `.claude/agents/`와 `.claude/skills/`를 생성해 팀 구조를 더 명시적으로 만들 수 있습니다.
- Antigravity 사용자는 Harness 산출물을 그대로 실행하기보다 Project, Rules, Workflows, Subagents, Worktree를 이용해 같은 파일 계약을 옮기는 편이 안전합니다.

따라서 이 장은 "Codex가 아니어도 이렇게 가능합니다"를 보여주는 보조 트랙입니다.

## 개념 매핑

| 워크숍 개념 | Codex | Claude Code + Harness | Antigravity 적용 |
|---|---|---|---|
| Supervisor | 감독 thread | orchestrator agent 또는 skill | main agent / workflow owner |
| Worker | 별도 thread | `.claude/agents/{role}.md` | subagent 또는 별도 agent |
| 작업 계약 | worker prompt | agent definition + skill trigger | Rule + Workflow prompt |
| 반환 파일 | `threads/{role}/return.md` | `_workspace/{phase}-{role}.md` 또는 지정 산출물 | `threads/{role}/return.md` 같은 공유 파일 |
| 검증 gate | Review-Verification thread | reviewer/qa agent | reviewer subagent + human review |
| 병합 | supervisor merge prompt | orchestrator merge pass | main agent merge pass |
| 인간 승인 | human-only checklist | `CLAUDE.md` / skill rule에 명시 | project rule / workflow gate |

핵심은 파일 이름이 아니라 역할과 책임입니다. worker가 같은 파일을 동시에 고치게 하지 말고, 먼저 반환 파일을 쓰게 한 뒤 supervisor가 병합합니다.

## Claude Code에서 Harness로 구성하기

`revfactory/harness`는 Claude Code용 team-architecture factory입니다. domain description을 주면 agent team, role definition, skill, orchestration rule을 생성하는 방식입니다.

공개 README와 quickstart 기준의 기본 흐름은 다음과 같습니다.

```bash
claude plugin marketplace add revfactory/harness
claude plugin install harness@harness
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

저장소 문서에는 설치 명령 표기가 위치에 따라 조금 다를 수 있습니다. 실제 워크샵이나 연구실 세팅에서는 최신 README와 quickstart를 확인한 뒤 한 가지 명령으로 통일해 안내하는 것이 좋습니다.

### Harness 생성 프롬프트

```text
하네스를 구성해줘.

도메인:
연세대학교 대학원 연구실의 AI-assisted research writing lab.

목표:
- 대학원생이 논문 작성 과정에서 AI를 연구보조원처럼 쓰게 한다.
- AI가 최종 저자나 최종 판단자가 되지 않도록 한다.
- 자료 정리, 문헌 위치 잡기, 데이터/방법 검토, 시각화 계획, 검증, 초안 작성, 인간 승인 과정을 역할별로 분리한다.

원하는 팀 구조:
1. Supervisor-Orchestrator
2. Evidence-Literature Specialist
3. Data-Methods Specialist
4. Visual-Assets Specialist
5. Review-Verification Specialist
6. Drafting Specialist

운영 패턴:
- Fan-out/Fan-in: 문헌, 데이터/방법, 시각화 worker를 병렬로 실행한다.
- Producer-Reviewer: Drafting 결과는 Review-Verification을 통과해야 한다.
- Supervisor: 최종 병합과 human-only gate는 Supervisor가 관리한다.

공통 규칙:
- 각 worker는 자기 반환 파일 하나만 책임진다.
- Review-Verification이 blocked 처리한 claim은 초안에 넣지 않는다.
- raw data, raw quote, 실명, private link, participant-level detail은 공개/수업용 산출물에 넣지 않는다.
- quote, statistics, ethics, external circulation은 human-only gate로 남긴다.

생성할 산출물:
- `.claude/agents/` 아래 역할별 agent definition
- `.claude/skills/` 아래 research-writing orchestration skill
- `CLAUDE.md`에는 긴 지침을 반복하지 말고, skill trigger와 파일 계약 포인터만 남긴다.
- `_workspace/` 또는 `threads/` 아래 반환 파일 convention을 문서화한다.
```

### 기대 산출물

Harness가 잘 구성되면 다음 구조를 기대할 수 있습니다.

```text
.claude/
  agents/
    supervisor-orchestrator.md
    evidence-literature.md
    data-methods.md
    visual-assets.md
    review-verification.md
    drafting.md
  skills/
    research-writing-lab/
      SKILL.md
      references/
CLAUDE.md
_workspace/
```

### Agent Teams와 subagents 선택

Claude Code에서는 크게 두 가지 운영을 생각할 수 있습니다.

| 선택 | 언제 쓰나 | 주의 |
|---|---|---|
| Agent Teams | worker끼리 조율하거나, supervisor가 여러 agent에게 계속 메시지를 보내야 할 때 | 실험 기능 flag와 비용/토큰 증가를 고려 |
| Subagents | 특정 역할에게 한 번 맡기고 결과를 main session으로 돌려받으면 충분할 때 | peer-to-peer 협업보다는 main session 중심 |

논문 워크샵에서는 처음부터 Agent Teams를 강하게 요구하기보다, subagent 또는 Harness-generated role prompt만으로도 충분히 데모할 수 있습니다. 다만 팀 간 검증과 장기 운영을 보여주려면 Agent Teams가 더 자연스럽습니다.

## Antigravity로 옮기는 방식

Antigravity는 Harness의 `.claude/agents/`와 `.claude/skills/`를 그대로 실행하는 런타임으로 보지 않는 편이 안전합니다. 대신 Harness가 만든 agent/skill 문서를 "역할 설계서"로 읽고, Antigravity의 Project, Rules, Workflows, Subagents로 옮깁니다.

### Project rule 예시

Antigravity 프로젝트에는 `.agents/rules/` 아래 markdown 규칙을 둘 수 있습니다.

```text
# Research Writing Lab Rule

이 프로젝트에서 AI agent는 논문 최종 저자가 아니라 연구보조 역할을 한다.

공통 규칙:
- source가 없는 claim을 만들지 않는다.
- raw data, raw quote, 실명, private link, participant-level detail을 공개 산출물에 넣지 않는다.
- worker는 먼저 반환 파일을 작성한다.
- supervisor 역할의 agent만 최종 병합 파일을 수정한다.
- Review-Verification이 blocked 처리한 claim은 초안에 넣지 않는다.
- quote, statistics, ethics, external circulation은 human-only gate다.

기본 반환 파일:
- Evidence-Literature: `threads/evidence-literature/return.md`
- Data-Methods: `threads/data-methods/return.md`
- Visual-Assets: `figures/visual-manifest.md`
- Review-Verification: `threads/review-verification/return.md`
- Drafting: `threads/drafting/return.md`
```

### Workflow prompt 예시

```text
workflow name: research-writing-lab

목표:
현재 프로젝트 폴더의 자료를 바탕으로 논문 초안 패키지를 만든다. 완성 논문이나 publication-ready claim을 만들지 않는다.

단계:
1. Supervisor intake: 자료 목록, 금지 주장, human-only gate를 확인한다.
2. Evidence-Literature, Data-Methods, Visual-Assets subagent를 독립 실행한다.
3. 각 subagent는 지정된 반환 파일만 작성한다.
4. Review-Verification subagent가 반환 파일과 draft 후보 claim을 검토한다.
5. Drafting subagent는 허용된 claim만 사용해 section outline 또는 paragraph unit draft를 작성한다.
6. Supervisor가 merge report와 human signoff checklist를 작성한다.

중요:
같은 본문 파일을 여러 subagent가 동시에 수정하지 않는다. 병렬 작업은 return file까지만 허용한다.
```

### Antigravity 운영 팁

- Project는 연구 자료가 들어 있는 폴더와 공개 산출물 폴더를 구분해서 구성합니다.
- 병렬 작업이나 위험한 수정이 있으면 Worktree를 사용해 기본 폴더를 보호합니다.
- Rules에는 짧고 반복 가능한 금지/허용 규칙을 둡니다.
- Workflows에는 단계 순서와 반환 파일 계약을 둡니다.
- Subagent에게 직접 초안 파일을 고치게 하기보다 먼저 반환 파일을 만들게 합니다.
- 터미널 명령, 외부 URL 읽기, private folder 접근은 permission rule로 제한합니다.

## Codex에서 multi-thread를 invoke하는 법

Codex에서는 "thread를 나눈다"가 실제로 별도 대화/작업 단위를 만든다는 뜻입니다. 수동 운영과 도구 기반 운영을 모두 사용할 수 있습니다.

### 수동 운영

1. Supervisor thread를 하나 엽니다.
2. 같은 프로젝트에서 Evidence-Literature, Data-Methods, Visual-Assets, Review-Verification, Drafting thread를 만듭니다.
3. 각 worker thread 제목과 역할을 `threads/thread-map.md`에 기록합니다.
4. 각 worker에는 `Worker Common Contract`와 역할별 prompt를 보냅니다.
5. 각 worker는 지정된 반환 파일 하나만 작성합니다.
6. Supervisor는 반환 파일을 읽고 `merge-report.md`, `source-verification.md`, `human-decisions.md`를 만듭니다.

### Codex 앱 도구 기반 운영

현재 Codex 앱에서는 별도 thread를 만들고, 기존 thread에 메시지를 보내고, thread 상태를 읽는 방식의 조율이 가능합니다.

```text
create_thread:
- 새 worker thread를 만든다.
- 같은 프로젝트의 local 환경 또는 별도 worktree 환경을 선택한다.

send_message_to_thread:
- worker thread에 역할 prompt나 후속 지시를 보낸다.

read_thread:
- worker thread의 최근 상태와 요약을 감독 thread에서 확인한다.
```

작업 방식은 다음과 같습니다.

```text
Supervisor
  1. worker별 목표와 반환 파일을 정한다.
  2. create_thread로 worker를 만든다.
  3. send_message_to_thread로 역할 prompt를 보낸다.
  4. read_thread와 반환 파일로 완료 상태를 확인한다.
  5. 충돌이 없을 때만 supervisor가 병합한다.
```

중요한 제한도 있습니다.

- worker가 자동으로 supervisor에게 "던져주는" 마법 같은 병합은 기대하지 않습니다.
- supervisor가 thread summary와 반환 파일을 읽고 병합해야 합니다.
- 여러 worker가 같은 파일을 수정하면 충돌 위험이 큽니다.
- read-only 분석은 같은 local 프로젝트에서 해도 되지만, 파일 수정이 병렬로 일어나면 worktree를 쓰는 편이 안전합니다.

## 키 메시지

```text
Codex, Claude Code, Antigravity 중 어떤 도구를 쓰느냐보다 중요한 것은 역할 분리, 반환 파일, 검증 gate, human-only decision을 남기는 것입니다. 도구는 달라도 연구자가 director라는 구조는 같습니다.
```

## 참고 링크

- `revfactory/harness`: https://github.com/revfactory/harness
- Harness quickstart: https://github.com/revfactory/harness/blob/main/docs/quickstart.md
- Harness experimental dependency note: https://github.com/revfactory/harness/blob/main/docs/experimental-dependency.md
- Claude Code subagents documentation: https://code.claude.com/docs/en/sub-agents
- Antigravity Projects documentation: https://www.antigravity.google/docs/projects
- Antigravity Rules and Workflows documentation: https://antigravity.google/docs/rules-workflows
- Antigravity Subagents documentation: https://antigravity.google/docs/subagents
