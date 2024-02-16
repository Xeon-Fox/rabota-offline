import random

def random_matrix(row, column):
    matrix = []
    for _ in range(row):
        new_row = [random.randint(-100, 100) for _ in range(column)]
        matrix.append(new_row)
    return matrix

def it_of_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            yield matrix[r][c]

my_matrix = random_matrix(4, 6)

print(my_matrix)
numbers = it_of_matrix(my_matrix)

for x in numbers:
    print(x, end=", ")