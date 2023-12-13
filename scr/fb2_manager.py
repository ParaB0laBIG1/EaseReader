from flet import *
import xml.etree.ElementTree as ET


class FB2Manager:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        