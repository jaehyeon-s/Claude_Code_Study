#!/usr/bin/env python3
"""아주 작은 할 일 관리 CLI.

사용법:
    python todo.py add "장보기"      # 할 일 추가
    python todo.py list              # 목록 보기
    python todo.py done 1            # 1번 완료 처리
"""
import json
import sys
from pathlib import Path

# 할 일을 저장할 파일 (프로그램과 같은 폴더에 tasks.json 생성)
DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """저장된 할 일들을 읽어온다. 파일이 없으면 빈 목록."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def save_tasks(tasks):
    """할 일 목록을 파일에 저장한다."""
    DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ 추가됨: {title}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("(할 일이 없습니다)")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")


def complete_task(index):
    tasks = load_tasks()
    # 사용자는 1번부터 세므로 -1 해서 실제 위치를 찾는다
    tasks[index - 1]["done"] = True
    save_tasks(tasks)
    print(f"🎉 완료: {tasks[index - 1]['title']}")


def delete_task(index):
    tasks = load_tasks()
    # 사용자는 1번부터 세므로 -1 해서 실제 위치를 찾는다
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"🗑️ 삭제됨: {removed['title']}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return

    command = args[0]
    if command == "add":
        add_task(args[1])
    elif command == "list":
        list_tasks()
    elif command == "done":
        complete_task(int(args[1]))
    elif command == "delete":
        delete_task(int(args[1]))
    else:
        print(f"알 수 없는 명령: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
