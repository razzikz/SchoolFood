from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model import Registration, AddProduct
from connection import *


app = FastAPI()


@app.post("/register/")
async def registration(data: Registration) -> JSONResponse:
    answer = add_user(
        tg_id=data.tg_id,
        age=data.age,
        sex=data.sex,
        diabetes=data.diabetes,
        height=data.height,
        weight=data.weight,
        name=data.name
    )

    if answer:
        return JSONResponse({
            "register": "Success",
            "name": data.name,
            "age": data.age,
            "sex": data.sex,
            "diabetes": data.diabetes,
            "height": data.height,
            "weight": data.weight
        })
    else:
        return JSONResponse({
            "register": "Error"
        })


@app.get("/product_info/{product_id}")
async def product_info(product_id: int) -> JSONResponse:

    food = product_information(id=product_id)

    if food is not None:
        return JSONResponse({
            "food_id": food[0],
            "dish_name": food[1],
            "weight": food[2],
            "protein": food[3],
            "fat": food[4],
            "carbohydrates": food[5],
            "kbzu": food[6]
        })

    else:
        return JSONResponse({
            "info": "Error"
        })


@app.get("/all_products/")
async def full_product() -> JSONResponse:
    res = json.loads(all_products())

    return JSONResponse({
        "products": res
    })


@app.post("/add_product/")
async def add_product(data: AddProduct) -> JSONResponse:
    answer = add_food_to_basket(
        user_id=data.user_id,
        product_id=data.product_id
    )

    if answer:
        return JSONResponse({
            "add": "Success"
        })
    else:
        return JSONResponse({
            "add": "Error"
        })


@app.get("/basket/{user_id}")
async def get_basket(user_id: str) -> JSONResponse:
    get_basket_from_user(user_id)