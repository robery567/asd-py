class Phrase:
    def __init__(self, text):
        self.text = text
        self.words = []
        self.__set_words()

    def __set_words(self):
        word = []

        for char in self.text:
            if char != ' ':
                word.append(char)
            else:
                self.words.append(word)
                del word
                word = []

        self.words.append(word)

    def get_words_count(self):
        return len(self.words)

    def get_words(self):
        return self.words

    def __reverse_word(self, word):
        reversed_word = ""

        for i in range(len(word)-1, -1, -1):
            reversed_word += word[i]

        return reversed_word

    def encrypt_phrase(self):
        reversed_phrase = []

        for i in range(len(self.words)-1, -1, -1):
            reversed_phrase.append(self.__reverse_word(self.words[i]))

        self.words = reversed_phrase
