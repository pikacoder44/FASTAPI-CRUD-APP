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
