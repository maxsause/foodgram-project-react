import re

from django.core.exceptions import ValidationError

regex = re.compile(r"^[a-zA-Z0-9]+$")


def validate_username(data):
    if re.fullmatch(regex, data):
        return data
    raise ValidationError(
        'Недопустимое имя пользователя!')
