from pydantic import BaseModel
from typing import Union


class Registration(BaseModel):
    tg_id: str
    sex: str
    height: Union[int, float] = int
    weight: Union[int, float] = int
    age: int
    diabetes: bool
    name: str
