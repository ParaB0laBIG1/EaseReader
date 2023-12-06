import json
import os
from flet import Page, app, FilePickerResultEvent
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ConfigManager():
    def __init__(self, page: Page):
        super().__init__()

        self.page = page

        self.config_path = "config.json"
        
        self.data = {
            "path_to_text_file": [],
            "theme": "Dark"
        }

    def file_traking(self):
        pass

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
    
    def get_config_data(self):
        """
            Getting config data
        """

        with open(self.config_path, "r") as f:
            return json.load(f)

    def checking_path_availability(self, path):
        """
            Checking for duplicate paths
        """

        config_data = self.get_config_data()
        path_to_text_file_value = config_data.get("path_to_text_file", [])
        
        for path_file in path_to_text_file_value:
            if path_file == path:
                return True
        return False

    def save_path_in_config(self, e: FilePickerResultEvent):
        """
            Save the path to the file in a json file
        """
        config_data = self.get_config_data()
        check = self.checking_path_availability(path=", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!")
        
        if check == True:
            print("the selected file is already written to Json")
        else:
            config_data["path_to_text_file"].append(", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!")
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(config_data, f, indent=4, ensure_ascii=False)
        