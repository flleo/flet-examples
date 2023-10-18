import colorsys

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Ruta inicial: {page.route}", color=ft.colors.WHITE54))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Nueva ruta: {e.route}", color=ft.colors.WHITE))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.bgcolor = ft.colors.BROWN_500
    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Ve a la Tienda", on_click=go_store))



ft.app(target=main, view=ft.AppView.WEB_BROWSER)