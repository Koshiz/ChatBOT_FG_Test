from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float = 20.1
    is_offer: Union[bool, None] = None
    
class Numbers(BaseModel):
    name: str
    first_number: int = 20
    second_number: int = 30
    summation: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}

@app.post("/numbers/{number_id}")
def post_numbers(fnumber_id: int, snumber_id: int):
    return {"First Number" : fnumber_id, "Second Number" : snumber_id}

@app.post("/numbers/{number_ids}")
def sum_numbers(fnumber_id : int, snumber_id : int, numbers : Numbers):
    return {"Summation of numbers": fnumber_id + snumber_id, "Second Num from class": numbers.second_number }





    