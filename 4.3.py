class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def line_check(password):
    lines = [
        'qwertyuiop[]', 'asdfghjkl;', 'zxcvbnm,./',
        '][poiuytrewq', ';lkjhgfdsa', '/.,mnbvcxz',
        "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю.",
        "ъхзщшгнекуцй", "\эждлорпавыф", ".юбьтимсчя",
        "ё1234567890-=", "=-0987654321ё", "`1234567890-=", '=-0987654321`'
        ]
    extra = password.lower()
    for i in range(len(password) - 2):
        for line in lines:
            if extra[i] + extra[i + 1] + extra[i + 2] in line:
                return 'error'
    return False


def is_there_a_num(password):
    for elem in list(password):
        if elem.isdigit():
            return False
    return 'error'


def both_cases(password):
    for elem in password:
        if not elem.islower():
            continue
        else:
            for elem_ in password:
                if not elem_.isupper():
                    continue
                else:
                    break
            return False
    return 'error'


def check_password(password):
    if len(password) < 9:
        raise LengthError
    if is_there_a_num(password):
        raise DigitError
    if both_cases(password):
        raise LetterError
    if line_check(password):
        raise SequenceError
    return 'ok'

try:
    print(check_password('GБвИНddифпГxFGH'))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password('41157082'))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password('Еpert'))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password('WeR22'))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password('Hey297daw'))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password("U3UшHЪnDЧ5yш.yмЯpH"))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password("еПQSНгиfУЙ70qE"))
except Exception as error:
    print(error.__class__.__name__)

try:
    print(check_password("G7FgTU0bwТuio"))
except Exception as error:
    print(error.__class__.__name__)