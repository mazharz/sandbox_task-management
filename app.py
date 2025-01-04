from flask import Flask, request
import psycopg2

app = Flask(__name__)

db_connection = {
    "dbname": "main",
    "user": "postgres",
    "password": "1234",
    "host": "0.0.0.0",
    "port": 5432,
}

db_init_file = "./db/init.sql"


@app.route("/")
def index():
    return {"key": "value"}


@app.post("/db/init")
def db_init():
    try:
        with psycopg2.connect(**db_connection) as conn:
            with conn.cursor() as cursor:
                with open(db_init_file, "r") as file:
                    sql_script = file.read()
                cursor.execute(sql_script)
            conn.commit()
            return {
                "success": True,
                "message": "Database was initialized successfully!",
            }
    except Exception as e:
        app.logger.error(e)
        return {"success": False}


@app.post("/task")
def create_task():
    task_name = request.get_json()["name"]
    try:
        with psycopg2.connect(**db_connection) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO tasks (name) VALUES ('{task_name}')")
            conn.commit()
            return {
                "success": True,
                "message": f"Task with name {task_name} was created successfully!",
            }
    except Exception as e:
        app.logger.error(e)
        return {"success": False}


@app.get("/task/<name>")
def get_task(name):
    try:
        with psycopg2.connect(**db_connection) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM tasks WHERE name='{name}'")
                result = cursor.fetchall()
            conn.commit()
            return {
                "success": True,
                "name": result[0][0],
            }
    except Exception as e:
        app.logger.error(e)
        return {"success": False}
