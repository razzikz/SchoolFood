import flet as ft
import json
import requests

def main(page: ft.Page):
    global product_rows_list
    page.title = "Школьная еда | каталог"
    page.bgcolor = "#F0F8E0"

    green = "#4CAF50"
    darker_green = "#388E3C"
    white = "#FFFFFF"

    search_bar = ft.Container(
        bgcolor=green,
        border_radius=30,
        padding=ft.padding.only(left=20, right=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.TextField(
                    hint_text="Поиск...",
                    color=white,
                    border=ft.InputBorder.NONE,
                    label_style=ft.TextStyle(color=white),
                    hint_style=ft.TextStyle(
                        color="#594747",
                        weight=ft.FontWeight.BOLD
                    ),
                ),
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    icon_color="#594747",
                    icon_size=20,
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(0)
                    )
                ),
            ]
        ),
    )

    tabs_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.TextButton(
                content=ft.Text("Готовые блюда", color=darker_green, weight=ft.FontWeight.BOLD),
                style=ft.ButtonStyle(padding=ft.padding.all(10))
            ),
            ft.TextButton(
                content=ft.Text("Продукты", color="#8D8D8D"),
                style=ft.ButtonStyle(padding=ft.padding.all(10))
            ),
        ]
    )

    active_tab_indicator = ft.Container(
        bgcolor=green,
        height=2,
        width=80,
        margin=ft.margin.only(top=-5),
        alignment=ft.alignment.center
    )

    out = requests.get(url="http://127.0.0.1:8000/all_products/").json()
    def create_product_card(recommendation_text, recommendation_color, arr):
        return ft.Container(
            width=160,
            height=180,
            bgcolor=white,
            border_radius=10,
            padding=ft.padding.all(15),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Text(arr, color=darker_green, size=12),
                    ft.Container(height=10),
                    ft.Text(
                        recommendation_text,
                        color=recommendation_color,
                        weight=ft.FontWeight.BOLD,
                        size=14
                    ),
                ]
            )
        )

    product_rows_list = []
    products = out["products"]
    for i in range(0, len(products), 2):
        row_controls = [create_product_card("Рекомендовано", green, products[i]["name"])]
        if i + 1 < len(products):
            row_controls.append(create_product_card("Рекомендовано", green, products[i+1]["name"]))

        product_rows_list.append(ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=row_controls
        ))

    products_list_view = ft.ListView(
        controls=product_rows_list,
        height= 180 * 3 + 20 * 2,
        width=400,
        spacing=20,
        padding=ft.padding.symmetric(horizontal=10)
    )


    bottom_nav_bar = ft.Container(
        bgcolor=green,
        height=60,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(
                    icon=ft.icons.GRID_VIEW,
                    icon_color=white,
                    icon_size=30,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
                ft.IconButton(
                    icon=ft.icons.HOME_OUTLINED,
                    icon_color=white,
                    icon_size=30,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
                ft.IconButton(
                    icon=ft.icons.PERSON_OUTLINE,
                    icon_color=white,
                    icon_size=30,
                    style=ft.ButtonStyle(padding=ft.padding.all(0))
                ),
            ]
        )
    )

    page.add(
        ft.Column(
            controls=[
                search_bar,
                ft.Container(height=20),
                tabs_row,
                active_tab_indicator,
                ft.Container(height=20),
                products_list_view,
                ft.Container(),
                bottom_nav_bar,
            ],
            width=400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port =52)