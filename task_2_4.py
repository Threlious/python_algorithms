n = input("Введите число элементов ")
a = [1]
for i in range(int(n) - 1):
    a.append(a[i] * (-0.5))
print(a)
_sum = (a[-1] * (-0.5) - 1) / (-0.5 - 1)
print(_sum)
