

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matches = []
        word_letters = [letter for letter in self.word]
        for word in list:
            list_letters = [letter for letter in word]
            if sorted(list_letters) == sorted(word_letters):
                matches.append(word)
        return matches