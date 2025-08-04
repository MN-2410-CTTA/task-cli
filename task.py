import sys
import os
import json
from datetime import datetime


def show_help():
    print("Usage:")
    print("  python task.py add \"Task description\"")
    print("  python task.py list")
    print("  python task.py update <id> \"New description\"")
    print("  python task.py delete <id>")
    print("  python task.py mark-done <id>")
    print("  python task.py mark-in-progress <id>")
    print("  python task.py list <status>  # todo | done | in-progress")


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def format_task(task, show_status=True):
    lines = [
        f"[{task['id']}] {task['description']}",
        f"    Created at : {task['createdAt']}",
        f"    Updated at : {task['updatedAt']}"
    ]
    if show_status:
        lines.insert(1, f"    Status     : {task['status']}")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            return

        tasks = load_tasks()
        next_id = max((task['id'] for task in tasks), default=0) + 1
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        new_task = {
            "id": next_id,
            "description": sys.argv[2],
            "status": "todo",
            "createdAt": now,
            "updatedAt": now
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {next_id})")

    elif command == "list":
        tasks = load_tasks()
        status_titles = {
            "todo": "📝 Todo Tasks",
            "in-progress": "🔧 In-Progress Tasks",
            "done": "✅ Done Tasks"
        }

        if len(sys.argv) == 3:
            status = sys.argv[2]
            filtered_tasks = [task for task in tasks if task['status'] == status]
            print(f"{status_titles.get(status, 'Tasks')}\n{'─' * 44}")
            for task in filtered_tasks:
                print(format_task(task, show_status=False))
        else:
            print("📋 All Tasks\n" + "─" * 44)
            for task in tasks:
                print(format_task(task))

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Missing task ID or new description.")
        else:
            task_id = sys.argv[2]
            new_description = sys.argv[3]
            print(f"[Placeholder] Update task {task_id} with: {new_description}")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Missing task ID.")
        else:
            task_id = sys.argv[2]
            print(f"[Placeholder] Delete task {task_id}")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Missing task ID.")
        else:
            task_id = sys.argv[2]
            print(f"[Placeholder] Mark task {task_id} as done")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Missing task ID.")
        else:
            task_id = sys.argv[2]
            print(f"[Placeholder] Mark task {task_id} as in-progress")

    else:
        print(f"Unknown command: {command}")
        show_help()


if __name__ == "__main__":
    main()
