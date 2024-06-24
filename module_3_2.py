def single_root_words (root_word, *other_words):
    same_words = []
    for word in other_words:
        if type(word) is not str and type(root_word) is not str:
            print('parameters must be string')
    root_word = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        other_words = [word_lower]
        for i in other_words:
            if root_word in i or i in root_word:
                same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)