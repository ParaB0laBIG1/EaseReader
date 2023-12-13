from flet import *
from ui.AppbarUi import AppBarUI
from ui.main_window import MainWindow
from scr.book_manager import draw_book


def main(page: Page):
    # window settings

    page.window_width = 800
    page.window_height = 600
    page.window_center()
    page.title = "EaseReader"

    appbar = AppBarUI(page=page)
    app = MainWindow(page=page)

    page.appbar = appbar.appbarui
    page.add(app.build())
    draw_book(app)

    page.update()


if __name__ == '__main__':
    from scr.config_manager import ConfigManager
    config = ConfigManager(page=Page)

    config.check_config_file()
    app(target=main)
    