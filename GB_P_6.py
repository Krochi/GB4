# Задание 1. Гласные буквы
# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину


# Запрашиваем текст у пользователя
# text = input("Введите текст: ")
#
# # Определяем строку с гласными буквами русского алфавита
# vowels_russian = 'ауоыиэяюёе'
#
# # Создаём список гласных из введённого текста
# vowels = [letter for letter in text.lower() if letter in vowels_russian]
#
# # Выводим список гласных букв
# print("Список гласных букв:", vowels)
#
# # Выводим длину списка
# print("Длина списка:", len(vowels))



# Задача 2. Случайные соревнования
# # Напишите программу, которая генерирует два списка участников (по 20
# # элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
# # подходящую функцию из модуля random. Затем сгенерируйте третий список, в
# # котором окажутся только победители из каждой пары


# import random
#
# # Генерация двух списков случайных вещественных чисел
# first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
# second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
#
# # Генерация списка победителей
# winners = [first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(20)]
#
# # Выводим результаты
# print("Первая команда:", first_team)
# print("Вторая команда:", second_team)
# print("Победители тура:", winners)



# Задача 3. Двумерный список
# Часто в программировании приходится писать код исходя из результата,
# который требует заказчик. В этот раз ему нужно получить двумерный список:
#  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# Напишите программу, которая генерирует такой список и выводит его на экран.
# Используйте только list comprehensions.

# Генерируем двумерный список с использованием вложенного генератора списка
result = [[i + j * 4 for j in range(3)] for i in range(1, 5)]
print(result)



# Задача 4. Список списков
# Дан многомерный список:
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# Напишите код, который раскрывает все вложенные списки, то есть оставляет
# лишь внешний список. Для решения используйте только list comprehensions.
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

output_list = [digit for sublist1 in nice_list for sublist2 in sublist1 for digit in sublist2]
print(output_list)



# Задача 5. Шифр Цезаря
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять
# русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу,
# которая изменит фразу при помощи шифра Цезаря.

def caesar_cipher(message, shift):

 alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
 result = []


 for char in message:
  if char in alphabet:
   index = alphabet.index(char)
   new_index = (index + shift) % len(alphabet)
   result.append(alphabet[new_index])
  else:
   result.append(char)

 return ''.join(result)


message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = caesar_cipher(message, shift)

print("Зашифрованное сообщение:", encrypted_message)



