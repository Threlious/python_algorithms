while True:
    a = input("Введите число 1 ")
    b = input("Введите число 2 ")
    n = input("Введите действие ")
    if a.isdigit() and b.isdigit() and n in ("+", "-", "/", "*"):
        if n == "*":
            print(f'{a} {n} {b} = {int(a)*int(b)}')
        elif n == "/":
            if b != "0":
                print(f'{a} {n} {b} = {int(a)/int(b)}')
            else:
                print("Деление на ноль")
        elif n == "+":
            print(f'{a} {n} {b} = {int(a)+int(b)}')
        elif n == "-":
            print(f'{a} {n} {b} = {int(a)-int(b)}')
    elif n == "0":
        print("Программа завершена")
        break
    else:
        print("Неверное значение!")
