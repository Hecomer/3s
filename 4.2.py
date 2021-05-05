class FormatError(Exception):
    pass


class NumberError(Exception):
    pass


def check_ph_num():
    phone_num = input()
    if phone_num.startswith('8'):
        phone_num = phone_num.replace('8', '+7', 1)
    elif not phone_num.startswith('+7'):
        raise FormatError('Неверный формат')

    phone_num = phone_num.replace(' ', '')

    if '(' in phone_num or ')' in phone_num:
        if phone_num.count('(') == 1 and phone_num.count(')') == 1:
            if phone_num.find('(') < phone_num.find(')'):
                phone_num = phone_num.replace('(', '')
                phone_num = phone_num.replace(')', '')
        else:
            raise FormatError('Неверный формат')

    if '-' in phone_num and (phone_num[-1] == '-' or phone_num[0] == '-' or '--' in phone_num):
        raise FormatError('Неверный формат')
    else:
        phone_num = phone_num.replace('-', '')

    for char in phone_num:
        if not char.isdigit() and char != '+':
            raise FormatError('Неверный формат')

    if len(phone_num) != 12:
        raise NumberError('Неверное количество цифр')

    return phone_num


print(check_ph_num())