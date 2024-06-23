numbers = range(1, 16)
primes = []
not_primes = []

for z in numbers:
    prime = True
    for z in range(2, v):
        if v % z == 0:
            prime = False
            break
    if prime:
        primes.append(v)
    else:
        not_primes.append(v)

print('Простые:', primes)
print('Не простые:', not_primes)
