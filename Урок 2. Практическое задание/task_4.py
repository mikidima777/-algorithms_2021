"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""


def get_sum_seq(number_of_el):
    if number_of_el == 1:
        return [1, 1]
    else:
        prev = get_sum_seq(number_of_el - 1)
        new_elem = prev[0] * (-0.5)
        return [new_elem, prev[1] + new_elem]


seq_number = int(input('Введите количество элементов: '))
seq_sum = get_sum_seq(seq_number)
print(f'Количество элементов: {seq_number}, их сумма: {seq_sum[1]}.')
