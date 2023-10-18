import flet as ft

def main(page):
    def checkbox_changed(e):
        output_text.value = (
            f"Has aprendido cómo esquiar : {todo_check.value}."
        )
        page.update()
    output_text = ft.Text()
    todo_check = ft.Checkbox(label="Hacer: Aprender cómo usar los esquis", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

ft.app(target=main)