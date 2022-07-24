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
import asyncio
import aiohttp
from datetime import datetime
import time

async def collection_animals(url):
    async with aiohttp.ClientSession() as session:
        while True:
            response = await session.get(url)
            soup = BeautifulSoup(await response.text(), "lxml")
            find_block = soup.find("div", id="mw-pages")
            animals = find_block.find_all("li")
            for animal in animals:
                if test_letter(animal.text):
                    data.append(animal.text + "\n")
                elif animal.text == "Aaaaba":
                    return True
            url = "https://ru.wikipedia.org" + find_block.find_all(href=re.compile("pagefrom"))[0].get("href")

def test_letter(animal):
    letter = animal.lower()[0]
    return ord(letter) >= ord("а") and ord(letter) <= ord("я")

def letter_count():
    with open("animals_file.txt", "r",encoding="utf-8") as animals_file:
        animals = animals_file.readlines()
    animals_dict = {}
    for animal in animals:
        letter = animal.upper()[0]
        if letter in animals_dict:
            animals_dict[letter] += 1
        else:
            animals_dict[letter] = 1
    animals_dict = sorted(animals_dict.items())
    for letter in animals_dict:
        print(f"{letter[0]}: {letter[1]}")

if __name__ == "__main__":
    start_time = datetime.now()
    data  = []
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(collection_animals("https://inlnk.ru/jElywR"))
    with open("animals_file.txt", "w", encoding="utf-8") as animals_file:
        animals_file.write("".join(data))
    letter_count()
    print(datetime.now() - start_time) # 15.0 seconds
