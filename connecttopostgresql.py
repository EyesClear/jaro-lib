from fastapi import FastAPI
import psycopg2, json

app = FastAPI()

@app.get("/query")
def query(q: str):
    conn = psycopg2.connect(
        host="uat.eyesclear.com",
        port=32444,
        dbname="ec_uat",
        user="copilot_user",
        password="your_password"
    )
    cur = conn.cursor()
    cur.execute(q)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return {"result": data}
