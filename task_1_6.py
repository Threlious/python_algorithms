number = int(input('Введите номер буквы '))
if 1 <= number <= 26:
    print(f'Это буква {chr(number + 96)}')
else:
    print('Введено неверное значение')
