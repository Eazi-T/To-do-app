from db import cur, conn

def add_task(title):
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()

def list_tasks():
    cur.execute("SELECT id, title, completed FROM tasks ORDER BY id")
    return cur.fetchall()

def complete_task(task_id):
    cur.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()

def delete_task(task_id):
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
