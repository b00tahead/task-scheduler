import sqlite3

DB_PATH = "db/tasks.db"


def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def save_task(name, time, recurring):
    """Insert a new task into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (name, time, recurring) VALUES (?, ?, ?)",
        (name, time, recurring),
    )
    conn.commit()
    conn.close()


def get_all_tasks():
    """Retrieve all tasks from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks
