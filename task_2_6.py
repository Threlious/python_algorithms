import random as rd

number = rd.randint(0, 100)
n = 1
while n <= 11:
    if n <= 10:
        choice = int(input("Введите число "))
        if choice < number:
            print("Число больше")
        elif choice == number:
            print('Вы угадали число!')
            break
        elif choice > number:
            print("Число меньше")
    else:
        print(f'Было загадано число {number}, вы проиграли')
    n += 1
