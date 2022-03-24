"""Password analyzer"""
from file_passwords_validator import FilePasswordValidator


def main():
    """main password analyzer function"""

    validator = FilePasswordValidator()
    validator.validate()


if __name__ == '__main__':
    main()
