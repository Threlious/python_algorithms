import random as rd
import cProfile
'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического задания первых трех 
уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Code1
cProfile.run("min_numbers(1000)") - 0.002 seconds
cProfile.run("min_numbers(10000)") - 0.020 seconds
cProfile.run("min_numbers(100000)") - 0.201 seconds
Сложность:
O(n) линейная сложность, так как время исполнения кода возрастает пропорционально увеличению размера входных данных 

Code2
cProfile.run("min_numbers2(1000)") - 0.002 seconds
cProfile.run("min_numbers2(10000)") - 0.020 seconds
cProfile.run("min_numbers2(100000)") - 0.198 seconds  
Сложность:
O(n) линейная сложность, так как время исполнения кода возрастает пропорционально увеличению размера входных данных

Сложность не изменилась, время выполнения изменилось на малую величину, что может являться погрешностью вычисления
врмени исполнения. Встроенный метод sort эквивалентен по времени ручному написанию кода. 
'''


def min_numbers(n):
    list1 = [rd.randint(1, 100) for i in range(n)]
    list1.sort()
    print(f'Min elements - {list1[0:2]}')


def min_numbers2(n):
    list1 = [rd.randint(1, 100) for i in range(n)]
    min_val1 = list1[0]
    min_val2 = list1[0]
    for i in list1:
        if i < min_val1:
            min_val1 = i
    list1.remove(min_val1)
    for i in list1:
        if i < min_val2:
            min_val2 = i
    print(min_val1, min_val2)


# cProfile.run("min_numbers2(100000)")
# cProfile.run("min_numbers(100000)")
