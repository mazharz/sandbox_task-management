from app import bootstrap_app
from app.db.database import close_db_pool

app = bootstrap_app()

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        close_db_pool()
