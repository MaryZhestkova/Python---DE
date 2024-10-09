# 2. Напишите функцию, которая получает на вход директорию и рекурсивно 
# обходит её и все вложенные директории. Результаты обхода 
# сохраните в файлы json, csv и pickle. 
# ○ Для дочерних объектов указывайте родительскую директорию. 
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер 
# файлов в ней с учётом всех вложенных файлов и директорий.


from pathlib import Path
import json
import csv
import pickle

def get_directory_info(directory: Path) -> list:
    result = []

    for item in directory.rglob('*'):
        if item.is_dir():
            size = sum(f.stat().st_size for f in item.rglob('*') if f.is_file())
            result.append({
                'name': item.name,
                'type': 'directory',
                'parent': str(item.parent),
                'size': size
            })
        elif item.is_file():
            result.append({
                'name': item.name,
                'type': 'file',
                'parent': str(item.parent),
                'size': item.stat().st_size
            })

    return result

def save_to_files(data: list, directory: Path) -> None:
    # Сохранение в JSON
    with open(directory / 'directory_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    # Сохранение в CSV
    with open(directory / 'directory_info.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    # Сохранение в Pickle
    with open(directory / 'directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def process_directory(directory: str) -> None:
    dir_path = Path(directory)
    data = get_directory_info(dir_path)
    save_to_files(data, dir_path)

if __name__ == '__main__':
    process_directory('/Users/mariyazhestkova/Desktop/Python_course/Python-HW-8')  # Укажите путь к вашей директории