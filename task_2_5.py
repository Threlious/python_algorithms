n = 32
while n <= 127:
    for i in range(n, n + 10):
        if i <= 127:
            print(f'{i} - {chr(i)}', end=" ")
        else:
            break
    print()
    n += 10
