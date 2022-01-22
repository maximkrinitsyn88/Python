import random
from termcolor import cprint, colored


def guess_the_number():
    hidden_number = [random.randint(1, 9)]
    while len(hidden_number) != 4:
        digit = random.randint(0, 9)
        if digit not in hidden_number:
            hidden_number.append(digit)
    hidden_number = ''.join(str(i) for i in hidden_number)
    return hidden_number


def checking_the_entered_number():
    while True:
        number = input(colored('Введите число: ', color='blue'))
        if len(str(number)) != len(set(str(number))):
            cprint('Цифры должны быть разные')
            return False # так четче
        elif number == '':
            cprint('Введите четырехзначное число')
            return False
        elif int(number[0]) == 0:
            cprint('Нельзя начинать с нуля')
            return False
        elif int(number) > 9999:
            cprint('Введите четырехзначное число')
            return False
        elif int(number) < 1000:
            cprint('Введите четырехзначное число')
            return False
        else:
            return number


def check_win(number, hidden_number):
    bulls_and_cows = compare_numbers(str(number), str(hidden_number))
    cprint(bulls_and_cows, color='magenta')
    if bulls_and_cows['Bulls'] == 4:
        cprint(colored('Игра окончена', color='yellow'))
        return True


def compare_numbers(number, hidden_number):
    quantity_bulls = 0
    quantity_cows = 0
    bulls_and_cows = {'Bulls': quantity_bulls, 'Cows': quantity_cows}
    for index_holder, numeric_holder in enumerate(hidden_number):
        for index_number, numeric_number in enumerate(number):
            if numeric_holder == numeric_number and index_holder == index_number:
                quantity_bulls += 1
                bulls_and_cows.update({'Bulls': quantity_bulls})
            elif numeric_holder == numeric_number:
                quantity_cows += 1
                bulls_and_cows.update({'Cows': quantity_cows})
    return bulls_and_cows


# def guess_the_number():
#     hidden_number = []
#     for _ in range(0, 10):
#         hidden_number.append(_)
#     hidden_number = random.sample(hidden_number, 4)
#     if hidden_number[0] == 0:
#         random.shuffle(hidden_number)
#     hidden_number = ''.join(str(i) for i in hidden_number)
#     return hidden_number


# return not (number[0] == '0' or len(str(number)) != 4 or len(number) != len(set(number)))

