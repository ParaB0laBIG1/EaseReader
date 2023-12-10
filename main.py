from flet import *
from ui.AppbarUi import AppBarUI
from ui.main_window import MainWindow
from ui.book_ui import BookUI


def main(page: Page):
    # window settings

    page.window_width = 800
    page.window_height = 600
    page.window_center()
    page.title = "EaseReader"

    appbar = AppBarUI(page=page)
    app = MainWindow(page=page)
    book_ui = BookUI(page=page, main_window=app)

    page.appbar = appbar.appbarui
    page.add(app.build())
    book_ui.draw_book_ui()

    page.update()


if __name__ == '__main__':
    from scr.config_manager import ConfigManager
    config = ConfigManager(page=Page)

    config.check_config_file()
    app(target=main)
    