'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
'''

import sys

res = {}
for i in range(2, 10):
    res[i] = []
    for j in range(2, 100):
        if j % i == 0:
            res[i].append(j)
    print(f'Числу {i} кратны {len(res[i])} чисел: {res[i]}')


sum_size = 0
sum_size1 = 0
sum_size2 = 0
sum_size += sys.getsizeof(i)
sum_size1 += sys.getsizeof(print)
sum_size2 += sys.getsizeof(res)

print('\nПеременные занимают:', sum_size, sum_size1, sum_size2)

'''
Переменные занимают: 28 72 360
'''