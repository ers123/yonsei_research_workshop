# Claude Code Subagents Note

루트의 `presentation.html`은 Claude Code subagents 개념을 참고하기 위해 보관한 자료입니다. 워크숍에서는 이 파일을 메인 자료로 설명하기보다, "Codex multi-thread와 같은 사고방식을 Claude Code에서는 subagents로 옮길 수 있다"는 보조 예시로 쓰면 충분합니다.

## 연구실 workflow로 번역하기

Claude Code subagent는 독립된 전문 작업자를 보내고, main conversation에는 결과 요약만 돌려받는 방식으로 이해하면 쉽습니다.

논문 작성에서는 다음처럼 매핑할 수 있습니다.

| 연구 workflow | Claude Code subagent 역할 |
|---|---|
| 자료 목록화 | materials-mapper |
| 문헌 흐름 정리 | literature-mapper |
| claim-source 연결 | evidence-binder |
| 목차 설계 | outline-architect |
| 위험 검토 | critic-verifier |

## 왜 유용한가

- 긴 파일 탐색이나 반복 검토가 main context를 오염시키지 않는다.
- read-only reviewer처럼 권한을 제한할 수 있다.
- 서로 독립적인 조사 작업을 병렬로 맡길 수 있다.
- main conversation은 supervisor 역할에 집중할 수 있다.

## 연구용 subagent 예시

```md
---
name: evidence-binder
description: Map manuscript claims to provided sources and flag unsupported claims.
tools: Read, Grep, Glob
model: sonnet
---

You are an evidence-binding reviewer for an academic manuscript project.

Use only provided project files.
Do not edit files.
Do not invent citations, statistics, quotes, or participant details.

Return:
- allowed claims
- allowed-with-caveat claims
- blocked claims
- human-only decisions
- missing sources
```

## 주의할 점

- subagent는 별도 context에서 시작하므로 필요한 배경을 task message에 충분히 넣어야 한다.
- worker를 많이 만들수록 supervisor merge 비용이 커진다.
- background 작업은 permission prompt를 처리하지 못할 수 있으므로, 연구자료를 다룰 때는 read-only agent부터 시작하는 것이 좋다.
- 비용이 커질 수 있으므로, 워크숍에서는 4-5개 역할까지만 보여주는 것이 적절하다.

## 참고

- 루트의 `presentation.html`: Claude Code subagents 개념 설명용 참고 자료
- Claude Code 공식 subagents 문서: https://code.claude.com/docs/en/sub-agents
