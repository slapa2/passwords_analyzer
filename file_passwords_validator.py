"""Program reads passwords from file and write correct passwords to anoder file"""

from password_validators.basic_password_validator import PasswordValidator
from password_validators.haveibeenpwned_password_validator import HaveibeenpwnedPasswordValidator


class FilePasswordValidator:
    """File Password Validator"""

    def __init__(self):
        self.basic_validator = PasswordValidator()
        self.haveibeenpwned_validator = HaveibeenpwnedPasswordValidator()

    def validate(
            self,
            passwords_file: str = 'var/passwords.csv',
            correct_passwords_file:str = 'var/correct_passwords.csv'
    ):
        """Validate passwords form password_file and write correct to output_file"""

        with open(passwords_file, 'r', encoding='utf8') as input_file, \
                open(correct_passwords_file, 'w', encoding='utf8') as output_file:
            for password in input_file:
                password = password.rstrip()
                errors = []
                errors.extend(self.basic_validator.validate(password))
                errors.extend(self.haveibeenpwned_validator.validate(password))
                if not errors:
                    output_file.write(f'{password}\n')
