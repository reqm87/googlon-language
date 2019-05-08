import math


class Googlon:

    def __init__(self, text):
        self.prepositions = 0
        self.verbs = 0
        self.subjunctive_verbs = 0
        self.sorted_words = ""
        self.pretty_numbers = 0
        self.process(text)
        self.print_results()

    def print_results(self):
        print('1) There are {} prepositions in the text'.format(
            self.prepositions))
        print('2) There are {} verbs in the text'.format(self.verbs))
        print('3) There are {} subjunctive verbs in the text'.format(
            self.subjunctive_verbs))
        print('4) Vocabulary list: {}'.format(self.sorted_words))
        print('5) There are {} distinct pretty numbers in the text'.format(
            self.pretty_numbers))

    @staticmethod
    def get_alphabet():
        return ['s', 'x', 'o', 'c', 'q', 'n', 'm', 'w', 'p', 'f',
                'y', 'h', 'e', 'l', 'j', 'r', 'd', 'g', 'u', 'i']

    @staticmethod
    def get_foo_letters():
        return ['s', 'x', 'm', 'p', 'f', 'd', 'u']

    @staticmethod
    def get_bar_letters():
        return ['o', 'c', 'q', 'n', 'w', 'y', 'h',
                'e', 'l', 'j', 'r', 'g', 'i']

    def is_preposition(self, word):
        return (len(word) == 6) \
               and (word[5] in self.get_foo_letters()) \
               and ('u' not in word)

    def is_verb(self, word):
        return (len(word) >= 6) \
               and (word[len(word) - 1] in self.get_bar_letters())

    def is_subjunctive_verb(self, word):
        return self.is_verb(word) and word[0] in self.get_bar_letters()

    def is_pretty_number(self, word):
        index = 0
        value = 0
        for letter in word:
            value += int(math.pow(20, index)) \
                     * self.get_alphabet().index(letter)
            index += 1
        return value >= 81827 and value % 3 == 0

    def sort_words(self, words):
        self.sorted_words = ' '.join(sorted(
            words, key=lambda word: [self.get_alphabet().index(letter)
                                     for letter in word]))

    def process(self, text):
        words = text.split(' ')
        for word in words:
            if self.is_preposition(word):
                self.prepositions += 1
            if self.is_verb(word):
                self.verbs += 1
            if self.is_subjunctive_verb(word):
                self.subjunctive_verbs += 1
            if self.is_pretty_number(word):
                self.pretty_numbers += 1
        self.sort_words(words)


def main():
    text = str(input('Please enter the text: '))
    Googlon(text)


if __name__ == "__main__":
    main()
