
from fastapi import FastAPI

# poetry run uvicorn main:app --reload

app = FastAPI()




@app.get('/')
def index():
    return {"greetings":"hello world from talha"}


@app.get('/hello')
def hello():
    return {"greetings":"Assalam u Alaikum from FASTAPI"}
