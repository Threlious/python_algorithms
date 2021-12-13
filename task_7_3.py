from random import randint
from statistics import median

lst = [randint(0, 100) for i in range(101)]
# test = [40, 92, 98, 81, 100, 83, 50, 86, 2, 83, 3]


def med_find(arr):
    med = None  # медиана в начале не определена
    num = len(arr) // 2  # число элементов с каждой стороны
    for i in arr:
        left, right = [], []  # левая и правая сторона относительно проверяемого числа
        tmp = arr[:arr.index(i)] + arr[arr.index(i) + 1:]  # слайс части списка без декущего элемента
        same = []  # хранилище копий текущего числа
        for j in tmp:  # здесь раскидываем числа относительного текущего числа
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)
            elif i == j:
                same.append(j)
        for k in same:  # здесь разбрасываем одинаковые числа, чтобы с кажой стороны было поровну
            if len(right) > len(left):
                left.append(k)
            else:
                right.append(k)
        if len(right) == num and len(left) == num:  # проверка соответствия равенства количества чисел с каждой стороны
            med = i
            break
    return med


print(f'{lst}\nMedian by module - {median(lst)}\nMedian by func - {med_find(lst)}')
# print(f'{test}\nMedian by module - {median(test)}\nMedian by func - {med_find(test)}')
