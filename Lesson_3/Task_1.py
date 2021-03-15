for i in range(2, 10):
    result = 0
    for n in range(2, 100):
        if n % i == 0:
            result += 1
    print(result)
