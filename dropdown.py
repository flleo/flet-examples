import random

import flet as ft


def main(page):
    page.window_width = 400
    page.window_height = 400

    def button_clicked(e):
        salid = "Desplegable con valor: "
        output_text.value = f"{salid}{color_dropdown.value}"
        output_text.color = color_dropdown.value
        page.update()

    def on_change(e):
        color = random.choices(range(256), k=3)
        print(f'on_change-color: {color}')
        e.color = color
        page.update()

    def on_blur(e):
        color = random.choices(range(256), k=3)
        e.color = color
        print(f'on_blur-color: {color}')
        page.update()

    def on_focus(e):
        color = random.choices(range(256), k=3)
        e.color = color
        print(f'on_focus-color: {color}')
        page.update()

    color_dropdown = ft.Dropdown(
        alignment=ft.alignment.center,
        autofocus=True,
        bgcolor=ft.colors.AMBER_ACCENT,
        border_color=ft.colors.GREY_300,
        border_radius=25,
        border_width=5,
        border=ft.border.only(right=ft.colors.GREEN),
        color=ft.colors.RED,
        content_padding=50,
        counter_style=ft.TextStyle(decoration_color=ft.colors.AMBER_ACCENT_700, bgcolor=ft.colors.RED),
        counter_text='contador red',
        dense=True,  # Si TextField es parte de una forma densa (es decir, utiliza menos espacio vertical).
        error_text='Error brown',
        error_style=ft.TextStyle(italic=True, color=ft.colors.BROWN),
        filled=True,
        focused_color=ft.colors.CYAN_ACCENT_400,
        focused_bgcolor=ft.colors.RED_ACCENT,
        focused_border_color=ft.colors.CYAN_50,
        focused_border_width=2,
        helper_text='Helper error',
        helper_style=ft.TextStyle(color=ft.colors.ERROR),
        hint_text='hint-text green',
        hint_style=ft.TextStyle(decoration_color='green'),
        icon=ft.icons.BOY,
        label='label bgreen',
        label_style=ft.TextStyle(decoration_color='blue', color='green'),
        on_blur=on_blur,
        on_focus=on_focus,
        on_change=on_change,
        opacity=50,
        options=[
            ft.dropdown.Option("red"),
            ft.dropdown.Option("green"),
            ft.dropdown.Option("blue")
        ],
        prefix_text='prefix_text orange  ',
        prefix_style=ft.TextStyle(decoration_color='orange'),
        prefix_icon=ft.icons.HEIGHT,
        prefix=ft.Text('prefix orange  '),
        suffix_text='  suffix_text blue',
        suffix_style=ft.TextStyle(decoration_color='blue'),
        suffix_icon=ft.icons.NOTIFICATIONS,
        suffix=ft.Text('  suffix blue'),
        text_size=20,
        text_style=ft.TextStyle(decoration_color=ft.colors.CYAN_ACCENT_400, bgcolor=ft.colors.BLUE_900,
                                color=ft.colors.GREEN),
        value='green',
        width=300,
    )

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Entrega", on_click=button_clicked)

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    color_dropdown, submit_btn, output_text
                ]
            )
        )
    )


ft.app(target=main)
