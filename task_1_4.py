import random as r
choice1 = input('Выберите действие и введите соответствующую букву \n'
                'i - случайное целое число\n'
                'f - случайное вещественное число\n'
                's - случайный симовл\n')
if choice1 == 'i':
    up1 = int(input('Введите верхнюю границу '))
    down1 = int(input('Введите нижнюю границу '))
    print(f'Случайное целое число {r.randint(down1, up1)}')
elif choice1 == 'f':
    up1 = float(input('Введите верхнюю границу '))
    down1 = float(input('Введите нижнюю границу '))
    print(f'Случайное вещественное число {r.uniform(down1, up1)}')
elif choice1 == 's':
    up1 = ord((input('Введите верхнюю границу ')))
    down1 = ord((input('Введите нижнюю границу ')))
    print(f'Случайный символ {chr(r.randint(down1, up1))}')
else:
    print('Неверное значение')
