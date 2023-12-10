import xml.etree.ElementTree as ET

def get_author_name(fb2_file_path):
    tree = ET.parse(fb2_file_path)
    root = tree.getroot()

    # Пространство имён для FB2
    ns = {'fb2': 'http://www.gribuser.ru/xml/fictionbook/2.0'}

    # Найти элемент, содержащий информацию об авторе
    author_info = root.find('.//fb2:description/fb2:title-info/fb2:author', ns)

    # Получить имя автора
    author_name = author_info.find('./fb2:first-name', ns).text
    author_last_name = author_info.find('./fb2:last-name', ns).text

    # Собрать полное имя автора
    full_author_name = f'{author_name} {author_last_name}'

    return full_author_name

# Пример использования
fb2_file_path = "C:\\Users\\Oleksii\\Downloads\\1984. Джордж Оруэлл.fb2"
author_name = get_author_name(fb2_file_path)
print(f'Имя автора: {author_name}')
