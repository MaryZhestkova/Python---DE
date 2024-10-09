# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 
# из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def rename_files(directory, base_name, num_digits, source_ext, target_ext, name_range):
    # Получаем список всех файлов в директории
    files = [f for f in os.listdir(directory) if f.endswith(source_ext)]
    # Счетчик для порядкового номера
    counter = 1
    for file in files:
        # Извлекаем оригинальное имя файла без расширения
        original_name = os.path.splitext(file)[0]
        
        # Получаем срез оригинального имени
        sliced_name = original_name[name_range[0]:name_range[1]]
        
        # Формируем новое имя файла
        new_name = f"{sliced_name}{base_name}{str(counter).zfill(num_digits)}{target_ext}"
        
        # Полные пути к старому и новому файлам
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_name)
        
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        
        print(f"Переименован: '{file}' -> '{new_name}'")
        
        # Увеличиваем счетчик
        counter += 1

# Пример
rename_files(
    directory='/Users/mariyazhestkova/Desktop/Python_course/texts',  #  Меняем путь
    base_name='_new',
    num_digits=3,
    source_ext='.txt',
    target_ext='.md',
    name_range=[3, 6]
)