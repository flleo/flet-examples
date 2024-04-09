import os

import flet
from flet import ElevatedButton, LoginEvent, Page
from flet.auth.providers import GoogleOAuthProvider



def main(page: Page):
    provider = GoogleOAuthProvider(
        client_id='clientID',
        client_secret='clientSecret',
        redirect_url="http://localhost:8503/api/oauth/redirect",
    )

    def login_button_click(e):
        page.login(provider, scope=['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com'
                                                                                      '/auth/userinfo.profile'])

    def on_login(e: LoginEvent):
        if not e.error:
            toggle_login_buttons()

    def logout_button_click(e):
        page.logout()

    def on_logout(e):
        toggle_login_buttons()

    def toggle_login_buttons():
        login_button.visible = page.auth is None
        logout_button.visible = page.auth is not None
        page.update()

    login_button = ElevatedButton("Login with Google", on_click=login_button_click)
    logout_button = ElevatedButton("Logout", on_click=logout_button_click)
    toggle_login_buttons()
    page.on_login = on_login
    page.on_logout = on_logout
    page.add(login_button, logout_button)


flet.app(target=main, port=8503, view=flet.WEB_BROWSER)



