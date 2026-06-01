# 📅 Claude Code 일주일 마스터 플랜 (Python)

> 진행 방식: 매 세션 `개념(짧게) → Claude가 도구 실제 실행 시연 → 직접 시켜보기`
> 모든 결과물은 이 repo에 커밋하여 복습 가능하게 보존.

| Day | 주제 | 실습 예제 (Python) | 상태 |
|-----|------|--------------------|------|
| **1** | 기본기 & 멘탈모델 | 작은 CLI 앱 뼈대 만들기 + `/init`으로 CLAUDE.md 생성 | ✅ 진행중 |
| **2** | 파일 탐색 & 코드 작성 | 기능 구현 → 버그 심기 → 찾아서 수정 (Read/Grep/Edit) | ⬜ |
| **3** | Git & GitHub | 브랜치→커밋→PR 생성→리뷰 (GitHub MCP) | ⬜ |
| **4** | Plan Mode & 대규모 작업 | 멀티 파일 리팩터링: 계획→승인→실행 | ⬜ |
| **5** | 스킬 & 슬래시 커맨드 | `/code-review`, `/security-review`, `/simplify` | ⬜ |
| **6** | 설정 & 자동화 | `settings.json`, Hooks(저장 시 자동 테스트), MCP 활용 | ⬜ |
| **7** | 종합 실전 | 작은 앱 풀사이클: 기획→구현→리뷰→테스트→PR | ⬜ |

## 핵심 멘탈모델
- Claude Code는 챗봇이 아니라 **도구를 쓰는 에이전트**: 파일 읽기(Read), 검색(Glob/Grep),
  편집(Edit/Write), 실행(Bash), 위임(서브에이전트), 스킬(슬래시 커맨드) 등을 직접 수행.
- **Claude Code on the Web** 환경: 클라우드의 임시 컨테이너 → 결과물은 반드시 commit & push 해야 보존.
- 작업 브랜치: `claude/charming-mayer-1QmW7`

## 진도 로그
- Day 1 (2026-06-01): 로드맵 저장, 멘탈모델, 첫 CLI 앱 실습 시작
