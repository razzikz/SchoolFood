import sqlite3

from typing import Union

from model import Registration


def add_user(tg_id: str, sex: str, age: int, diabetes: bool, name: str, height: Union[int, float] = int,
             weight: Union[int, float] = int) -> bool:
    connection = sqlite3.connect("database/users.db")
    cur = connection.cursor()

    try:
        cur.execute(
            """
            INSERT INTO users (tg_id, sex, height, weight, age, diabetes, name)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (tg_id, sex, height, weight, age, diabetes, name)
        )

        connection.commit()
        connection.close()

        return True
    except sqlite3.Error:
        connection.commit()
        connection.close()

        return False
