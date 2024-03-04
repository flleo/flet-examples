import flet as ft
# Un control que inserta su contenido con suficiente relleno para evitar intrusiones por parte del sistema operativo.
# Por ejemplo, esto sangrará el contenido lo suficiente como para evitar la barra de estado en la parte superior de la
# pantalla. También sangrará el contenido en la cantidad necesaria para evitar The Notch en el iPhone X u otras
# características físicas creativas similares de la pantalla. Cuando se especifica un acolchado mínimo, se aplicará el
# mayor entre el acolchado mínimo o el acolchado del área segura.


class State:
    counter = 0


def main(page: ft.Page):
    state = State()

    def add_click(e):
        state.counter += 1
        _counter.value = str(state.counter)
        _counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                _counter := ft.Text("0", size=50),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
    )


ft.app(main)
