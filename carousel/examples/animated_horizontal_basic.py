from flet import *
from fletcarousel import BasicAnimatedHorizontalCarousel, HintLine, AutoCycle


def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.rtl = True
    carousel = BasicAnimatedHorizontalCarousel(
        page=page,
        auto_cycle=AutoCycle(duration=2),
        # expand=True,
        # padding=50,
        hint_lines=HintLine(
            active_color='red',
            inactive_color='white',
            alignment=MainAxisAlignment.CENTER,
            max_list_size=400
        ),
        items=[
            Container(
                content=Image(
                    src=img,
                    # scale=0.7,
                    # height=250
                ),
                height=250,
                border_radius=25,
                alignment=alignment.center,
            ) for img in item.img
        ],
    )
    page.add(carousel)


app(target=main)


