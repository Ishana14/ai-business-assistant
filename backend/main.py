# from fastapi import FastAPI
# from router import route_task

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "AI Business Assistant Running"}

# @app.post("/process")
# def process(input_text: str):
#     result = route_task(input_text)
#     return {"response": result}



# from pydantic import BaseModel


from fastapi import FastAPI
from pydantic import BaseModel
from router import route_task

app = FastAPI()

class UserInput(BaseModel):
    input_text: str

@app.get("/")
def home():
    return {"message": "AI Assistant Running"}

@app.post("/process")
def process(data: UserInput):
    result = route_task(data.input_text)
    return {"response": result}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


