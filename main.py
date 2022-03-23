"""Password analyzer"""

from password_validator import PasswordValidator


def main():
    """main password analyzer function"""
    print('Hello World')
    validator = PasswordValidator()
    print(validator.validate('123456'))


if __name__ == '__main__':
    main()
