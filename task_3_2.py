list1 = [8, 3, 15, 6, 4, 2]
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(list1.index(i))
print(list2)
