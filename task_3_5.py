import random as rd

list1 = [rd.randint(-10, 10) for i in range(10)]
print(list1)
negative = []
for i in list1:
    if i < 0:
        negative.append(i)
max_negative = max(negative)
idx_max = 0
for i in list1:
    if i == max_negative:
        idx_max = list1.index(i)
        break
print(f'Максимальное отрицательное число {max_negative} на {idx_max} позиции')
