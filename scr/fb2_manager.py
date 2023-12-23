from flet import *
from bs4 import BeautifulSoup
from PIL import Image
import base64
from io import BytesIO


class FB2Manager:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.metadata = {
            "title": None,
            "author": None,
            "cover": None
        }

    def generate_metadata(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "xml")

        author_tag = soup.find("author") or soup.find("title-info")
        author_name = author_tag.find("first-name").text + ' ' + author_tag.find("last-name").text

        title_tag = soup.find("title-info").find("book-title")
        book_title = title_tag.text

        self.metadata["title"] = book_title
        self.metadata["author"] = author_name
        self.metadata["cover"] = self.get_cover_book(filename=filename)
        print(self.metadata["cover"])
        return self.metadata
    
    def get_cover_book(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')

        # Найти обложку в XML-структуре fb2
        cover_data = None
        for binary_tag in soup.find_all('binary', {'content-type': 'image/jpeg'}):
            cover_data = binary_tag.text

            if cover_data:
                # Декодировать base64 и создать изображение из байтов
                image_data = base64.b64decode(cover_data)
                image = Image.open(BytesIO(image_data))

                return image