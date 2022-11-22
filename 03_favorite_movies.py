#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
s1 = my_favorite_movies[0:10:1]
s2 = my_favorite_movies[42:57:1]
s3 = my_favorite_movies[12:25:1]
s4 = my_favorite_movies[35:40:1]
print(s1)
print(s2)
print(s3)
print(s4)