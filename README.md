# 📝 Task CLI — Command-Line Task Manager in Python

A simple and efficient command-line tool to manage tasks (to-dos, in-progress, done) using Python and JSON for local storage.

## 📦 Features

- Add, update, and delete tasks
- Mark tasks as "done" or "in-progress"
- Filter and list tasks by status
- Stores tasks in a persistent `tasks.json` file
- Easy to use, lightweight, and dependency-free

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.7 or higher

### 📥 Installation
Clone the repository:
```bash
git clone https://github.com/MN-2410-CTTA/task-cli.git
cd task-cli
```

(Optional) Make the script executable:
```bash
chmod +x task.py
```

---

## 📌 Usage

```bash
python task.py <command> [args]
```

### Commands

| Command | Description |
|--------|-------------|
| `add "description"` | Add a new task |
| `list` | List all tasks |
| `list <status>` | List tasks by status: `todo`, `done`, `in-progress` |
| `update <id> "new description"` | Update a task's description |
| `delete <id>` | Delete a task by ID |
| `mark-done <id>` | Mark a task as done |
| `mark-in-progress <id>` | Mark a task as in-progress |

---

### ✅ Example
```bash
python task.py add "Finish documentation"
python task.py list
python task.py update 1 "Finish documentation v1"
python task.py mark-in-progress 1
python task.py mark-done 1
python task.py delete 1
```

---

## 🗃 Data Storage

Tasks are saved in a `tasks.json` file using the following format:
```json
[
  {
    "id": 1,
    "description": "Example task",
    "status": "todo",
    "createdAt": "2025-08-05 12:30",
    "updatedAt": "2025-08-05 12:30"
  }
]
```

---

## 🔖 Versioning

This project follows [Semantic Versioning](https://semver.org/). See the [Releases](https://github.com/<your-username>/task-cli/releases) page for available versions.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## ✨ Future Improvements (Planned)

- Task priorities
- Due dates & deadlines
- Search & filter by keyword
- Export to CSV
- Reminder notifications

---

## 👤 Author

**Your Name** — [@MN-2410-CTTA](https://github.com/MN-2410-CTTA)

Feel free to submit issues or contribute!
