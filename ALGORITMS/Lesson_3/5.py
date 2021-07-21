'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

import random

arr = [random.randint(-100, 100) for i in range(10)]
print('\n', arr)
print('\n Максимальный отрицательный элемент:', min(arr))

for i in range(len(arr)):
    mini = min(arr)
    ind = arr.index(mini)
print(' Находится на позиции:', ind + 1)
