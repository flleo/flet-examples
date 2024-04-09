import flet as ft
from flet_core import FilePickerUploadFile


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Selección cancelada"
        )
        selected_files.update()

    file_picker = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(file_picker)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Selecciona fotos",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: file_picker.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )

    def upload_files(e):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)

    upload_files()


ft.app(target=main, view=ft.AppView.WEB_BROWSER)

