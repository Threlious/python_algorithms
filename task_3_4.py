list1 = [8, 8, 3, 3, 3, 3, 15, 6, 4, 2, 0, 0]
# 8 - 2 раза
# 3 - 4 раза
# 0 - 2 раза
set1 = set(list1)
print(f'{list1}\n{set1}')
list2 = []
idx = 0
for i in set1:
    list2.append(0)
    for j in list1:
        if i == j:
            list2[idx] += 1
    idx += 1
print(list2)
list_upd = list(set1)
idx_max = list2.index(max(list2))
print(f'Число {list_upd[idx_max]} встречается {list2[idx_max]} раз')
