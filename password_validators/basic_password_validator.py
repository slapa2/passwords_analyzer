"""Password Validator"""
import string
from typing import List

from password_validators.password_validator_interface import PasswordValidatorInterface


class PasswordValidationException(Exception):
    """Exception is risen when password didn't pass validation"""


class ToShortPasswordException(PasswordValidationException):
    """Exception is risen when password is too short"""


class LowerCharsException(PasswordValidationException):
    """Exception is risen when password has no lowercase chars"""


class UpperCharsException(PasswordValidationException):
    """Exception is risen when password has no uppercase chars"""


class SpecialCharsException(PasswordValidationException):
    """Exception is risen when password hasn't any special character"""


class PasswordValidator(PasswordValidatorInterface):
    """Basic password validator"""

    def __init__(self,
                 password_min_len: int = 8,
                 lower_min_counter: int = 1,
                 upper_min_counter: int = 1,
                 special_min_counter: int = 1
                 ) -> None:

        self.password_min_len = password_min_len
        self.lower_min_counter = lower_min_counter
        self.upper_min_counter = upper_min_counter
        self.special_min_counter = special_min_counter

    def validate(self, password: str) -> List[str]:
        """Password validation method"""
        errors = []

        try:
            self._validate_len(password)
        except ToShortPasswordException as exc:
            errors.append(str(exc))

        try:
            self._validate_lower_chars(password)
        except LowerCharsException as exc:
            errors.append(str(exc))

        try:
            self._validate_upper_chars(password)
        except UpperCharsException as exc:
            errors.append(str(exc))

        try:
            self._validate_special_characters(password)
        except SpecialCharsException as exc:
            errors.append(str(exc))

        return errors

    def _validate_len(self, password: str) -> None:
        """validate password length"""
        if len(password) < self.password_min_len:
            raise ToShortPasswordException(
                f'Password must have at least {self.password_min_len} characters')

    def _validate_lower_chars(self, password:str) -> None:
        """validate if password has lower and upper characters"""
        lower = [x for x in password if x in string.ascii_lowercase]
        if len(lower) < self.lower_min_counter:
            raise LowerCharsException(
                f'Password must have at least {self.lower_min_counter} lowercase characters')

    def _validate_upper_chars(self, password:str) -> None:
        """validate if password has lower and upper characters"""
        upper = [x for x in password if x in string.ascii_uppercase]
        if len(upper) < self.upper_min_counter:
            raise UpperCharsException(
                f'Password must have at least {self.upper_min_counter} uppercase characters')

    def _validate_special_characters(self, password: str) -> None:
        """validate if password has any special character"""
        special = [x for x in password if x in string.punctuation]
        if len(special) < self.special_min_counter:
            raise SpecialCharsException(
                f'Password must have at least {self.special_min_counter} special characters')
