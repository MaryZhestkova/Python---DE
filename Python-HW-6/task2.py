def validate_queens(positions):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if positions[i][1] == positions[j][1] or abs(positions[i][0] - positions[j][0]) == abs(positions[i][1] - positions[j][1]):
                return False
    return True

# Пример
my_positions = [
    (1, 2),  
    (2, 4),  
    (3, 6),  
    (4, 8),  
    (5, 3),  
    (6, 1),  
    (7, 7),  
    (8, 5)
]

# Пример
result = validate_queens(my_positions)
print(result)  # Вернет True, если ферзи не бьют друг друга, иначе False