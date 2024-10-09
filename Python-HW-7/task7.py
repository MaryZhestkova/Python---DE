# Задача из семинара, которую не успели разобрать
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

def create_test_environment(test_folder):
    # Создаем тестовую директорию
    os.makedirs(test_folder, exist_ok=True)

    # Список файлов для создания
    test_files = [
        'video1.mp4',
        'image1.jpg',
        'document1.txt',
        'audio1.mp3',
        'video2.mkv',
        'image2.png',
        'document2.pdf',
        'audio2.wav',
        'other_file.docx',
        'not_a_file.txt'  # Файл, который должен остаться
    ]

    # Создаем тестовые файлы
    for file_name in test_files:
        with open(os.path.join(test_folder, file_name), 'w') as f:
            f.write(f'This is a test file: {file_name}')

# Пример использования
test_folder = '/Users/mariyazhestkova/Desktop/Python_course'  # Замените на ваш путь
create_test_environment(test_folder)

def sort_files(source_folder):
    # Определяем расширения для каждой категории
    categories = {
        'videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'texts': ['.txt', '.pdf', '.docx', '.xlsx'],
        'audios': ['.mp3', '.wav', '.aac']
    }
    
    # Создаем директории для каждой категории
    for category in categories.keys():
        category_path = os.path.join(source_folder, category)
        os.makedirs(category_path, exist_ok=True)

    # Перебираем файлы в исходной папке
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Пропускаем директории
        if os.path.isdir(file_path):
            continue

        moved = False
        # Проверяем расширение файла и перемещаем его в соответствующую директорию
        for category, extensions in categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_folder, category, filename))
                moved = True
                break
        
        # Если файл не подошел ни под одну категорию, он остается в исходной папке

# Пример использования
source_directory = '/Users/mariyazhestkova/Desktop/Python_course'  # Замените на ваш путь
sort_files(source_directory)

