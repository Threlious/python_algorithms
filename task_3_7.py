import random as rd

list1 = [rd.randint(1, 100) for i in range(10)]
print(list1)
list1.sort()
print(list1)
print(f'Min elements - {list1[0:2]}')
