from flet import *
from ui.main_window import MainWindow
from scr.fb2_manager import FB2Manager
from ui.BookUI.BookLoader import BookLoader
import json


class BookManager(UserControl):
    def __init__(self, page: Page, fb_manager: FB2Manager, book_loader_ui: BookLoader):
        super().__init__()

        self.page = page
        self.fb2_manager = fb_manager
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

    def draw_book(self, main_window: MainWindow):
        file_paths = self.get_book_path()
        
        main_window.book_row.controls.clear()
        for filename in file_paths:
            metadata = self.fb2_manager.generate_metadata(filename=filename)

            # Создаем новый экземпляр BookLoader для каждой книги
            book_loader = BookLoader(self.page)
            book_loader.title_book.value = metadata["title"]
            book_loader.author_name.value = metadata["author"]
            book_loader.cover_book_image.src = f"https://picsum.photos/200/200?"
            book_loader.cover_book_image.src = metadata["cover"]

            main_window.book_row.controls.append(book_loader.build())
            
        main_window.book_row.update()