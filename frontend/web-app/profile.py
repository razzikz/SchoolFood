import urllib.parse

import flet as ft

import requests


def main(page: ft.Page):
    page.title = "Школьная еда | Профиль"
    page.bgcolor = "#F0F8E0"

    green = "#4CAF50"
    darker_green = "#388E3C"
    white = "#FFFFFF"

    name_text = ft.Text(
        value="",
        size=20,
        color=darker_green,
        weight=ft.FontWeight.BOLD
    )
    age_text = ft.Text(
        value="Возраст: ",
        size=20,
        color=darker_green,
        weight=ft.FontWeight.BOLD
    )

    height_text = ft.Text(
        value="Рост: ",
        size=20,
        color=darker_green,
        weight=ft.FontWeight.BOLD
    )

    weight_text = ft.Text(
        value="Вес: ",
        size=20,
        color=darker_green,
        weight=ft.FontWeight.BOLD
    )

    sex_text = ft.Text(
        value="Пол: ",
        size=20,
        color=darker_green,
        weight=ft.FontWeight.BOLD
    )

    bottom_nav_bar = ft.Container(
        bgcolor=green,
        height=50,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(
                    icon=ft.icons.GRID_VIEW,
                    icon_color=white,
                    icon_size=25,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
                ft.IconButton(
                    icon=ft.icons.HOME_OUTLINED,
                    icon_color=white,
                    icon_size=25,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
                ft.IconButton(
                    icon=ft.icons.PERSON_OUTLINE,
                    icon_color=white,
                    icon_size=25,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
            ],
            expand=True,
        ),
    )

    def set_text(e):
        user_data = urllib.parse.unquote(page.query.page.route)
        parsed_url = urllib.parse.parse_qs(user_data.lstrip("/?"))

        user_id = parsed_url.get("user_id", ["unknown"])[0]

        response = requests.get(url=f"http://127.0.0.1:8000/user_info/{user_id}")

        print(response)

    page.add(
        ft.Container(
            ft.Column(
                controls=[
                    name_text,
                    ft.Container(height=10),
                    age_text,
                    ft.Container(height=10),
                    height_text,
                    ft.Container(height=10),
                    weight_text,
                    ft.Container(height=10),
                    sex_text,
                    ft.Container(expand=True),
                    bottom_nav_bar
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START
            ),
            expand=True,
            padding=20
        )
    )

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER, port=55)
