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
    basket = get_basket_from_user(user_id)

    if basket is not None:
        basket = json.loads(basket)

        return JSONResponse({
            "basket": basket
        })

    else:
        return JSONResponse({
            "get": "Error"
        })


@app.get("/check/{user_id}")
async def check(user_id: str) -> JSONResponse:

    answer = check_registration(tg_id=user_id)

    if answer:
        data = user_data(user_id=user_id)

        if data:
            return JSONResponse({
                "login": True,
                "tg_id": data[0],
                "sex": data[1],
                "height": data[3],
                "weight": data[4],
                "age": data[5],
                "diabetes": data[6],
                "name": data[2]
            })

    return JSONResponse({
        "login": False
    })


@app.get("/user_info/{user_id}")
async def user_info(user_id: str) -> JSONResponse:

    data = information_user(user_id=user_id)

    if data is not None:
        return JSONResponse({
            "tg_id": data[0],
            "sex": data[1],
            "height": data[3],
            "weight": data[4],
            "age": data[5],
            "diabetes": data[6],
            "name": data[2]
        })

    else:
        return JSONResponse({
            "info": "Error"
        })