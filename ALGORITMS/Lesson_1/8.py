"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""

x = int(input('Введите год: '))
if x % 4 == 0:
    print('Этот год високосный')
else:
    print('Этот год обычный')
