"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random
import sys


def menu():
    print('\n\tМЕНЮ:\n')
    print('[1] Вывести случайное целое число')
    print('[2] Случайное вещественное число')
    print('[3] Случайный символ')
    print('[0] Выход')


menu()
option = input()

while option != '0':
    if option == '1':
        print(random.randint(1, 100))
    elif option == '2':
        print(float(random.randrange(100)))
    elif option == '3':
        print(random.choice('abcdef'))

    if __name__ == '__main__':
        option = input()






