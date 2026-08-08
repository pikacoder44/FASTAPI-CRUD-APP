# Assignment of FlyRankAI
## Basic CRUD Setup in FastAPI

## Swagger UI
![Swagger UI](/Swagger%20UI%201.png)

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pikacoder44/FASTAPI-CRUD-APP.git
   ```
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```


## Learn SQL by Hand

For this task, I used **DB Browser for SQLite** to directly interact with the `tasks.db` database created by the FastAPI application.

### SQL Query

```sql
UPDATE tasks SET done = 1;
```

### Result

This query marked every task in the `tasks` table as completed. The change was immediately reflected in the FastAPI `GET /tasks` endpoint without restarting the server, confirming that both DB Browser and the API use the same SQLite database as the single source of truth.

### Other Queries Tested

```sql
SELECT * FROM tasks;
SELECT * FROM tasks WHERE done = 1;
SELECT COUNT(*) FROM tasks;
DELETE FROM tasks WHERE done = 1;
```


# Assignment 4 — SQLite Task API

A FastAPI task management API backed by SQLite.

## Why SQLite?

SQLite was chosen because it provides:

* **Single file** — the entire database is stored in one file.
* **Zero setup** — no separate database server is required.
* **Persistence** — data survives application restarts.
* **Easy development** — Python includes SQLite through its built-in `sqlite3` module.

## Database

The database file is:

```text
tasks.db
```

It is created automatically in the project directory when the application starts.

The `tasks` table is also created automatically if it does not already exist. If the table is empty, three example tasks are inserted automatically.

The database file is normally git-ignored so that each fresh clone creates its own database.

## How to Run

Create and activate the virtual environment, install the dependencies, and start the server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Database Screenshot

The SQLite database was opened using **DB Browser for SQLite**.

![Database in DB Browser](screenshots/database-browser.png)

## Example SQL Query

The following query was executed directly in DB Browser for SQLite:

```sql
UPDATE tasks SET done = 1;
```

This query marked every task as completed. The change was immediately reflected by the FastAPI `GET /tasks` endpoint without restarting the server.

## Automatic Database Setup

No manual database setup is required.

On a fresh clone, starting the application automatically:

1. Creates `tasks.db`.
2. Creates the `tasks` table.
3. Checks whether the table is empty.
4. Inserts three example tasks if the table is empty.

Therefore, a fresh clone can be started with the documented command and immediately accessed through:

```text
GET /tasks
```

The API returns the three seeded example tasks.
