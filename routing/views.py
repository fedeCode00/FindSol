import flet as ft
from flet import *


def main(page: ft.Page):

    page.views.append(
                View(
                    route='/',
                    controls=[
                        ft.AppBar(
                            title=ft.Text(
                                "OK",
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLACK87
                                ),
                            bgcolor=ft.colors.BLUE,
                            center_title=True,
                            actions=[
                                ft.IconButton(ft.icons.MENU, tooltip="OK", on_click=lambda _: page.go('/') ,icon_color=ft.colors.BLACK87)
                            ],
                            color=ft.colors.WHITE
                            )
                        ]
                    )
                )

if __name__ == '__main__':
        ft.app(target=main)