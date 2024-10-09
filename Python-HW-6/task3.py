import random
from task2 import validate_queens

def generate_positions():
    for _ in range(4):  # 4 успешные расстановки
        attempts = 0  # счётчик попыток
        while attempts < 100:  # ограничиваем количество попыток
            # Генерируем уникальные позиции для 8 королев
            columns = list(range(1, 9))  # Столбцы от 1 до 8
            random.shuffle(columns)  # Перемешиваем столбцы
            
            positions = [(i, columns[i - 1]) for i in range(1, 9)]  # Создаем позиции
            
            if validate_queens(positions):  # если расстановка успешная
                print(positions)  # выводим успешную расстановку
                break
            
            attempts += 1
        else:
            print("Не удалось найти успешную расстановку за 100 попыток.")

generate_positions()