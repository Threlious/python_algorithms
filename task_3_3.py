import random as rd

list1 = [rd.randint(1, 100) for i in range(10)]
print(list1)
ma = max(list1)
mi = min(list1)
print(f'max - {ma}, min - {mi}')
mi_idx = list1.index(mi)
ma_idx = list1.index(ma)
list1[ma_idx] = mi
list1[mi_idx] = ma
print(list1)
