from fastapi import FastAPI
from pydantic import BaseModel
from aggregation import aggregate


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.post("/aggr/")
def aggr(item: Item):
    return aggregate(item.text)
