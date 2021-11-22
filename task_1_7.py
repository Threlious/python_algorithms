a = int(input('Введите сторону 1 '))
b = int(input('Введите сторону 2 '))
c = int(input('Введите сторону 3 '))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b and a == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')
