import psycopg2

conn = psycopg2.connect(
    dbname="todo_db",
    user="postgres",
    password="Temidayo24",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def init_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE
        )
    """)
    conn.commit()
