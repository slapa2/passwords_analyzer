"""password_validator tests"""

from password_validators.basic_password_validator import PasswordValidator


def test_negative_validate_len():
    """test to short password validator"""
    validator = PasswordValidator(password_min_len=8)
    errors = validator.validate('1234567')
    assert "Password must have at least 8 characters" in str(errors)


def test_validate_len_positive():
    """test to short password validator"""
    validator = PasswordValidator(password_min_len=8)
    errors = validator.validate('12345678')
    assert "Password must have at least 8 characters" not in str(errors)


def test_positive_upper_lower_chars():
    """test lower and upper chars in password validator"""
    validator = PasswordValidator(lower_and_upper=True, special_characters=False)
    errors = validator.validate('1234Aa!@')
    assert "Password must have uppercase and lowercase characters" not in str(errors)


def test_negative_upper_lower_chars():
    """test lower and upper chars in password validator"""
    validator = PasswordValidator(lower_and_upper=True, special_characters=False)
    errors = validator.validate('1234aa!@')
    assert "Password must have uppercase and lowercase characters" in str(errors)


def test_positive_special_chars():
    """test special chars in password validator"""
    validator = PasswordValidator(lower_and_upper=False, special_characters=True)
    errors = validator.validate('1234Aa!@')
    assert "Password must have any special character" not in str(errors)


def test_negative_special_chars():
    """test special chars in password validator"""
    validator = PasswordValidator(lower_and_upper=False, special_characters=True)
    errors = validator.validate('1234AaBb')
    assert "Password must have any special character" in str(errors)
