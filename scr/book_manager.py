from flet import *
from ui.main_window import MainWindow
from ui.book_ui import BookUI
import json


class BookManager(UserControl):
    def __init__(self, page: Page, book_ui: BookUI):
        super().__init__()

        self.page = page
        self.book_ui = book_ui

    def get_book_path(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("path_to_text_file", [])
            
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}

    def draw_book(self,main_window: MainWindow, book_ui):
        items = []

        entries = self.get_book_path()

        main_window.book_row.controls.clear()
        print("Books clear") 

        for i in entries:
            main_window.book_row.controls.append(
                self.book_ui
            )
        
        main_window.book_row.update()
        print("drawing books to window")
