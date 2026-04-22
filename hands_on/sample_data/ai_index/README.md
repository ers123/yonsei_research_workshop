# AI Index 2026 — Track B 실습 자료

Track B (대량 자료 처리)의 주 실습 자료입니다.

## 파일

| 파일 | 크기 | 용도 |
|------|------|------|
| `ai_index_report_2026.pdf` | 약 37 MB | 원본 PDF (Stanford HAI, 2026). Part 1 Naive 접근 + Part 2 직접 추출 시도 |
| `ai_index_extracted_backup.md` | 약 13 KB | 미리 추출된 백업. Part 2에서 추출이 시간 초과되거나 실패했을 때 사용 |

## 원본 출처

- **Stanford HAI**, *Artificial Intelligence Index Report 2026*
- 공식 링크: https://hai.stanford.edu/ai-index/
- 라이선스: CC BY-ND 4.0 (원본). 본 추출본은 CC BY-NC-SA 4.0.

## 실습 흐름

상세는 `hands_on/prompts_v2/track_b_대량처리.md` 참조.

요약:
1. **Part 1** — 원본 PDF를 챗봇에 그대로 업로드 → 난이도별 질문 3개 (쉬움/중간/어려움)
2. **Part 2** — Claude Code로 마크다운 추출 시도. 시간 초과 시 `ai_index_extracted_backup.md` 사용
3. **Part 3** — 같은 질문을 추출본에 다시. Naive vs Harness 비교
4. **Part 4** — 같은 추출본으로 다른 질문 N개 (재사용성 증명)

## 왜 AI Index인가

- **최신 (2026)**: 워크숍 Part 1에서 인용한 통계 상당수가 이 리포트 출처
- **대용량 (37MB, 423 pages)**: 실무에서 마주치는 "큰 공공 리포트"의 전형
- **다양한 시각 자료**: 표, 시계열 차트, 지도 — naive 접근의 한계가 명확히 드러남
- **공개 자료**: 저작권 이슈 없이 자유롭게 실습·재배포 가능
- **메타 즐거움**: AI 워크숍에서 AI Index를 분석한다는 재귀성
