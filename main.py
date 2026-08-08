import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI()
DATABASE = "tasks.db"


def get_db():
    return sqlite3.connect(DATABASE)


def init_db():
    db = get_db()
    cursor = db.cursor()

    # Create tasks table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            done BOOLEAN
        )
        """)

    # Check how many tasks already exist in the database
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    # Seed only if the table is empty
    if count == 0:
        # Seed the database with initial tasks
        initial_tasks = [
            ("Learn FastAPI", False),
            ("Build a simple API", True),
            ("Deploy the API", False),
        ]
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)", initial_tasks
        )
        db.commit()
        db.close()


init_db()

tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": True},
    {"id": 3, "title": "Task 3", "done": False},
    {"id": 4, "title": "Task 4", "done": False},
    {"id": 5, "title": "Task 5", "done": False},
]


@app.get("/", description="Root endpoint that provides basic information about the API")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health", description="Health check endpoint")
async def health():
    return {"status": "ok"}


@app.get("/tasks", description="Get all tasks")
async def get_tasks():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    db.close()

    return [{"id": task[0], "title": task[1], "done": bool(task[2])} for task in tasks]


@app.get("/tasks/{id}", description="Get a task by its ID")
async def get_task_from_id(id: int):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    task = cursor.fetchone()

    db.close()

    if task:
        return {"id": task[0], "title": task[1], "done": bool(task[2])}
    raise HTTPException(status_code=404, detail={"error": "Task not found"})


@app.post("/tasks", status_code=201, description="Create a new task")
async def create_task(task: dict):
    if "title" not in task or not task["title"].strip():
        raise HTTPException(status_code=400, detail="Task must have a title")
    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (task["title"], 0))

    # Get the ID assigned by SQlite
    task_id = cursor.lastrowid

    db.commit()
    db.close()

    return {"id": task_id, "title": task["title"], "done": False}


@app.put("/tasks/{id}", description="Update a task by its ID")
async def update_task(id: int, task: dict):
    if "title" not in task and "done" not in task:
        raise HTTPException(
            status_code=400, detail="Task must have a title or done status"
        )
    for existing_task in tasks:
        if existing_task["id"] == id:
            existing_task.update(task)
            return {
                "message": f"Task {id} updated successfully",
                "data": existing_task,
            }
    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@app.delete("/tasks/{id}", description="Delete a task by its ID")
async def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": f"Task {id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Task {id} not found")
