from flet import *
from ui.main_window import MainWindow
from scr.fb2_manager import FB2Manager
from ui.BookUI.BookLoader import BookLoader
import json


class BookManager(UserControl):
    def __init__(self, page: Page, fb_manager: FB2Manager, book_loader_ui: BookLoader):
        super().__init__()

        self.page = page
        self.fb_manager = fb_manager
        self.book_loader_ui = book_loader_ui

    def get_book_path(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                print(data.get("path_to_text_file", []))
                return data.get("path_to_text_file", [])
            
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []

    def draw_book(self,main_window: MainWindow):

        file_paths = self.get_book_path()

        for file_path in file_paths:
            metadate = self.fb_manager.generate_metadata(file_path=file_path)

            title_book = self.book_loader_ui.title_book
            book_loader_container = self.book_loader_ui.book_loader_container

            title_book.value = metadate["title"]
            print(title_book.value)

            
            main_window.book_row.controls.append(
                book_loader_container
            )

        main_window.book_row.update()