import sqlite3
import json

from typing import Union


def check_registration(tg_id: str) -> Union[bool, None]:
    connection = sqlite3.connect("database/users.db")
    cur = connection.cursor()

    try:
        answer = cur.execute(
            """
            SELECT tg_id FROM users WHERE tg_id=?
            """,
            (tg_id, )
        ).fetchone()

        if answer is not None:
            return True
        else:
            return False

    except sqlite3.Error:

        return None

    finally:
        connection.close()


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

        return True

    except sqlite3.Error:
        return False

    finally:
        connection.commit()
        connection.close()


def product_information(id: int) -> Union[dict, None]:
    connection = sqlite3.connect("database/food.db")
    cur = connection.cursor()

    try:
        food = cur.execute(
            """
            SELECT * FROM food WHERE id = ?
            """,
            (id, )
        ).fetchone()

        return food

    except sqlite3.Error:
        return None

    finally:
        connection.close()


def all_products() -> Union[json, None]:
    connection = sqlite3.connect("database/food.db")
    cur = connection.cursor()

    try:
        products = cur.execute(
            """
            SELECT * FROM food
            """
        ).fetchall()

        answer = [
            {
                "id": item[0],
                "name": item[1],
                "weight": item[2],
                "protein": item[3],
                "fat": item[4],
                "carbohydrates": item[5],
                "calories": item[6]
            }
            for item in products
        ]

        answer = json.dumps(answer, ensure_ascii=False, indent=4)

        return answer

    except sqlite3.Error:
        return None

    finally:
        connection.close()


def add_food_to_basket(user_id: str, product_id: int) -> bool:
    connection = sqlite3.connect("database/basket.db")
    cur = connection.cursor()

    try:
        count = cur.execute(
            """
            SELECT count FROM basket WHERE user_id = ? AND product_id = ?
            """,
            (user_id, product_id)
        ).fetchone()

        if count:
            cur.execute(
                """
                UPDATE basket SET count = ? WHERE user_id = ? AND product_id = ?
                """,
                (count[0] + 1, user_id, product_id)
            )

        else:
            cur.execute(
                """
                INSERT INTO basket (user_id, product_id, count)
                VALUES (?, ?, ?)
                """,
                (user_id, product_id, 1)
            )

        return True

    except sqlite3.Error as e:
        print(e)
        return False

    finally:
        connection.commit()
        connection.close()


def get_basket_from_user(user_id: str) -> Union[json, None]:
    connection = sqlite3.connect("database/basket.db")
    cur = connection.cursor()

    try:
        basket = cur.execute(
            """
            SELECT product_id, count FROM basket WHERE user_id = ?
            """,
            (user_id, )
        ).fetchall()

        data = [
            {
                "product_id": item[0],
                "count": item[1]
            }

            for item in basket
        ]

        data = json.dumps(data, ensure_ascii=False, indent=4)

        return data

    except sqlite3.Error:
        return None

    finally:
        connection.close()


def user_data(user_id: str) -> Union[json, None]:
    connection = sqlite3.connect("database/users.db")
    cur = connection.cursor()

    try:
        data = cur.execute(
            """
            SELECT * FROM users WHERE tg_id=?
            """,
            (user_id,)
        ).fetchone()

        return data

    except sqlite3.Error as e:

        print(e)

        return None

    finally:
        connection.close()