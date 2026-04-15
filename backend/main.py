from fastapi import FastAPI
from router import route_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Business Assistant Running"}

@app.post("/process")
def process(input_text: str):
    result = route_task(input_text)
    return {"response": result}