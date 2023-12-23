import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import tkinter as tk
import base64
from io import BytesIO

def read_fb2(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Найти обложку в XML-структуре fb2
    cover_data = None
    for binary_tag in root.iter('{http://www.gribuser.ru/xml/fictionbook/2.0}binary'):
        if 'content-type' in binary_tag.attrib and binary_tag.attrib['content-type'] == 'image/jpeg':
            cover_data = binary_tag.text
            break

    return cover_data

def display_cover(cover_data):
    if cover_data:
        # Декодировать base64 и создать изображение из байтов
        image_data = base64.b64decode(cover_data)
        image = Image.open(BytesIO(image_data))
        print(image)

        # Отобразить изображение в интерфейсе Tkinter
        root = tk.Tk()
        photo = ImageTk.PhotoImage(image)
        print(photo)
        label = tk.Label(root, image=photo)
        label.pack()

        root.mainloop()

if __name__ == "__main__":
    file_path = "C:\\Users\\Oleksii\\Downloads\\Нейромант. Гибсон Уильям.fb2"
    cover_data = read_fb2(file_path)
    display_cover(cover_data)
