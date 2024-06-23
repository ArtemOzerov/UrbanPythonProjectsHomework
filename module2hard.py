def find_pairs(n):
    pairs = []
    for z in range(1, 21):
        for v in range(z, 21):
            if (z + v) % n == 0:
                pairs.append(f"{z}{v}")
    return "".join(pairs)
n = int(input("Введите число от 3 до 20: "))
result = find_pairs(n)
print(f"Нужный пароль для числа {n}: {result}")