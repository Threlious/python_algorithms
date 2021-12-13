from random import uniform

lst = [round(uniform(0, 49), 1) for i in range(10)]


def merge_to_list(a, b):
    c = []
    i = j = 0  # первые элементы списка a и b
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(arr):  # выполянет сортировку
    if len(arr) == 1:  # если длина массива равна 1 то возвращает его как отсортированный
        return arr
    mid = len(arr) // 2  # середина массива
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge_to_list(left, right)


print(f'{lst}\n{merge_sort(lst)}')
