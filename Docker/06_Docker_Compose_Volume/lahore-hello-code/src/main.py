from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Multiple MicroservicesCool Just Added Volume. And testing volume!!": "5 MAY"}
