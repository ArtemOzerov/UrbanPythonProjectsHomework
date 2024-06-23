def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(f'Матрица {n}x{m}:\n{matrix}')

get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)