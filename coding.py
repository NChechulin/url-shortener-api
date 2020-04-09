from random import choice
import validation
import string
import db


alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase


def __generate_code(size=7):
    """generates random string"""
    return ''.join([choice(alphabet) for _ in range(size)])


def try_encode(user_input):
    """returns code, if user_input is a valid URL"""
    if validation.validate_url(user_input):
        url = user_input.strip()
        code = db.try_get_code(url)

        # if code is occupied, generate a new one with different length
        while not validation.validate_code(code):
            code = __generate_code(8)

        return code
    return None
