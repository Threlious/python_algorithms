M = 5
N = 4
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(4):
        n = int(input("Введите число "))
        matrix[i].append(n)
for i in range(5):
    for j in range(4):
        print(matrix[i][j], end=' ')
        if j == 3:
            print(sum(matrix[i]), end='')
    print()
