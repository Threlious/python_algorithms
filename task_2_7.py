n = int(input("Введите число "))
list1 = []
for i in range(n):
    list1.append(i + 1)
print(list1)
print(f'Сумма чисел последовательности {sum(list1)}')
if sum(list1) == (n * (n + 1)) / 2:
    print(f"Равенство выполняется")
    print((n * (n + 1)) / 2)
else:
    print(f"Равенство не выполняется")
