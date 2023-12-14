from flet import *
from ui.main_window import MainWindow
from ui.book_ui import BookUI
from scr.config_manager import ConfigManager
from scr.book_manager import BookManager


class AppBarUI(UserControl):
    def __init__(self, page: Page, book_m: BookManager, main_window: MainWindow, book_ui: BookUI):
        super().__init__()
        self.page = page
        self.book_m = book_m
        self.main_window = main_window
        self.book_ui = book_ui
        self.config = ConfigManager(self.page, self.book_m, self.main_window, book_ui=book_ui)

        self.open_book = TextButton(icon=icons.ADD,text="Add Book", 
                                    on_click=lambda _: self.selected_files.pick_files(dialog_title="Select file",
                                                                                    allowed_extensions=["pdf", "fb2"]))

        self.button_list = PopupMenuButton(
            items=[
                self.open_book
            ]
        )

        self.search_book = TextField(label=f"Search in Library", width=250,height=40)

        self.appbarui = AppBar(
            bgcolor=colors.WHITE12,
            leading=self.button_list,
            title=self.search_book
        )

        self.selected_files = FilePicker(on_result=self.config.save_path_in_config)
        self.page.overlay.extend([self.selected_files])
