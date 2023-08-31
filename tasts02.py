#Функции-редуцеры для списков: Напишите функцию-редуктор, которая принимает список строк и возвращает строку, состоящую из объединенных элементов списка через запятую. Например, для списка ["apple", "banana", "cherry"] результат должен быть "apple, banana, cherry".
from functools import reduce

def concat(a, b):
    return a + b

strings = ["apple", "banana", "cherry"]
delim = ', '
s = delim.join(strings)
result = reduce(concat, s)

print(result)