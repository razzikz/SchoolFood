import pandas as pd
import sqlite3

data = pd.read_csv("database/food.csv", delimiter=";")

for i in range(2, len(data.columns)):
    for j in range(len(data)):

        value = data.iloc[j, i]

        if isinstance(value, str):
            value = value.replace(",", ".")
            data.iloc[j, i] = float(value)


connection = sqlite3.connect("database/food.db")
cur = connection.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS food (
        id INTEGER PRIMARY KEY,
        dish_name TEXT NOT NULL,
        weight REAL NOT NULL,
        protein REAL NOT NULL,
        fat REAL NOT NULL,
        carbohydrates REAL NOT NULL,
        kbzu REAL NOT NULL
    )
    """
)

for _, row in data.iterrows():
    cur.execute(
        """
        INSERT INTO food (dish_name, weight, protein, fat, carbohydrates, kbzu)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (row["Блюдо"], row["Выход (гр)"], row["Белки (г)"], row["Жиры (г)"], row["Углеводы (г)"], row["Ккал"])
    )

connection.commit()
connection.close()

connection = sqlite3.connect("database/users.db")
cur = connection.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Users (
        tg_id TEXT PRIMARY KEY,
        sex TEXT NOT NULL,
        name TEXT NOT NULL,
        height INTEGER NOT NULL,
        weight INTEGER NOT NULL,
        age INTEGER NOT NULL,
        diabetes BOOLEAN NOT NULL
    )
    """
)

connection.commit()
connection.close()
