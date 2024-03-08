import flet as ft


def main(page):
    first_name = ft.Ref[ft.TextField(value='puta', color=ft.colors.RED)]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()
    # first_name.current.value = "ostia"
    page.update()
    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        # ft.Column(ref=greetings),
        ft.Text(ref=first_name)
    )


ft.app(target=main)
