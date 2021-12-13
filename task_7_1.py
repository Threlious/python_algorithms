from random import randrange

a = [randrange(-100, 100) for i in range(10)]


def sort_bubble(arr):
    n = 1
    tmp = None
    while n <= len(arr):
        if n == 1:
            tmp = arr.copy()
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if n == 1 and arr == tmp:
            print("Array is already sorted")
            break
        n += 1
    return arr


print(f'{a}\n{sort_bubble(a)}')
# b = sorted(a, reverse=True)
# print(f'{b}\n{sort_bubble(b)}')
