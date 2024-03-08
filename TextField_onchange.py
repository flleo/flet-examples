import flet as ft


def main(page: ft.Page):

    def cambia(e):
        t.value = e.control.value
        page.update()

    t = ft.Text('hla')
    tf = ft.TextField()

    tf.on_change = cambia

    page.add(
        ft.Column(
            controls=[
                tf,
                t
            ],

        )
    )


ft.app(target=main)
