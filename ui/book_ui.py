from flet import *
from scr.config_manager import ConfigManager
from scr.fb2_manager import FB2Manager
from ui.main_window import MainWindow


class BookUI(UserControl):
    def __init__(self, page: Page, main_window: MainWindow):
        super().__init__()

        self.page = page
        self.config_m = ConfigManager(page=self.page)
        self.fb2_m = FB2Manager(self.page)
        self.main_w = main_window

    def draw_book_ui(self):

        items = []
        entries = self.config_m.get_config_data(key="path_to_text_file")

        print("Add")
        for i in entries:
            self.main_w.book_row.controls.append(
                Container(
                    alignment=alignment.center,
                    width=300,height=300,
                    bgcolor=colors.BLUE_GREY_700,
                    border_radius=border_radius.all(5)
                )
            )
        
        self.main_w.book_row.update()