from flet import *
from ui.AppbarUi import AppBarUI
from ui.main_window import MainWindow
from ui.book_ui import BookUI
from scr.book_manager import BookManager
from scr.config_manager import ConfigManager


def main(page: Page):
    
    app = MainWindow(page=page)
    global_bookUI = BookUI(page=page)
    book_manager = BookManager(page, global_bookUI) 
    appbar = AppBarUI(page=page, book_m=book_manager, main_window=app, book_ui=global_bookUI)
    config = ConfigManager(page=Page, book_m=book_manager, main_window=app, book_ui=global_bookUI)

    config.check_config_file()

    # window settings
    page.window_width = 800
    page.window_height = 600
    page.window_center()
    page.title = "EaseReader"

    page.appbar = appbar.appbarui
    page.add(app.build())

    book_manager.draw_book(app, global_bookUI.book_ui_container)

    page.update()

if __name__ == '__main__':
    app(target=main)
