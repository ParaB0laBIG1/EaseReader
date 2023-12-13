from flet import *


class BookUI(UserControl):
    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.book_ui = Container(
                    alignment=alignment.center,
                    width=350,height=200,
                    bgcolor=colors.BLUE_GREY_700,
                    border_radius=border_radius.all(5)
                )
