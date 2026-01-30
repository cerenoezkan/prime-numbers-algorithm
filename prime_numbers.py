for number in range(500, 600):
    is_prime = True

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
