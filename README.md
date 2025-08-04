# ✅ Task Tracker CLI

A simple command-line task manager written in Python.

Track your tasks with clean output, simple commands, and no external dependencies.

---

## 🚀 Installation

### 1. Make sure you have Python installed

You can check by running this in your terminal or command prompt:

```bash
python --version
```

If it shows something like `Python 3.10.6`, you're good.
If not, download Python here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2. Download this project

You can:

* Click the green **"Code"** button above and choose **"Download ZIP"**
* Or clone it with Git:

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

---

## 🛠️ How to Use

You run everything from your terminal using this command pattern:

```bash
python task.py <command>
```

### ✅ Add a Task

```bash
python task.py add "Do my homework"
```

This will create a new task with a status of `todo`.

---

### 📋 List All Tasks

```bash
python task.py list
```

Shows all tasks you've added, including their status and timestamps.

---

### 🔍 List Tasks by Status

You can filter your tasks like this:

```bash
python task.py list todo
python task.py list in-progress
python task.py list done
```

This only shows the tasks with that status.

---

## 📁 Where are tasks saved?

Your tasks are saved in a file called `tasks.json` in the same folder.
You don’t need to touch it — the script handles everything for you.

---

## 📌 Current Limitations

* You can't yet update or delete tasks.
* You can't mark a task as done or in-progress yet.
* These features are coming in the next update!

---

## ✨ Coming Soon

* `mark-done`, `mark-in-progress`
* `update`, `delete`, and task ID validation
* Better error messages

---

Made with 💻 and Python by \[Your Name]
