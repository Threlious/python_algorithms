a = int(input('Введите число 1 '))
b = int(input('Введите число 2 '))
c = int(input('Введите число 3 '))
if b < a < c or c < a < b:
    print(f'Среднее число {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')
