letter1 = input('Введите первую букву ')
letter2 = input('Введите вторую букву ')
o1 = ord(letter1) - 96
o2 = ord(letter2) - 96
print(f'Буква {letter1} на {o1} месте\n'
      f'Буква {letter2} на {o2} месте\n')
if o1 > o2:
    print(f'Между ними {o1 - o2 - 1} букв')
elif o1 < o2:
    print(f'Между ними {o2 - o1 - 1} букв')
elif o1 == o2:
    print(f'Буквы находятся на одной позиции')
