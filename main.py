from fastapi import FastAPI, HTTPException

app = FastAPI()

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
    return tasks



@app.get("/tasks/{id}", description="Get a task by its ID")
async def get_task_from_id(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")



@app.post("/tasks", status_code=201, description="Create a new task")
async def create_task(task: dict):
    if "title" not in task:
        raise HTTPException(status_code=400, detail="Task must have a title")
    task_id = len(tasks) + 1
    task["id"] = task_id
    task["done"] = False
    tasks.append(task)

    return {
        "message": f"done, here's your receipt",
        "data": task,
    }

@app.put("/tasks/{id}", description="Update a task by its ID")
async def update_task(id: int, task: dict):
    if "title" not in task and "done" not in task:
        raise HTTPException(status_code=400, detail="Task must have a title or done status")
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