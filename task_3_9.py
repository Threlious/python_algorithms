import random as rd
M = 5
N = 4
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(4):
        n = rd.randint(0, 9)
        matrix[i].append(n)
for i in range(5):
    for j in range(4):
        print(matrix[i][j], end=' ')
        if j == 3:
            print('|', sum(matrix[i]), end='')
    print()
new_list = []
for i in range(4):
    new_list.append([])
    for j in range(5):
        new_list[i].append(matrix[j][i])
min_list = []
n = 0
for i in new_list:
    min_list.append(min(new_list[n]))
    n += 1
print(f'{"_ "  * 4}')
for i in min_list:
    print(i, end=' ')
print(f'\nMax element: {max(min_list)}')
