class Player:
    def __init__(self, name=""):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f"""Player({self.name}, {self.used_words})"""

    def count_used_words(self):
        """
        Получение количества использованных слов
        """
        return len(self.used_words)

    def add_word(self, word):
        """
        Добавление слова в использованные слова
        """
        self.used_words.append(word)
    def is_word_used(self, word):
        """
        Проверка использования слова до этого
        """
        return word.lower() in self.used_words
