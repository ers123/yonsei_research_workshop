# Case Study: Thread-Based Paper Lab

이 case study는 Codex thread 기반 논문 작성 시연에서 얻은 공개용 운영 요약입니다.

원래 실행에는 더 많은 thread와 반환 파일이 있었지만, 학생이 따라 할 권장 모델은 compact model입니다.

## 핵심 메시지

```text
하나의 채팅창에 논문 전체를 맡기지 않는다.
Supervisor가 worker threads에 역할을 나누어 맡기고, 반환 파일을 모아 source-gated draft package를 만든다.
```

## 실제 실행에서 배운 것

### 잘 된 점

- 문헌, 방법/데이터, 검증, 초안, 리뷰, 시각화를 분리하니 각 판단의 책임이 선명해졌다.
- source verifier가 blocked claim을 분리하면서 초안의 과장 가능성을 줄였다.
- reviewer thread를 따로 두니 초안 작성 thread가 놓친 overclaim과 caveat를 찾기 쉬웠다.
- visual-assets 역할을 두면서 figure/table이 장식이 아니라 claim-support 장치라는 점이 보였다.

### 개선한 점

- 처음에는 역할 소개용 thread와 실행용 thread가 분리되어 thread 수가 많아졌다.
- outline, drafting, revision, packaging을 모두 다른 thread로 만들면 발표 화면이 복잡해진다.
- 그래서 공개 권장안은 supervisor 1개 + worker 5개로 줄였다.

## 권장 public model

| Role | Why it exists |
|---|---|
| Supervisor | 전체 지휘, phase gate, 반환 병합, human signoff |
| Evidence-Literature | 문헌 위치, theory lens, citation 후보 |
| Data-Methods | 자료가 허용하는 claim과 허용하지 않는 claim |
| Visual-Assets | 표/그림 spec, caption, safety label |
| Review-Verification | source, privacy, overclaim, citation risk gate |
| Drafting | outline, draft, revision |

## Case study files

- [thread_model_public.md](thread_model_public.md)
- [handoff_board_public.md](handoff_board_public.md)
- [thread_explosion_lesson.md](thread_explosion_lesson.md)
- [visual_assets_workflow.md](visual_assets_workflow.md)

## 공개 자료 경계

이 case study는 운영 방식만 보여줍니다. 원자료, 인터뷰 원문, 참여자 단위 데이터, private link는 포함하지 않습니다.
