from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model import Registration
from connection import add_user


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
