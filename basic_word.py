class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"""BasicWord({self.word}, {len(self.sub_words)})"""

    def has_sub_word(self, word):
        """
        Проверяет наличие слова в списке
        """
        return word in self.sub_words

    def count_sub_words(self):
        """
        Возвращает общее количество подслов
        """
        return len(self.sub_words)

    def get_word(self):
        return self.word
