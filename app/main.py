from typing import Union
from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: int
#     colour: str
#     company: str
#     on_sale: Union[bool, None] = None


app.include_router(auth_router)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")