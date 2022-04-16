"""Password analyzer"""
from password_validators.validator import Validator


def main():
    """main password analyzer function"""

    validator = Validator()
    interface = """
    1. validate passwords from file2
    2. single passeord validation
    3. exit program
    """

    while (option := input(interface)) != '3':
        if option == '1':
            validator.validate_file()
            print('passwords from file: var/passwords.csv were validated')
        elif option == '2':
            password = input('enter password to valite: ')
            errors = validator.validate_password(password)
            if not errors:
                print('password is valid')
                continue

            for error in errors:
                print(error)


if __name__ == '__main__':
    main()
