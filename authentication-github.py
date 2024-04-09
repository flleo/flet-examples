
import os

import flet as ft
from flet.auth.providers import GitHubOAuthProvider
#
# GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
# assert GITHUB_CLIENT_ID, "set GITHUB_CLIENT_ID environment variable"
# GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
# assert GITHUB_CLIENT_SECRET, "set GITHUB_CLIENT_SECRET environment variable"
GITHUB_CLIENT_ID='d3657e81a96a98b8281c'
GITHUB_CLIENT_SECRET='12ec9ffa98b1a4b0c68d89cdf007ce9ebaca1537'


def main(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    print(f"FLET_SECRET_KEY: {os.environ['FLET_SECRET_KEY']}")

    def login_click(e):
        page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)