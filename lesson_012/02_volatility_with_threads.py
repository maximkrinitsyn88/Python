# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import operator
import os
import threading
import time

secid_volatility = {}


class Volatility(threading.Thread):

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file

    def run(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            price_list = []
            for line in file:
                if "PRICE" not in line:
                    line = line.split(',')
                    price_list.append(line[2])
            min_price = float(min(price_list))
            max_price = float(max(price_list))
            half_sum = (min_price + max_price) / 2
            volatility = round(((max_price - min_price) / half_sum) * 100, 2)
            volatility_dict = dict({line[0]: volatility})
            secid_volatility.update(volatility_dict)
            print(volatility_dict, flush=True)


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)')
        return result
    return surrogate


def folder_unpacking(folder):
    files = []
    directory = os.listdir(folder)
    for file in directory:
        filepath = os.path.join(folder, file)
        files.append(filepath)
    return files


@time_track
def main():
    folder = './trades'
    volatility = [Volatility(file=file) for file in folder_unpacking(folder)]
    for vol in volatility:
        vol.start()
    for vol in volatility:
        vol.join()
    min_volatility = sorted(secid_volatility.items(), key=operator.itemgetter(1), reverse=False)[:3]
    max_volatility = sorted(secid_volatility.items(), key=operator.itemgetter(1), reverse=True)[:3]
    print('Максимальная волатильность:')
    for _ in max_volatility:
        _ = (str(_)[1:-1])
        print('      {_}'.format(_=_))
    print('Минимальная волатильность:')
    for _ in min_volatility:
        _ = (str(_)[1:-1])
        print('      {_}'.format(_=_))
    print('Нулевая волатильность:')
    for key, value in secid_volatility.items():
        if value == 0:
            print('      `{key}`, {value} '.format(key=key, value=value))


if __name__ == '__main__':
    main()
