import flet as ft
import json
import requests

def main(page: ft.Page):
    global product_rows_list
    page.title = "Школьная еда | каталог"
    page.bgcolor = "#F0F8E0"
    page.padding = 0

    green = "#4CAF50"
    darker_green = "#388E3C"
    white = "#FFFFFF"

    search_bar_content = ft.Container(
        height=40,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    hint_text="Поиск...",
                    content_padding=ft.padding.all(5),
                    color="#594747",
                    border_color="transparent",
                    border_radius=20,
                    label_style=ft.TextStyle(color="#594747"),
                    hint_style=ft.TextStyle(
                        color="#8D8D8D",
                        weight=ft.FontWeight.BOLD
                    ),
                    expand=True,
                    border=ft.InputBorder.OUTLINE,
                ),
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    icon_color="#594747",
                    icon_size=20,
                ),
            ]
        ),
        bgcolor="#F3DEC9",
        border=ft.border.all(1, "#594747"),
        border_radius=20,
        padding=ft.padding.all(5),
        expand=False,
    )

    search_bar = ft.Container(
        content=search_bar_content,
        padding=ft.padding.only(left=20, right=20, top=20),
        expand=False,
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
        ],
        expand=False,
    )

    active_tab_indicator = ft.Container(
        bgcolor=green,
        height=2,
        width=80,
        margin=ft.margin.only(top=-5),
        alignment=ft.alignment.center
    )

    dialog = ft.AlertDialog(
        modal=True,
        open=False,
        title=ft.Text("Информация о продукте"),
        content=ft.Text("Здесь будет информация о продукте"),
        actions=[
            ft.TextButton("Закрыть", on_click=lambda e: close_dlg(e, page))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(dialog)

    background_container = None

    def close_dlg(e, page):
        nonlocal background_container
        dialog.open = False
        if background_container in page.overlay:
            page.overlay.remove(background_container)
        background_container = None
        page.update()

    def open_dlg(e, page, id_):
        nonlocal background_container
        dialog.open = True
        background_container = ft.Container(
            bgcolor=ft.colors.BLACK54,
            width=page.width,
            height=page.height,
        )
        page.overlay.append(background_container)
        page.update()
        dialog.update()


    out = requests.get(url="http://127.0.0.1:8000/all_products/").json()
    def create_product_card(arr, id_):
        return ft.TextButton(
            on_click=lambda e: open_dlg(e, page, id_),
            style=ft.ButtonStyle(
                padding=ft.padding.all(0),
                bgcolor=white,
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            content=ft.Container(
                width=160,
                height=180,
                bgcolor=None,
                border_radius=10,
                padding=ft.padding.all(15),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text(arr, color=darker_green, size=12),
                        ft.Container(height=10),
                    ]
                ),
            ),
            data=id_
        )

    product_rows_list = []
    products = out["products"]
    for i in range(0, len(products), 2):
        row_controls = [create_product_card(products[i]["name"], i)]
        if i + 1 < len(products):
            row_controls.append(create_product_card(products[i+1]["name"], i+1))

        product_rows_list.append(ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=row_controls,
            expand=True,
        ))

    products_list_view = ft.ListView(
        controls=product_rows_list,
        spacing=20,
        padding=ft.padding.symmetric(horizontal=10),
        expand=True,
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

    page.dialog = dialog
    page.add(
        ft.Column(
            controls=[
                search_bar,
                ft.Container(height=10),
                tabs_row,
                active_tab_indicator,
                ft.Container(height=10),
                products_list_view,
                bottom_nav_bar,
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port =52)