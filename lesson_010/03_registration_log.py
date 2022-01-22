# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __str__(self):
        return 'Поле имени содержит не только буквы'


class NotEmailError(Exception):

    def __str__(self):
        return 'Поле емейл НЕ содержит @ и .(точку)'


class CheckingUserData:

    def __init__(self, filename, filename_correct_data, filename_wrong_data):
        self.filename = filename
        self.filename_correct_data = filename_correct_data
        self.filename_wrong_data = filename_wrong_data
        self.valid_lines = []
        self.wrong_lines = []

    def run(self):
        self.read_file()
        self.write_correct_data()
        self.write_wrong_data()

    def read_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    valid_line = self.string_validation(line)
                    self.valid_lines.append(valid_line)
                except ValueError as exc:
                    if 'unpack' in exc.args[0]:
                        lack_of_data = f'Не хватает данных в строке {line}'[:-1]
                        self.wrong_lines.append(lack_of_data)
                    else:
                        wrong_range = f'Поле возраст НЕ является числом от 10 до 99 в строке {line}'[:-1]
                        self.wrong_lines.append(wrong_range)
                except NotNameError as nne:
                    wrong_name = f'{nne} в строке {line}'[:-1]
                    self.wrong_lines.append(wrong_name)
                except NotEmailError as nee:
                    wrong_email = f'{nee} в строке {line}'[:-1]
                    self.wrong_lines.append(wrong_email)

    def string_validation(self, line):
        name, email, age = line.split(' ')
        name = str(name)
        age = int(age)
        if 10 < age < 99:
            if name.isalpha():
                if ('@' and '.') in email:
                    valid = '{name} {email} {age}'.format(name=name, email=email, age=age)
                else:
                    raise NotEmailError()
            else:
                raise NotNameError()
        else:
            raise ValueError('Невалидные данные')
        return valid

    def write_correct_data(self):
        with open(self.filename_correct_data, 'w', encoding='utf-8') as fcd:
            for line in self.valid_lines:
                line = ('{line}\n'.format(line=line))
                fcd.write(line)

    def write_wrong_data(self):
        with open(self.filename_wrong_data, 'w', encoding='utf-8') as fwd:
            for line in self.wrong_lines:
                line = ('{line}\n'.format(line=line))
                fwd.write(line)


check_user = CheckingUserData(filename='registrations.txt', filename_correct_data='registrations_good.log',
                              filename_wrong_data='registrations_bad.log')
check_user.run()
# зачет!
