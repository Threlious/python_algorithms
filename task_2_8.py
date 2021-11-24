n = int(input("Введите количество чисел "))
user_list = []
for i in range(n):
    numb = int(input("Введите число "))
    user_list.append(numb)
print(user_list)
z = int(input("Введите ифру, которую необходимо посчитать "))
print(user_list.count(z))
