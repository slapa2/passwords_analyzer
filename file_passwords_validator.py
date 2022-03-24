"""Program reads passwords from file and write correct passwords to anoder file"""

from password_validators.basic_password_validator import PasswordValidator


class FilePasswordValidator:
    """File Password Validator"""

    def __init__(self):
        self.validator = PasswordValidator()

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
                if not self.validator.validate(password):
                    output_file.write(f'{password}\n')
