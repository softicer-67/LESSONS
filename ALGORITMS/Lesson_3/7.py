'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

import random

arr = [random.randint(1, 99) for _ in range(11)]
print('\n', arr)

mini_1 = min(arr)
min_ind = arr.index(mini_1)

del arr[min_ind]

mini_2 = min(arr)
print(' Два наименьших элемента в массиве', mini_1, 'и', mini_2)





