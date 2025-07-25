# 📝 To-Do List App (Python + PostgreSQL)
A simple command-line To-Do List application built with Python and PostgreSQL for persistent storage. This project demonstrates clean modular structure and interaction with a relational database using psycopg2.

## 📂 Project Structure
todo-app/
├── app.py            # Main CLI interface for the to-do application
├── db.py             # Database connection and initialization logic
├── todo.py           # Core functionality: add, list, complete, delete tasks
└── requirements.txt  # Python dependencies

## 🚀 Features
- Add new to-do tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Persistent PostgreSQL storage
- Clean modular code for easy extension

## 🧪 Setup Instructions
1. Clone the repository

```
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

2. Create a PostgreSQL database
```
CREATE DATABASE todo_db;
```
3. Configure environment variables
Create a .env file with the following:
```
DB_NAME=todo_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run the app
```
python app.py
```
