# 02. Evidence Binding Prompt

초안 claim과 source를 묶는 프롬프트입니다.

```text
아래 자료를 바탕으로 evidence binding table을 작성해 주세요.

입력:
- task-brief.md
- materials-inventory.md
- findings-summary.md
- do-not-claim.md
- 현재 outline 또는 section plan

목표:
- 각 section 또는 paragraph target이 어떤 source, note, finding에 기대는지 연결합니다.
- source가 없는 claim은 draft에 넣지 않습니다.
- 통계, 인과, quote, 일반화는 별도로 human-only 또는 needs verification으로 표시합니다.

출력 표:
| Section | Claim or paragraph target | Source / note / finding ID | Evidence status | Draft use | Risk |
|---|---|---|---|---|---|

Evidence status는 다음 중 하나로 표시하세요.
- allowed
- allowed with caveat
- blocked
- human-only
- needs verification

마지막에 다음을 정리하세요.
1. draft에 바로 쓸 수 있는 claim
2. caveat와 함께만 쓸 수 있는 claim
3. 차단해야 할 claim
4. 사람이 확인해야 할 claim
5. 누락된 source

주의:
- citation처럼 보이는 표현을 만들지 마세요.
- source가 약하면 약하다고 표시하세요.
- 확인되지 않은 참고문헌 정보를 지어내지 마세요.
```
