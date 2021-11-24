n = input("Введите натуральные числа через пробел ")
user_list = n.split(" ")
print(user_list)
new_list = []
for i in user_list:
    sum_i = 0
    for j in i:
        sum_i += int(j)
    new_list.append(sum_i)
idx = new_list.index(max(new_list))
print(f'Список с суммой цифр: {new_list}\nНаибольшее число по сумме цифр - {(user_list[idx])}, его сумма - '
      f'{new_list[idx]} ')
