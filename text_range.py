import time

import flet as ft


def main(page: ft.Page):
    hola = ft.Text(value="Hola, mundo!")
    page.add(hola)

    t = ft.Text()
    page.add(t)
    for i in range(3):
        t.value = f"Comenzamos, en: {i+1}"
        page.update()
        time.sleep(1)

    def button_clicked(e):
        page.add(ft.Text("Clickeado!"))

    but = ft.ElevatedButton(text="Clickeame", on_click=button_clicked)
    page.add(but)

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))



ft.app(target=main)
