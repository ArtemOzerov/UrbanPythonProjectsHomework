numbers = range(1, 16)
primes = []
not_primes = []
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
