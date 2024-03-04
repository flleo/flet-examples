import flet as ft


def main(page: ft.Page):
    page.title = "Badge on a NavigationBar destination icon"
    st = ft.Stack(
        controls=[
            ft.NavigationBar(
                destinations=[
                    ft.NavigationDestination(
                        icon_content=ft.Badge(
                            content=ft.Icon(ft.icons.EXPLORE),
                            small_size=10,
                            text='1'
                        ),
                        label="Explore",
                    ),
                    ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
                    ft.NavigationDestination(
                        icon_content=ft.Badge(content=ft.Icon(ft.icons.PHONE), text="10")
                    ),
                ],
            )
        ]
    )

    page.add(st)
    page.add(ft.Text("Body!"))


ft.app(target=main)
