"""Password Validator"""
from typing import List


class PasswordValidationException(Exception):
    """Exception is risen when password didn't pass validation"""


class ToShortPasswordException(PasswordValidationException):
    """Exception is risen when password is too short"""


class UpperLowerCharsExeption(PasswordValidationException):
    """Exception is risen when password has only lowercase or uppercase chars"""


class SpecialCharsException(PasswordValidationException):
    """Exception is risen when password hasn't any special character"""


class PasswordValidator:
    """Basic password validator"""

    def __init__(self,
                 password_min_len: int = 8,
                 lower_and_upper: bool = True,
                 special_characters: bool = True
                 ) -> None:

        self.password_min_len = password_min_len
        self.lower_and_upper = lower_and_upper
        self.special_characters = special_characters

    def validate(self, password: str) -> List[str]:
        """Password validation method"""
        errors = []

        try:
            self._validate_len(password)
        except ToShortPasswordException as exc:
            errors.append(str(exc))

        try:
            self._validate_upper_and_lower_chars(password)
        except UpperLowerCharsExeption as exc:
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
                f'Password must have at least {self.password_min_len} characters'
            )

    def _validate_upper_and_lower_chars(self, password:str) -> None:
        """validate if password has lower and upper characters"""
        if not self.lower_and_upper:
            return
        if any([
            password.lower() == password,
            password.upper() == password
        ]):
            raise UpperLowerCharsExeption(
                'Password must have uppercase and lowercase characters'
            )

    def _validate_special_characters(self, password: str) -> None:
        """validate if password has any special character"""
        if not self.special_characters:
            return
        if password.isalnum():
            raise SpecialCharsException(
                'Password must have any special character'
            )
