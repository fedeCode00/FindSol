import flet as ft
from flet import *


def main(page: ft.Page ):
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, bgcolor="#191970"
    )

    page.adaptive = True
    page.bgcolor = "white"

    # page.appbar = ft.AppBar( 
    #     title=ft.Text("APP"),
    #     leading_width=50,
    #     center_title=False,
    #     bgcolor= "#191970", 
    # )


    # page.add(
    #     ft.SafeArea( 
    #         ft.Column(
    #             [
                    
    #             ]
    #         )
    #     ),
    #    page.appbar
    # )

    def route_change(e: RouteChangeEvent):
        page.views.clear()

        page.views.append(
            View(
                 route='/',
                 appbar= ft.AppBar(
                      title=ft.Text("APP"),
                  leading_width=50,
                  center_title=False,
                  bgcolor= "#191970",    
                 ),
                 drawer=ft.NavigationDrawer(
                      bgcolor="#191970",
                      controls=[
                           ft.Container(height=12),
                           ft.Container(content=ft.Text("FastOperation",weight=ft.FontWeight.BOLD, size=15),padding=20),
                           ft.Divider(thickness=2),
                           ft.ExpansionTile(
                                title=ft.Text("Equazioni"),
                                affinity=ft.TileAffinity.PLATFORM,
                                maintain_state=False,
                                collapsed_text_color=ft.colors.WHITE,
                                text_color=ft.colors.WHITE,
                                controls=[
                                     ft.ListTile(
                                        title=ft.TextButton(
                                            "Primo Grado", 
                                            on_click=lambda _:page.go('/first'),
                                            data=0
                                            )
                                        ),
                                    ft.ListTile(
                                        title=ft.TextButton(
                                            "Secondo Grado", 
                                            on_click=lambda _:page.go('/first'),
                                            data=0
                                            )
                                        ),
                                    ],
                                bgcolor="#191970"
                           ),
                           ft.ExpansionTile(
                                title=ft.Text("Disequazioni"),
                                affinity=ft.TileAffinity.PLATFORM,
                                maintain_state=False,
                                collapsed_text_color=ft.colors.WHITE,
                                text_color=ft.colors.WHITE,
                                bgcolor="#556ad0",
                                controls=[
                                     ft.ListTile(
                                        title=ft.TextButton(
                                            "Primo Grado", 
                                            on_click=lambda _:page.go('/first'),
                                            data=0
                                            ),
                                        ),
                                    ft.ListTile(
                                        title=ft.TextButton(
                                            "Secondo Grado", 
                                            on_click=lambda _:page.go('/first'),
                                            data=0
                                            ),
                                        ),
                                    ],
                           )
                      ]
                 )
            )
        )           
                

        if page.route == '/first':
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
        
        page.update()
    
    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
        ft.app(target=main)