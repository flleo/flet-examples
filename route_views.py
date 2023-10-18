import flet as ft

def main(page: ft.Page):
    page.title = "Rutas"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("App Flet"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Tienda", on_click=lambda _: page.go("/store")),
                ]
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Tienda"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Home", on_click=lambda _: page.go("/"))
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)