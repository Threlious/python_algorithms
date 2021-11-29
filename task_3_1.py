for i in range(2, 10):
    lst = 0
    for j in range(2, 100):
        if j % i == 0:
            lst += 1
    print(f'{i} - {lst}')
