import random as rd

list1 = [rd.randint(0, 100) for i in range(10)]
print(list1)
max_idx = list1.index(max(list1))
min_idx = list1.index(min(list1))
sm = 0
if abs(max_idx - min_idx) == 1:
    print("Нет элементов между числами")
elif max_idx > min_idx:
    for i in list1[min_idx + 1:max_idx]:
        sm += i
elif max_idx < min_idx:
    for i in list1[max_idx + 1:min_idx]:
        sm += i
print(f'Максимальный элемент - {list1[max_idx]}\nМинимальный элемент - {list1[min_idx]}\n'
      f'Сумма между ними - {sm}')
