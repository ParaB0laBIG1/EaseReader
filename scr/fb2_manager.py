from flet import *
import xml.etree.ElementTree as ET
import json
from scr.config_manager import ConfigManager


class FB2Manager:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.config = ConfigManager(self.page)

        