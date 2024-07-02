data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(list_):
    total_sum = 0
    if isinstance(list_, (int, float)):
        return list_
    elif isinstance(list_, str):
        return len(list_)
    elif isinstance(list_, (list, tuple, set)):
        for item in list_:
            total_sum += calculate_structure_sum(item)
    elif isinstance(list_, dict):
        for key, value in list_.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)

#делал это пол дня, честно, 3 модуль сложноват