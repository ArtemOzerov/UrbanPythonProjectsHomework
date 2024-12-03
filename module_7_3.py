class WordsFinder:

    SYMBOLS_TO_REPLACE = [',', '.', '=', '!', '?', ';', ':', ' - ']
    def __init__(self, *file_names):
        self.file_names = file_names

    def replacement(self, line):
        new_line = line.replace(WordsFinder.SYMBOLS_TO_REPLACE[0], '')
        for s in WordsFinder.SYMBOLS_TO_REPLACE[1:]:
            new_line = new_line.replace(s, '')
        return new_line

    def get_all_words(self):
        all_words = {}

        for fname in self.file_names:
            with open(fname, 'r', encoding='utf-8') as file:
                all_words[fname] = []
                for line in file:
                    line = line.lower()
                    line = self.replacement(line)
                    for word in line.split():
                        all_words[fname].append(word)
        return all_words

    def find(self, word):
        dict_ = {}
        for fname, words in self.get_all_words().items():
            for pos, w in enumerate(words):
                if word.lower() == w.lower():
                    dict_[fname] = pos + 1
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        for fname, words in self.get_all_words().items():
            counter = 0
            for w in words:
                if word.lower() == w.lower():
                    counter += 1
            dict_[fname] = counter
        return dict_

def main():
    finder2 = WordsFinder('test_file.txt', 'test_file_b.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
if __name__ == '__main__':
    main()