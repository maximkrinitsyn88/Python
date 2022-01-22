# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# # Часть 1
# # На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# # который выдает последовательность простых чисел до n
# #
# # Распечатать все простые числа до 10000 в столбик
#
#
# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.prime_numbers = []
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i < self.n:
#             for self.i in range(2, self.n + 1):
#                 for prime in self.prime_numbers:
#                     if self.i % prime == 0:
#                         break
#                 else:
#                     self.prime_numbers.append(self.i)
#                     return self.i
#             else:
#                 raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=1000)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
# if number == 7:
#     return
#
#
# prime_numbers_generator = prime_numbers_generator(n=10000)
# print(prime_numbers_generator)
# for number in prime_numbers_generator:
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def prime_numbers_generator(*func, n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if func[0](number) and func[1](number):
                yield ['Простое счастливое палиндромное число', number]
            elif func[0](number):
                yield ['Простое палиндромное число', number]
            elif func[1](number):
                yield ['Простое счастливое число', number]
            elif func[2](number):
                yield ['Простое число, входящее в список чисел Фибоначчи', number]
            else:
                yield False


def happiness_filter(number):
    number = str(number)
    numb_len = len(number)
    numb_index = numb_len // 2
    first_numb = number[:numb_index]
    if len(number) <= 1:
        return False
    elif numb_len % 2 == 0:
        second_numb = number[numb_index:]
    else:
        second_numb = number[(numb_index + 1):]
    sum_first = sum(map(int, first_numb))
    sum_second = sum(map(int, second_numb))
    if sum_first == sum_second:
        return True


def palindromic_filter(number):
    number = str(number)
    if len(number) <= 1:
        return False
    elif number == number[::-1]:
        return True


def fib_numbers(number):
    fib_list = []
    fib1 = fib2 = 1
    for _ in range(1, 21):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib1)
    if number in fib_list:
        return True


filter_function_generator = prime_numbers_generator(palindromic_filter, happiness_filter, fib_numbers, n=10000)
print(filter_function_generator)
for numb in filter_function_generator:
    if numb:
        print(numb)
