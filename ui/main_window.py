from flet import *


class MainWindow(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = Page

        self.book_row = Row(
                wrap=True,
                spacing=10,
                scroll="auto",
                run_spacing=10,
                alignment=MainAxisAlignment.CENTER,
                width=page.window_width,
            )

        self.main_conatiner = Container(
            width=800,height=460,
            content=self.book_row
        )

    def build(self):
        return self.main_conatiner