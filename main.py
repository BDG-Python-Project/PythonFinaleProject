from random import randint
from realist import Realist
from fool import Fool
from positive import Positive

names_list = ["Ալեքսանդր", "Արամ", "Անահիտ", "Իրինա", "Նարինե", "Արմեն", "Հայկ", "Սիլվա", "Սանասար", "Բաղդասար"]
characters = [Fool, Positive, Realist]
persons = []

for j in range(5):
    random_age = randint(20, 40)
    index = randint(0, len(names_list) - 1)
    random_name = names_list[index]
    del names_list[index]

    character = characters[randint(0, len(characters) - 1)]
    person = character(random_name, random_age)
    persons.append(person)

chat_content = ""
for person in persons:
    chat_content += f"{person.get_name()} {person.get_age()} տարեկան \n"

chat_content += "\n\n"

for person in persons:
    others = [p for p in persons if p != person]

    for some_person in others:
        chat_content += person.say_hello(some_person) + "\n"
        chat_content += some_person.say_hello(person) + "\n"
        chat_content += "\n"

    persons = others
    chat_content += "\n\n"


chat_file = open("chat_messages.txt", "w", encoding='utf-8')
chat_file.write(chat_content)
chat_file.close()
