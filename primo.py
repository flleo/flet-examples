import flet as ft

HASTA = 1500
DESDE = 1000


def main(page: ft.Page):
    page.title = 'Primos'

    def noes_primo(num):
        valor = ''
        for n in range(2, num):
            if num % n == 0:
                valor += str(num) + " no es primo, " + str(n) + " es divisor" + '\n'
                return valor

    def primo(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    def no_primo(num):
        for n in range(2, num):
            if num % n == 0:
                return n
        return num

    def primos():
        n = DESDE
        _primos = ''
        while n < HASTA:
            n += 1
            if primo(n):
                _primos += str(n) + ' '
        return _primos

    def no_primos():
        n = DESDE
        _no_primos = ''
        while n < HASTA:
            n += 1
            num = no_primo(n)
            if num != n:
                _no_primos += str(n) + '->' + str(n) + '/' + str(num) + '=' + str(int(n / num)) + '\n'
        return _no_primos

    page.add(
        ft.Container(

            content=ft.Column(

                controls=[
                    ft.Row(
                        controls=[ft.Text(
                            'Numeros primos',
                            weight=ft.FontWeight.BOLD
                        )],
                    ),
                    ft.ResponsiveRow(
                        controls=[
                            ft.Text(
                                primos(),
                            )
                        ],
                    ),
                    ft.Row(
                        controls=[ft.Text(
                            'Numeros no primos',
                            weight=ft.FontWeight.BOLD
                        )],
                    ),
                    ft.ResponsiveRow(

                        # height=500,
                        controls=[
                            ft.ListView(
                                controls=[ft.Text(
                                    no_primos(),
                                ),
                                ]
                            )]
                    )]
            )
        )
    )


if __name__ == "__main__":
    ft.app(target=main, port=8090, assets_dir='assets')
