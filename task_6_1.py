from memory_profiler import profile
import math
"""
1) def num_act() - функция, производящая простейшие арифметические операции над 2 числами.
Под каждую переменную стандартно выделялось 20.2 Мбит памяти
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     20.2 MiB     20.2 MiB           1   @profile
    29                                         def num_act():
    30     20.2 MiB      0.0 MiB           2       while True:
    31     20.2 MiB      0.0 MiB           2           a = input("Введите число 1 ")
    32     20.2 MiB      0.0 MiB           2           b = input("Введите число 2 ")
    33     20.2 MiB      0.0 MiB           2           n = input("Введите действие ")
    34     20.2 MiB      0.0 MiB           2           if a.isdigit() and b.isdigit() and n in ("+", "-", "/", "*"):
    35     20.2 MiB      0.0 MiB           1               if n == "*":
    36                                                         print(f'{a} {n} {b} = {int(a)*int(b)}')
    37     20.2 MiB      0.0 MiB           1               elif n == "/":
    38                                                         if b != "0":
    39                                                             print(f'{a} {n} {b} = {int(a)/int(b)}')
    40                                                         else:
    41                                                             print("Деление на ноль")
    42     20.2 MiB      0.0 MiB           1               elif n == "+":
    43                                                         print(f'{a} {n} {b} = {int(a)+int(b)}')
    44     20.2 MiB      0.0 MiB           1               elif n == "-":
    45     20.2 MiB      0.0 MiB           1                   print(f'{a} {n} {b} = {int(a)-int(b)}')
    46     20.2 MiB      0.0 MiB           1           elif n == "0":
    47     20.2 MiB      0.0 MiB           1               print("Программа завершена")
    48     20.2 MiB      0.0 MiB           1               break
    49                                                 else:
    50                                                     print("Неверное значение!")
    
2) def prime_numbers(g) - функция нахождения n-о простого числа без использования решета Эратосфена
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     20.1 MiB     20.1 MiB           1   @profile
    35                                         def prime_numbers(g):
    36     20.1 MiB      0.0 MiB           1       prime_list = [2]
    37     20.1 MiB      0.0 MiB           1       division_num = 3
    38     20.4 MiB      0.0 MiB        7918       while len(prime_list) < g:
    39     20.4 MiB      0.0 MiB        7917           flag = True
    40     20.4 MiB      0.2 MiB      517382           for i in prime_list.copy():
    41     20.4 MiB      0.0 MiB      516383               if division_num % i == 0:
    42     20.4 MiB      0.0 MiB        6918                   flag = False
    43     20.4 MiB      0.0 MiB        6918                   break
    44     20.4 MiB      0.0 MiB        7917           if flag:
    45     20.4 MiB      0.1 MiB         999               prime_list.append(division_num)
    46     20.4 MiB      0.0 MiB        7917           division_num += 1
    47     20.4 MiB      0.0 MiB           1       return prime_list[-1]
Простая инициализация переменных требует меньше оперативной памяти в отличии от цикла.

3) def eratosthenes(g) - функция нахождения n-о простого числа с использованием решета Эратосфена
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   103     20.1 MiB     20.1 MiB           1   @profile
   104                                         def eratosthenes(g):
   105     20.2 MiB      0.1 MiB         652       a = [i for i in range(prime_max(g))]
   106     20.2 MiB      0.0 MiB           1       a[1] = 0
   107     20.2 MiB      0.0 MiB           1       m = 2
   108     20.2 MiB      0.0 MiB         648       while m < prime_max(g):
   109     20.2 MiB      0.0 MiB         647           if a[m] != 0:
   110     20.2 MiB      0.0 MiB         118               j = m * 2
   111     20.2 MiB      0.0 MiB        1333               while j < prime_max(g):
   112     20.2 MiB      0.0 MiB        1215                   a[j] = 0
   113     20.2 MiB      0.0 MiB        1215                   j = j + m
   114     20.2 MiB      0.0 MiB         647           m += 1
   115     20.2 MiB      0.0 MiB           1       b = []
   116     20.2 MiB      0.0 MiB         650       for i in a:
   117     20.2 MiB      0.0 MiB         649           if a[i] != 0:
   118     20.2 MiB      0.0 MiB         118               b.append(a[i])
   119     20.2 MiB      0.0 MiB           1       del a
   120     20.2 MiB      0.0 MiB           1       return b[-1]
Использование памяти аналогично по принципу с предыдущей функцией
"""


@profile
def num_act():
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


@profile
def prime_numbers(g):
    prime_list = [2]
    division_num = 3
    while len(prime_list) < g:
        flag = True
        for i in prime_list.copy():
            if division_num % i == 0:
                flag = False
                break
        if flag:
            prime_list.append(division_num)
        division_num += 1
    return prime_list[-1]


def prime_max(i):
    primes = 0  # количество простых чисел на промежутке
    n = 2  # верхняя граница интервала i простых чисел
    while primes <= i:
        primes = n / math.log(n)  # теорема о распределения простых чисел
        n += 1
    return n  # возвращает максимальное число, на промежутке которого i простых чисел


@profile
def eratosthenes(g):
    a = [i for i in range(prime_max(g))]
    a[1] = 0
    m = 2
    while m < prime_max(g):
        if a[m] != 0:
            j = m * 2
            while j < prime_max(g):
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b[-1]


if __name__ == "__main__":
    pass
    # num_act()
    # prime_numbers(1000)
    # print(eratosthenes(100))
