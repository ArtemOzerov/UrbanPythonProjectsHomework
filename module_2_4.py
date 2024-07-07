numbers = range(1, 16)
primes = []  # [2, 3, 5, 7, 11, 13]
not_primes = []  # [4, 6, 8, 9, 10, 12, 14, 15]
# is_prime = True  # после проверки (True - в prime, False - в not_prime).
for z in numbers:
    if z == 1:
        continue
    is_prime = True
    for v in range(2, z):
        if z % v == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(z)
    else:
        not_primes.append(z)
print(primes)
print(not_primes)
