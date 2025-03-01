import flet as ft
import requests

dark_green = "#2B7834"
orange = "#EC7A2E"
light_green = "#EAF1CB"
white = "#FFFFFF"


def main(page: ft.Page):
    page.title = "Школьная еда | Регистрация"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.bgcolor = light_green
    page.theme = ft.Theme(font_family="Inter")

    registration_text = ft.Text(
        value="Регистрация",
        size=30,
        color=dark_green,
        weight=ft.FontWeight.BOLD
    )

    gender_text = ft.Text(
        value="Ваш пол:",
        size=20,
        color=dark_green,
        weight=ft.FontWeight.BOLD
    )

    diabetes_text = ft.Text(
        value="Наличие диабета:",
        size=20,
        color=dark_green,
        weight=ft.FontWeight.BOLD
    )

    selected_gender = ft.Ref[str]()
    selected_gender.current = "Мужской"

    selected_diabetes = ft.Ref[str]()
    selected_diabetes.current = "Нет"

    def update_gender_style(gender):
        male_button.style = ft.ButtonStyle(
            bgcolor=dark_green if gender == "Мужской" else white,
            color=white if gender == "Мужской" else dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        )
        female_button.style = ft.ButtonStyle(
            bgcolor=dark_green if gender == "Женский" else white,
            color=white if gender == "Женский" else dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        )
        page.update()

    def update_diabetes_style(diabetes):
        diabetes_yes_button.style = ft.ButtonStyle(
            bgcolor=dark_green if diabetes == "Есть" else white,
            color=white if diabetes == "Есть" else dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        )
        diabetes_no_button.style = ft.ButtonStyle(
            bgcolor=dark_green if diabetes == "Нет" else white,
            color=white if diabetes == "Нет" else dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        )
        page.update()

    def male_clicked(e):
        selected_gender.current = "Мужской"
        update_gender_style("Мужской")

    def female_clicked(e):
        selected_gender.current = "Женский"
        update_gender_style("Женский")

    def diabetes_yes_clicked(e):
        selected_diabetes.current = "Есть"
        update_diabetes_style("Есть")

    def diabetes_no_clicked(e):
        selected_diabetes.current = "Нет"
        update_diabetes_style("Нет")

    def register_clicked(e):
        user_id = str(page.query.page.route)[10:]

        data = {
            "tg_id": user_id,
            "sex": selected_gender.current,
            "height": height_field.value,
            "weight": weight_field.value,
            "age": age_field.value,
            "diabetes": True if selected_diabetes.current == "Есть" else False,
            "name": "Имя"
        }

        dialog = ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=10),
            actions=[ft.TextButton("Закрыть", on_click=lambda e: page.close(dialog))],
        )
        if data_validity(data["height"], data["weight"], data["age"]):
            try:
                response = requests.post(url="http://127.0.0.1:8000/register/", json=data)

                if response.status_code == 200:
                    dialog.title = ft.Text("Успех!")
                    dialog.content = ft.Text("Успешная регистрация!")
                else:
                    dialog.title = ft.Text("Ошибка!")
                    dialog.content = ft.Text("Неправильный ввод данных!")

            except requests.exceptions.RequestException as e:
                dialog.title = ft.Text("Ошибка!")
                dialog.content = ft.Text("Неправильный ввод данных!")

        else:
            dialog.title = ft.Text("Ошибка!")
            dialog.content = ft.Text("Неправильный ввод данных!")
        page.open(dialog)

    def data_validity(height, weight, age) -> bool:
        try:
            if height is not None and not (1 <= int(height) <= 300):
                return False
            if weight is not None and not (1 <= int(weight) <= 300):
                return False
            if age is not None and not (1 <= int(age) <= 150):
                return False
        except (TypeError, ValueError):
            return False
        return True

    male_button = ft.ElevatedButton(
        text="Мужской",
        on_click=male_clicked,
        style=ft.ButtonStyle(
            bgcolor=dark_green,
            color=white,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        height=40,
        width=130,
    )

    female_button = ft.ElevatedButton(
        text="Женский",
        on_click=female_clicked,
        style=ft.ButtonStyle(
            bgcolor=white,
            color=dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        height=40,
        width=130,
    )

    diabetes_yes_button = ft.ElevatedButton(
        text="Есть",
        on_click=diabetes_yes_clicked,
        style=ft.ButtonStyle(
            bgcolor=white,
            color=dark_green,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        height=40,
        width=130,
    )

    diabetes_no_button = ft.ElevatedButton(
        text="Нет",
        on_click=diabetes_no_clicked,
        style=ft.ButtonStyle(
            bgcolor=dark_green,
            color=white,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        height=40,
        width=130,
    )

    age_field = ft.TextField(
        label="Ваш возраст",
        width=200,
        height=40,
        border_color=dark_green,
        color=dark_green,
        label_style=ft.TextStyle(color="#6c757d"),
        cursor_color="#6c757d",
        border_width=2,
    )

    height_field = ft.TextField(
        label="Ваш рост, см",
        width=200,
        height=40,
        border_color=dark_green,
        color=dark_green,
        label_style=ft.TextStyle(color="#6c757d"),
        cursor_color="#6c757d",
        border_width=2,
    )

    weight_field = ft.TextField(
        label="Ваш вес, кг",
        width=200,
        height=40,
        border_color=dark_green,
        color=dark_green,
        label_style=ft.TextStyle(color="#6c757d"),
        cursor_color="#6c757d",
        border_width=2,
    )

    register_button = ft.ElevatedButton(
        text="Зарегистрироваться",
        on_click=register_clicked,
        style=ft.ButtonStyle(
            bgcolor=dark_green,
            color=white,
            side=ft.BorderSide(width=2, color=dark_green),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        height=50,
        width=200,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[registration_text],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[gender_text],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    controls=[male_button, female_button],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=20,
                ),
                ft.Column(
                    controls=[
                        age_field,
                        height_field,
                        weight_field,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    controls=[diabetes_text],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    controls=[diabetes_yes_button, diabetes_no_button],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=20,
                ),
                ft.Container(height=10),
                ft.Row(
                    controls=[register_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=50)
