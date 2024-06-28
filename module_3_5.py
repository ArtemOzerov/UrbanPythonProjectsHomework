def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
if __name__ == '__main__':
    result = get_multiplied_digits(int(input('Введите число: ')))
    print(result)