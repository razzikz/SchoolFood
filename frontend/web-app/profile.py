import flet as ft

import requests


def main(page: ft.Page):
    page.title = "Школьная еда | Профиль"
    page.bgcolor = "#F0F8E0"


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=53)
