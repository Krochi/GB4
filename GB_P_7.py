#Задача1.
from functools import reduce

# Заданные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

floats_cubed = list(map(lambda x: round(x ** 3, 3), floats))

long_names = list(filter(lambda name: len(name) >= 5, names))

product_of_numbers = reduce(lambda x, y: x * y, numbers)

print(f"Числа в третьей степени: {floats_cubed}")
print(f"Имена длиной 5 и более букв: {long_names}")
print(f"Произведение всех чисел: {product_of_numbers}")




#Задача2.

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = list(map(lambda x, y: (x, y), letters, numbers))
print(results)




#Задача3

from collections import Counter

def can_be_poly(s: str) -> bool:

    freq = Counter(s)

    odd_counts = list(filter(lambda x: x % 2 != 0, freq.values()))

    return len(odd_counts) <= 1


print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False



#Задача4

def count_unique_characters(s: str) -> int:

    s_lower = s.lower()

    unique_chars = list(filter(lambda x: s_lower.count(x) == 1, s_lower))

    return len(unique_chars)

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)

