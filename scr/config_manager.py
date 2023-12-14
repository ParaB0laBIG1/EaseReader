import json
import os
from flet import Page, FilePickerResultEvent
from scr.book_manager import BookManager
from ui.main_window import MainWindow
from ui.book_ui import BookUI


class ConfigManager():
    def __init__(self, page: Page, book_m: BookManager, main_window: MainWindow, book_ui: BookUI):
        super().__init__()

        self.page = page
        self.config_path = "config.json"
        self.config_data = self.load_config_data()  
        self.book_m = book_m
        self.main_window = main_window
        self.book_ui = book_ui

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

    def checking_path_availability(self, path):
        """
            Checking for duplicate paths
        """

        path_to_text_file_value = self.get_config_data(key="path_to_text_file")
        return path in path_to_text_file_value
        
    def save_path_in_config(self, e: FilePickerResultEvent):
        """
        Save the path to the file in a json file
        """

        config_data_path = set(self.get_config_data(key="path_to_text_file"))
        new_paths = [f.path for f in e.files]

        for path in new_paths:
            if self.checking_path_availability(path):
                print(f"The selected file '{path}' is already written to Json")
            else:
                config_data_path.add(path)

        self.config_data["path_to_text_file"] = list(config_data_path)

        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config_data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error while writing to config file: {e}")

        self.book_m.draw_book(self.main_window)
        print("Paths added to config")
