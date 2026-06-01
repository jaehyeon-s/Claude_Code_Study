# CLAUDE.md

이 파일은 Claude Code가 이 저장소에서 작업할 때 매번 자동으로 참고하는 프로젝트 메모리입니다.

## 프로젝트 개요
Claude Code를 일주일간 학습하기 위한 실습 저장소. (`README.md` 참고)
연습용 예제로 작은 할 일 관리 CLI(`todo.py`)를 발전시켜 나간다.

## 실행 방법
```bash
python3 todo.py add "내용"   # 할 일 추가
python3 todo.py list         # 목록 보기
python3 todo.py done <번호>  # 완료 처리
```

## 컨벤션
- 언어: Python 3 (표준 라이브러리만 사용, 외부 의존성 없음)
- 주석/문서: 학습용이므로 한국어로 친절하게 설명을 단다.
- 데이터는 `tasks.json`에 저장 (커밋하지 않음 — 런타임 산출물).

## 주의사항
- 작업 브랜치: `claude/charming-mayer-1QmW7`
- 이 환경은 Claude Code on the Web (임시 컨테이너) → 결과물은 반드시 commit & push.
