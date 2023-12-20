import json
import os
from flet import Page, FilePickerResultEvent
from scr.book_manager import BookManager
from ui.BookUI.BookLoader import BookLoader
from ui.main_window import MainWindow


class ConfigManager():
    def __init__(self, page: Page, book_m: BookManager, main_window: MainWindow,  book_loader_ui: BookLoader):
        super().__init__()

        self.page = page
        self.config_path = "config.json"
        self.config_data = self.load_config_data()  
        self.book_m = book_m
        self.main_window = main_window
        self.book_loader_ui = book_loader_ui


        self.data = {
            "path_to_text_file": []
        }

    def load_config_data(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}

    def check_config_file(self):
        """
            Checking the presence of the config file
        """
        if os.path.exists(self.config_path):
            print("Config file exists")
        else:
            self.create_config_file()

    def create_config_file(self):
        """
            Create the config file
        """
        with open(self.config_path, "w") as f:
            json.dump(self.data, f, indent=4)

        print("Create json file")
    
    def get_config_data(self, key: str):
        """
            Getting config data
        """

        get_data = self.config_data.get(key, [])
        return get_data

    def save_path_in_config(self, e: FilePickerResultEvent):
        """
        Save the path to the file in a json file
        """
        new_paths = [f.path for f in e.files]

        existing_paths = self.config_data.get("path_to_text_file", [])
        paths_to_add = list(set(new_paths) - set(existing_paths))

        if paths_to_add:
            print("The path was saved in config")

            self.config_data.setdefault("path_to_text_file", []).extend(paths_to_add)

            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config_data, f, indent=4, ensure_ascii=False)

            self.book_m.draw_book(main_window=self.main_window)
        else:
            print("The path is already saved in the config")



    def checking_path_availability(self, path):
        """
        Checking for duplicate paths
        """
        paths_from_config = self.get_config_data(key="path_to_text_file")

        return any(path == config_path for config_path in paths_from_config)

