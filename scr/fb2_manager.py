from flet import *
from bs4 import BeautifulSoup
import os


class FB2Manager:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        
    
    def generate_metadata(self,file_path):

        metadata = {"title":None, "author":None}

        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'xml')

        all_tags = soup.find("description")
        title = all_tags.find("book-title").text
        if title == '' or title is None:
            title = os.path.splitext(
                os.path.basename(file_path))[0]

        author_tag = soup.find('author')
        author = f"{author_tag.find('first-name').text.strip()} {author_tag.find('last-name').text.strip()}"

        metadata['title'] = title
        metadata['author'] = author
        return metadata