n = input('Введите натуральное число ')
even = []
odd = []
for i in n:
    if int(i) % 2 == 0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(f'{even} - {len(even)} чётных элементов')
print(f'{odd} - {len(odd)} нечётных элементов')
