# Project Folder Template

새 연구 프로젝트를 시작할 때 아래 구조를 권장합니다.

```text
paper-project/
  AGENTS.md
  context/
    task-brief.md
    do-not-claim.md
    ai-use-log.md
    human-decisions.md
  sources/
    papers/
    benchmark-papers/
    reading-notes.md
  data/
    sanitized-summary.md
    analysis-readiness.md
    raw-private/
  evidence/
    materials-inventory.md
    findings-summary.md
    evidence-bindings.md
    source-verification.md
  figures/
    specs/
    generated/
    approved/
    visual-manifest.md
  draft/
    outline.md
    first-draft.md
    review.md
    revised-draft.md
    draft-package.md
  threads/
    supervisor/
    evidence-literature/
    data-methods/
    visual-assets/
    review-verification/
    drafting/
```

## Folder Rules

- `raw-private/` 자료는 외부 모델에 보내지 않는다.
- `generated/` 그림은 승인 전 초안이다.
- `approved/` 그림만 원고에 삽입한다.
- worker thread는 자기 폴더의 return 파일 하나만 작성한다.
- supervisor만 여러 반환 파일을 읽고 병합한다.
