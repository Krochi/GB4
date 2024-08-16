#Задание1:

# Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Нужно выполнить две задачи:
# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третьем
# списках.
# Каждую задачу нужно выполнить двумя способами:
# 1. без использования множеств;
# 2. с использованием множеств.

#Решение1:

elements = set(array_1) & set(array_2) & set(array_3)

common_elements = list(elements)

print(common_elements)

unique_elements = set(array_1) - set(array_2) - set(array_3)

unique_elements = list(unique_elements)

print(unique_elements)

#Решение2:
array = [[1, 5, 10, 20, 40, 80, 100],
        [6, 7, 20, 80, 100],
        [3, 4, 15, 20, 30, 70, 80, 120]]

common_elements = set(array[0])
for lst in array[1:]:
    common_elements &= set(lst)

common_elements = list(common_elements)

print(common_elements)




#Задание2:

# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.

#Решение:

def is_poly(words):
    volue_dict = {}

    for char in words:
        if char in volue_dict:
            volue_dict[char] += 1
        else:
            volue_dict[char] = 1

    odd_count = 0
    for count in volue_dict.values():
        if count % 2 != 0:
            odd_count += 1

    if len(words) % 2 == 0 and odd_count == 0:
        return True
    elif len(words) % 2 != 0 and odd_count == 1:
        return True
    else:
        return False

word1 = "aab"
word2 = "aabc"

print(f"'{word1}' это слово является палиндромом? {is_poly(word1)}")
print(f"'{word2}' это слово является палиндромом? {is_poly(word2)}")



#Задание3:

sinonyms = {
    'привет': 'здравствуйте',
    "печально": "грустно",
    "весело": "радостно",
    "быстрый": "скорый",
    "умный": "разумный",
    "веселый": "радостный",
    "красивый": "прекрасный",
    "сильный": "мощный",
    "страшный": "ужасный",
    "добрый": "сердечный",
    "смешной": "забавный"
}

while True:
    word = input("Введите слово: ").strip().lower()

    if word in sinonyms:
        print(f"Синоним слова '{word}': {sinonyms[word]}")
        break
    else:
        print("Слово не найдено в словаре. Попробуйте снова.")



#Задание4:

# Создайте программу для лингвистов, которая будет инвертировать полученный
# словарь. То есть в качестве ключа будет частота, а в качестве значения —
# список символов с этой частотой. Вам нужно реаллизовать:
# 1. получить текст и создать из него оригинальный словарь частот;
# 2. создать новый словарь и заполнить его данными из оригинального
# словаря частот, используя количество повторов в качестве ключей, а
# буквы — в качестве значений, добавляя их в список для хранения.

#Решение:

def create_dict(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def invert_dict(frequency):
    inverted = {}
    for char, count in frequency.items():
        if count in inverted:
            inverted[count].append(char)
        else:
            inverted[count] = [char]
    return inverted

def print_dict(d):
    for key in sorted(d):
        print(f"{key} : {d[key]}")

text = input("Введите текст: ")

original_frequency = create_dict(text)

inverted_frequency = invert_dict(original_frequency)

print("Оригинальный словарь частот:")
print_dict(original_frequency)

print("Инвертированный словарь частот:")
print_dict(inverted_frequency)
