from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

item_master = {1 : "Description for item 1",
               2 : "Description for item 2",
               3 : "Description for item 3",
               4 : "Description for item 4",
               5 : "Description for item 5",
}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# We get app from fastAPI, get function gets home directory
# tells that below code should be displayed on home page
# To get documentation of end points we need to give "../docs" in our URL 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Creating a new end-point in API or URL
# No. of end points = No. of functions
@app.get("/items")
async def items():
    #return {"items": "Here are list of Items"}
    return {"items": item_master}

@app.get("/items/{item_id}")
async def get_item(item_id: int, short: bool = False):
    if short == True: 
        return {"item": item_master[item_id] }
    else:  
        {"item": "This is a long description" }  

# CRUD operations can be performed

@app.post("/items")
async def create_item(item: Item):
    return item.name