from os import getenv
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

db_pool = pool.SimpleConnectionPool(minconn=1, maxconn=10, dsn=getenv("DATABASE_URL"))


def get_db_connection():
    try:
        connection = db_pool.getconn()
        return connection
    except Exception as e:
        raise Exception(f"Error getting db connection: {e}")


def release_db_connection(connection):
    try:
        db_pool.putconn(connection)
    except Exception as e:
        raise Exception(f"Error releasing db connection: {e}")


def close_db_pool():
    if db_pool:
        db_pool.closeall()
