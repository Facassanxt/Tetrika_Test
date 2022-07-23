# В нашей школе мы не можем разглашать персональные данные пользователей, 
# но чтобы преподаватель и ученик смогли объяснить нашей поддержке,
# кого они имеют в виду (у преподавателей, например, часто учится несколько Саш),
# мы генерируем пользователям уникальные и легко произносимые имена.
# Имя у нас состоит из прилагательного, имени животного и двузначной цифры.
# В итоге получается, например, "Перламутровый лосось 77".
# Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
# и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
# А: 642
# Б: 412
# В:....

import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def test_letter(animal):
    letter = animal.lower()[0]
    return ord(letter) >= ord("а") and ord(letter) <= ord("я")

def collection_animals(url):
    animals_file = open("animals_file.txt", "w+")
    while True:
        html = get_html(url)
        soup = BeautifulSoup(html, "lxml")
        find_block = soup.find("div", id="mw-pages")
        animals = find_block.find_all("li")
        for animal in animals:
            if test_letter(animal.text):
                animals_file.write(animal.text + "\n")
            elif animal.text == "Aaaaba":
                animals_file.close()
                return True
        url = "https://ru.wikipedia.org" + find_block.find_all(href=re.compile("pagefrom"))[0].get("href")

def letter_count():
    with open("animals_file.txt", "r") as animals_file:
        animals = animals_file.readlines()
    animals_dict = {}
    for animal in animals:
        letter = animal.upper()[0]
        if letter in animals_dict:
            animals_dict[letter] += 1
        else:
            animals_dict[letter] = 1
    for letter in animals_dict:
        print(f"{letter}: {animals_dict[letter]}")

if __name__ == "__main__":
    collection_animals("https://inlnk.ru/jElywR")
    letter_count()