from contextlib import contextmanager
from app.db.database import get_db_connection, release_db_connection


@contextmanager
def get_db_cursor():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        release_db_connection(connection)
