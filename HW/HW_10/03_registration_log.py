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

class NotNameError(BaseException):
    pass


class NotEmailError(BaseException):
    pass


class FileVerification:

    def __init__(self, file, registrations_good, registrations_bad):
        self.file = file
        self.registrations_good = registrations_good
        self.registrations_bad = registrations_bad
        self.list_registrations_good = []
        self.list_registrations_bad = []

    def open_file(self):
        with open(self.file, 'r', encoding='utf-8') as file_to_check:
            for line in file_to_check:
                if line.endswith('\n'):
                    line = line[:-1]
                try:
                    self.check_all_fields(line)
                except ValueError as ecx:
                    self.list_registrations_bad.append(f'[{line}] - {ecx}')
                    continue
                except NotNameError:
                    self.list_registrations_bad.append(f'[{line}] - Поле имени содержит НЕ только буквы')
                    continue
                except NotEmailError:
                    self.list_registrations_bad.append(f'[{line}] - Поле емейл НЕ содержит @ и .(точку)')
                    continue
                self.list_registrations_good.append(f'[{line}]')

    def check_all_fields(self, line):
        words = line.split(' ')
        if len(words) != 3:
            raise ValueError('Не все поля заполнены')
        field_name, field_email, field_age = words
        field_name = str(field_name)
        field_email = str(field_email)
        field_age = int(field_age)
        for letter in field_name:
            if not (('а' <= field_name.lower() <= 'я') or (letter == 'ё')):
                raise NotNameError
        if not (10 <= field_age <= 99):
            raise ValueError('Поле возраст НЕ является числом от 10 до 99')
        if ('@' not in field_email) or ('.' not in field_email):
            raise NotEmailError

    def write_file(self):
        with open(self.registrations_bad, 'w', encoding='utf-8') as file_bad:
            for i in self.list_registrations_bad:
                file_bad.write(i + '\n')

        with open(self.registrations_good, 'w', encoding='utf-8') as file_good:
            for i in self.list_registrations_good:
                file_good.write(i + '\n')


check = FileVerification(file='registrations.txt', registrations_good='registrations_good.log.txt',
                         registrations_bad='registrations_bad.log.txt')

check.open_file()
check.write_file()
