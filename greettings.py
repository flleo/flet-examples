import flet as ft

def main(page):
    first_name = ft.TextField(label="Nombre", autofocus=True)
    last_name = ft.TextField(label="Apellido")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hola, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.title = "Saludos"
    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Di hola!", on_click=btn_click),
        greetings
    )


ft.app(target=main)