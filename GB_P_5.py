#Задание1:

# import copy
#
#
# def change_value(struct, key, new_value):
#     """Рекурсивно ищет и заменяет значение по ключу в словаре."""
#     if key in struct:
#         struct[key] = new_value
#     for k, v in struct.items():
#         if isinstance(v, dict):
#             change_value(v, key, new_value)
#
#
# def make_site(product_name):
#     """Создает структуру сайта для продукта с заданным названием."""
#     site_template = {
#         'html': {
#             'head': {
#                 'title': 'Куплю/продам телефон недорого'
#             },
#             'body': {
#                 'h2': 'У нас самая низкая цена на iPhone',
#                 'div': 'Купить',
#                 'p': 'Продать'
#             }
#         }
#     }
#     # Глубокое копирование шаблона
#     site_copy = copy.deepcopy(site_template)
#
#     # Замена значений в шаблоне
#     change_value(site_copy, 'title', f'Куплю/продам {product_name} недорого')
#     change_value(site_copy, 'h2', f'У нас самая низкая цена на {product_name}')
#
#     return site_copy
#
#
# def display_struct(struct, spaces=0):
#     """Рекурсивно выводит ключи и значения структуры словаря с отступами."""
#     indent = ' ' * spaces
#     for key, value in struct.items():
#         if isinstance(value, dict):
#             print(f"{indent}{key}:")
#             display_struct(value, spaces + 4)
#         else:
#             print(f"{indent}{key}: {value}")
#
#
# def main():
#     sites_count = int(input("Сколько сайтов: "))
#     sites = []
#
#     for _ in range(sites_count):
#         product_name = input("Введите название продукта для нового сайта: ")
#         site = make_site(product_name)
#         sites.append(site)
#
#         # Вывод всех сайтов в списке
#         for idx, site in enumerate(sites, 1):
#             print(f"\nСайт для {product_name}:")
#             display_struct(site)
#             print()  # Отступ между сайтами
#
#
# if __name__ == "__main__":
#     main()





#Заданаие2:

# def find_key(struct, key, max_depth=None, depth=1):
#     # Проверка на превышение максимальной глубины
#     if max_depth is not None and depth > max_depth:
#         return None
#
#     # Если ключ найден на текущем уровне
#     if key in struct:
#         return struct[key]
#
#     # Если ключ не найден, продолжаем поиск в подсловарях
#     for k, v in struct.items():
#         if isinstance(v, dict):
#             result = find_key(v, key, max_depth, depth + 1)
#             if result is not None:
#                 return result
#
#     # Если ключ не найден на всех уровнях
#     return None
#
#
# # Пример использования функции
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# # Пример 1
# key_to_find = 'head'
# print(find_key(site, key_to_find))  # {'title': 'Мой сайт'}
#
# # Пример 2
# key_to_find = 'head'
# max_depth = 1
# print(find_key(site, key_to_find, max_depth))  # None
#
# # Пример 3
# key_to_find = 'title'
# print(find_key(site, key_to_find))  # 'Мой сайт'
#
# # Пример 4
# key_to_find = 'title'
# max_depth = 2
# print(find_key(site, key_to_find, max_depth))  # 'Мой сайт'
#
# # Пример 5
# key_to_find = 'div'
# max_depth = 1
# print(find_key(site, key_to_find, max_depth))  # None




#Задание3:

# def my_sum(*args):
#     total_sum = 0
#
#     def helper(arg):
#         nonlocal total_sum
#         if isinstance(arg, int):
#             total_sum += arg
#         elif isinstance(arg, (list, tuple)):
#             for item in arg:
#                 helper(item)
#
#     for item in args:
#         helper(item)
#
#     return total_sum
#
# # Основной код для тестирования (закомментирован)
# print(my_sum([[1, 2, [3]], [1], 3]))  # Ожидаемый результат: 10
# print(my_sum(1, 2, 3, 4, 5))         # Ожидаемый результат: 15


#Задание4:

def flatten(a_list):
    result = []
    for element in a_list:
        if isinstance(element, int):
            result.append(element)
        elif isinstance(element, list):
            result.extend(flatten(element))
    return result

# Пример использования:
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
flattened_list = flatten(nice_list)
print(flattened_list)

