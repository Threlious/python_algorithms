year = int(input('Введите год '))
if str(year)[-1] == '0' and str(year)[-2] == '0':
    if year % 400 == 0:
        print('Год високосный (две последние цифры 00)')
    else:
        print('Год невисокосный')
else:
    if year % 4 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')
