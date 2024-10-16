class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for name in file_names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        del_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                clear_line = ''
                for line in f:
                    line = line.lower()
                    for char in line:
                        if char in del_list:
                            continue
                        clear_line += char
                    clear_line += ' '
            all_words.update({file: clear_line.split()})
        return all_words

    def find(self, word):
        find_dict = {}
        index = None
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                index = int(words.index(word)) + 1
            find_dict.update({file_name: index})
        return find_dict

    def count(self, word):
        count_dict = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            count_dict.update({file_name: words.count(word)})
        return count_dict


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT'))   # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего