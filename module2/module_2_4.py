numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for numb in numbers:
    is_prime = True
    for div in range(2, numb + 1):
        if (numb % div) == 0 and numb != div:
            is_prime = False
            break
        elif (numb % div) == 0 and numb == div:
            is_prime = True
        else:
            is_prime = False
    if is_prime and numb != 1:
        primes.append(numb)
    else:
        not_primes.append(numb)

print(f'Primes: {primes}')
print(f'Not_primes: {not_primes}')
