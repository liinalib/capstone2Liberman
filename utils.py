import random
import requests
from basic_word import BasicWord

def load_json_from_url(path):
    """
    Загружает данные по ссылке и возвращает слово
    """

    raw_data = requests.get(path)
    data = raw_data.json()
    return data

def load_random_word(path):
    """
   Возвращает случайное слово и его посдлово
   """
    all_words = load_json_from_url(path)
    one_word = random.choice(all_words)
    word = one_word["word"]
    sub_words = one_word["subwords"]
    basic_word = BasicWord(word, sub_words)

    return basic_word

basic_word = load_random_word("https://api.npoint.io/12b8dedc2af7c08865b2")
print(basic_word)
