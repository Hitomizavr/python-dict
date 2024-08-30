# Функция проверки падежей именования возраста

print("")

def padeg(num, one, two, three):
    if (2 <= age % 10 <= 4) and not (11 <= age % 100 <= 14):
        return one
    elif age % 10 == 1 and age % 100 != 11:
        return two
    else:
        return three
    return ""

pets = {}

while True:
    name = input("Введите имя питомца  (клавиша enter - выход): ")

    if name == "":
        break

    type = input("Введите тип животного: ")
    age = input("Введите возраст животного: ")
    owner = input("Введите имя хозяина питомца: ")

    pets[name] = {"Вид питомца": type, "Возраст питомца": age, "Имя владельца": owner}

for key in pets.keys():
    values = list(pets[key].values())

    name = key
    type = values[0]
    age = int(values[1])
    owner = values[2]

    print(
        "Это",
        type.lower().strip(),
        'по кличке "' + name.capitalize().strip() + '".',
        "Возраст:",
        age,
        padeg(age, "года", "год", "лет") + ".",
        "Имя владельца:",
        owner + "."
    )

# for pet in pets:
#     print("Это",
#     pets[pet]['Вид питомца'],
#     "по кличке", pet + ". Возраст питомца:",
#     pets[pet]['Возраст питомца'], padeg(int(pets[pet]['Возраст питомца']), "года", "год", "лет"),
#     "Имя владельца:", pets[pet]['Имя владельца']);
