from fastapi import FastAPI
import psycopg
import os

app = FastAPI()

@app.get("/query")
def query(q: str):
    # Load credentials from environment variables
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")

    # Connect to PostgreSQL
    conn = psycopg.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_pass
    )

    cur = conn.cursor()
    cur.execute(q)
    data = cur.fetchall()

    cur.close()
    conn.close()

    return {"result": data}
