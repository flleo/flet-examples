import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Desplegable con valor: {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Entrega", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Azul")
        ],
    )

    page.window_width = 400
    page.window_height = 400
    page.update()

    page.add(color_dropdown, submit_btn, output_text)




ft.app(target=main)