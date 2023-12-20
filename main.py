from flet import *
from ui.AppbarUi import AppBarUI
from ui.main_window import MainWindow
from scr.book_manager import BookManager
from scr.config_manager import ConfigManager
from ui.BookUI.BookLoader import BookLoader
from scr.fb2_manager import FB2Manager


def main(page: Page):
    
    app = MainWindow(page=page)
    fb2_manager = FB2Manager(page=page)
    book_loader_ui = BookLoader(page=page)
    book_manager = BookManager(page, fb_manager=fb2_manager, book_loader_ui=book_loader_ui) 
    appbar = AppBarUI(page=page, book_m=book_manager, main_window=app, book_loader_ui=book_loader_ui)
    config = ConfigManager(page=Page, book_m=book_manager, main_window=app, book_loader_ui=book_loader_ui)

    config.check_config_file()

    # window settings
    page.window_width = 800
    page.window_height = 600
    page.window_center()
    page.title = "EaseReader"

    page.appbar = appbar.appbarui
    page.add(app.build())

    book_manager.draw_book(app)

    page.update()

if __name__ == '__main__':
    app(target=main)
