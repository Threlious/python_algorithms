from itertools import zip_longest


def sum_hex(x, y):
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    numbers_dict = dict(zip(list_of_numbers, range(16)))  # словарь соответствия чисел из 16 системы и их
    # порядковых номеров
    first = list(x)
    second = list(y)
    if len(first) < len(second):  # меняем числа местами так, чтобы на первом месте стояло более длинное число
        first, second = second, first
    k = 0  # разряд
    first, second = first[::-1], second[::-1]
    res = []  # результат вычислений
    for first_, second_ in zip_longest(first, second, fillvalue='0'):
        res.append(list_of_numbers[(numbers_dict[first_] + numbers_dict[second_] + k) % 16])  # скаладываем два числа из
        # словаря соответствия по ключам, делим полученное число на 16, таким образом находим его индекс и используем
        # его в словаре list_of_numbers
        k = (numbers_dict[first_] + numbers_dict[second_]) // 16
    return res[::-1]


def multi_hex(x, y):
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    first = list(x)
    second = list(y)
    first, second = first[::-1], second[::-1]
    res = '0'  # первичное значение умножения
    for i in range(len(second)):
        sum_ = []  # результат суммы при последовательном умножении чисел первого числа на число второго
        if i > 0:
            sum_ = ['0'] * i
        k = 0
        for j in first:
            first_ = list_of_numbers.index(j)
            second_ = list_of_numbers.index(second[i])
            sum_.append(list_of_numbers[(first_ * second_ + k) % 16])  # прибавляем к промежуточной сумме результат
            # умножения
            k = (first_ * second_ + k) // 16  # число, переходящее на следующий разряд
            if j == len(second):
                break
        sum_.append(str(k))  # по завершении длины второго числа, добавляем оставшееся k
        res_x = sum_[::-1]
        res = sum_hex(res, res_x)
    return res


print(sum_hex('A2', 'C4F'))
print(multi_hex('A2', 'C4F'))
