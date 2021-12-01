import cProfile
import math
'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования Решета Эратосфена;
Использовать алгоритм решето Эратосфена
Без решета 
prime_numbers(g)
cProfile.run('prime_numbers(100)') - 0.001 seconds
cProfile.run('prime_numbers(1000)') - 0.035 seconds
cProfile.run('prime_numbers(10000)') - 3.472 seconds
Сложность: 
Предположительная сложность - квадратичная O(n**2) - так как при увеличении входных данных на 1 порядок время
выполнения возрастает на 2 порядка

С решетом
eratosthenes(g)
cProfile.run('eratosthenes(100)') - 0.389 seconds
cProfile.run('eratosthenes(1000)') - 86.621 seconds
Предположительная сложность - квадратичная O(n**2) - так как при увеличении входных данных на 1 порядок время
выполнения возрастает на 2 порядка

Алгоритм с применением решета Эратосфена даёт значительно меньшую производительность по сравнению с алгоритмом без
решета. Это моежт быть объяснено тем, что алгортим с решетом организован с применением дополнительной функции
prime_max(i), а также в нём создааётся 2 списка, что дополнительно нагружает оперативную память.
'''


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


cProfile.run('eratosthenes(1000)')
# cProfile.run('prime_numbers(10000)')
