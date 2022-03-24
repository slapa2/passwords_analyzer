"""Password Validator Interface"""

from abc import ABC, abstractmethod


class PasswordValidatorInterface(ABC):
    """Interface for password validator classes"""

    @abstractmethod
    def validate(self, password: str) -> bool:
        """
        Password validate method returns True if password is valid,
        if not returns False
        """
