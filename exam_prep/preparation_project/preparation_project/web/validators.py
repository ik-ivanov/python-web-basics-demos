from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def max_length_validator(value):
    max_length = 15
    if len(value) > max_length:
        raise ValidationError(f'Ensure this value has at most {max_length} characters.')


@deconstructible
class MaxLengthClassValidator:
    def __init__(self, max_length):
        self.max_length = max_length

    def __call__(self, value):
        if len(value) > self.max_length:
            raise ValidationError(f'Ensure this value has at most {self.max_length} characters.')

    def __eq__(self, other):
        return self.max_length == other.max_length


@deconstructible
class TextContainsOnlyAlphaNumericAndUnderscoreValidator:
    def __call__(self, value):

        # char.isalnum() or char == '_' - returns True if char is alphanumeric or '_'
        # value.isalnum() and '_' not in value - wrong

        # regex: ^[a-zA-Z0-9_]+$ - ^ - start of string, $ - end of string
        # use in RegexValidator

        for char in value:
            if not (char.isalnum() or char == '_'):
                raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

    def __eq__(self, other):
        return True


@deconstructible
class CustomFloatPositiveValidator:
    def __call__(self, value):
        if value < 0.0:
            raise ValidationError('Ensure this value is greater than or equal to 0.0.')

    def __eq__(self, other):
        return True