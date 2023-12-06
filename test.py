# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(doc.page_count):
#         page = doc[page_num]
#         text += page.get_text()
#     return text

# # Пример использования
# pdf_file_path = "C:\\Users\\Oleksii\\Downloads\\orvell-dzhordzh-19842283.pdf"
# pdf_text = extract_text_from_pdf(pdf_file_path)
# print(pdf_text)


import hashlib
import os
import json

def get_file_info(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            file_hash = hashlib.sha256(content).hexdigest()
        return {"content": content, "hash": file_hash}
    except FileNotFoundError:
        return None

def save_file_info(file_path, info):
    with open(file_path, 'wb') as file:
        file.write(info["content"])
    with open(file_path + ".info", 'w') as info_file:
        json.dump({"hash": info["hash"]}, info_file)

def check_file_changes(file_path):
    info_file_path = file_path + ".info"
    current_info = get_file_info(file_path)

    if os.path.exists(info_file_path):
        with open(info_file_path, 'r') as info_file:
            stored_hash = json.load(info_file).get("hash", None)

        if stored_hash != current_info["hash"]:
            print("Файл был изменен после выключения программы.")
            # Здесь можно обработать изменения в файле.
    else:
        print("Информации о файле нет. Создание записи.")
        save_file_info(file_path, current_info)

if __name__ == "__main__":
    file_path = "C:\\Users\\Oleksii\\Desktop\\test.txt"
    check_file_changes(file_path)
