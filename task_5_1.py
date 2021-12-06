import statistics


comp_num = input('Введите число предприятий ')
comp_dict = {}
for i in range(int(comp_num)):
    comp_name = input("Введите название компании ")
    comp_dict[comp_name] = []
    for j in range(1, 5):
        comp_sal = int(input(f'Введите прибыль за {j} квартал: '))
        comp_dict[comp_name].append(comp_sal)
sal_dict = {}
for i in comp_dict:
    sal_dict[i] = statistics.mean(comp_dict[i])
lst = [sal_dict[i] for i in sal_dict]
mean = statistics.mean(lst)
print(f'Средняя прибыль за год для всех предприятий: {mean}')
for i in sal_dict:
    if sal_dict[i] >= mean:
        print(f'Предприятие {i} имеет прибыль выше среднего')
for i in sal_dict:
    if sal_dict[i] < mean:
        print(f'Предприятие {i} имеет прибыль меньше среднего')
# print(comp_dict)
# print(sal_dict)
