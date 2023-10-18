import flet as ft
from flet import *
from flet_runtime.auth.providers.google_oauth_provider import GoogleOAuthProvider


clientID = "299357998598-r0mrbmvpoec4hjls327o3mbl6btfhu08.apps.googleusercontent.com"
clientSecret = "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"

def main(page:Page):
    provider = GoogleOAuthProvider(
        client_id=clientID,
        client_secret=clientSecret,
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )
    resulttxt = Column()

    def logingoogle(e):
        page.login(provider)

    def on_login(e):
        print(page.auth.user)
        resulttxt.controls.append(
            Column([
                Text(f"nombre: {page.auth.user['name']}"),
                Text(f"email: {page.auth.user['email']}"),
                Text(f"access token: {page.auth.token.access_token}"),
                Text(f"id: {page.auth.user.id}"),
                ])
            )
        page.update()

    page.on_login = on_login

    page.add(
        Column([
            Text("Logeate con  Google", size=30),
            ElevatedButton("Google",
                           bgcolor="blue", color="white",
                           on_click=logingoogle
                        ),
            resulttxt
        ])
    )


ft.app(target=main, port=8550, view=WEB_BROWSER)
