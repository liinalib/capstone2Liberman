from utils import load_random_word
from player import Player

DATA_SOURCE = "https://api.npoint.io/12b8dedc2af7c08865b2"

print("Введите имя игрока.")
user_name = input()

player = Player(user_name)
print(f"Привет, {user_name}")

basic_word = load_random_word(DATA_SOURCE)
print(f"""Составьте {basic_word.count_sub_words()} слов из слова {basic_word.get_word()}.""")
print("Слово должно быть не короче 3 букв.")

while player.count_used_words() < basic_word.count_sub_words():
    user_input = input().strip().lower()

    if user_input in ["стоп", "stop"]:
        break

    elif len(user_input) < 3:
        print("Короткое слово!")
        continue

    elif not basic_word.has_sub_word(user_input):
        print("Нет такого слова!")

    elif player.is_word_used(user_input):
        print("Слово уже использовано!")

    else:
        print("Верно!")
        player.add_word(user_input)

print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")