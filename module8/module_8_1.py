#Реализуйте следующую функцию:
#add_everything_up, будет складывать числа(int, float) и строки(str)
from sys import excepthook
from unittest import expectedFailure

from калькулятор import button_sub

#Описание функции:
#add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
#TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.


def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if isinstance(a, str):
            b = str(b)
        else :
            a = str(a)
    finally:
        return a + b
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
