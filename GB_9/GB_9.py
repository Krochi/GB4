# Набор рекламных данных, показывающих, щёлкнул ли конкретный
# пользователь рекламу на сайте компании или нет. Состоит из двух разных
# файлов: advertising_1.csv, advertising_2.csv. Описание столбцов
# датасета:
# ● Number: Номер пользователя в системе.
# ● Daily Time Spent on Site: Среднее ежедневное время нахождения
# пользователя на сайте в минутах.
# ● Daily Internet Usage: Среднее ежедневное время нахождения
# пользователя в интернете в минутах.
# ● Ad Topic Line: Заголовок рекламного объявления.
# ● Clicked on Ad: Кликнул пользователь на рекламу или нет.

# Задание 1.
# Загрузите таблицу из файла advertising_1.csv и сохраните её в датафрейм
# adv1_df. Укажите в качестве индекса столбец Number. Выведите на экран
# первые десять строк.
from turtle import pd

# Решение:

import pandas as pd
#
adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
# adv1_df.head(10)
# print(adv1_df)


# Задание 2.
# Выведите размер датафрейма adv1_df и cреднее ежедневное время
# нахождения в интернете пользователя под номером 8.

# Решение:

# adv1_df.shape
# result = adv1_df.loc[8, 'Daily Internet Usage']
#
# print(result)


# Задание 3.
# Загрузите таблицу из файла advertising_2.csv и сохраните её в датафрейм
# adv2_df. Укажите в качестве индекса стоблец Number. Выведите на экран
# строки для пользователей с номерами с 533-го по 536-й.

# Решение:

adv2_df = pd.read_csv('advertising_2.csv')
adv2_df = adv2_df.set_index('Number')

result = adv2_df.loc[533:536, :]
print(result)
