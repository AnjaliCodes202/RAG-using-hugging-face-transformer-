from fastapi import FastAPI
import os

print("🔥 LOADED test_api.py FROM:", os.path.abspath(__file__))

app = FastAPI()

@app.get("/ping")
def ping():
    return {"msg": "pong"}
