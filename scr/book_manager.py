from flet import Page
from ui.main_window import MainWindow
from ui.book_ui import BookUI
import json

book_ui = BookUI(page=Page)

def get_book_path():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("path_to_text_file", [])
        
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}

def draw_book(main_window: MainWindow(page=Page)):
    items = []

    entries = get_book_path()
    main_w = main_window

    # main_w.book_row.controls.clear()
    # print("Books clear")

    for i in entries:
        main_w.book_row.controls.append(
            book_ui.book_ui
        )
    
    main_w.book_row.update()
    print("drawing books to window")
