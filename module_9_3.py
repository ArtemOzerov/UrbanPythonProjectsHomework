def main():
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    first_result = (len(s1)-len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))
    second_result = (len(first[j])==len(second[j]) for j in range(len(first)))

    print(list(first_result))
    print(list(second_result))

if __name__ == '__main__':
    main()
