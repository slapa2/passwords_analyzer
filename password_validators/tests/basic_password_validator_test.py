"""password_validator tests"""

from password_validators.basic_password_validator import PasswordValidator


def test_negative_validate_len():
    """test to short password validator"""
    validator = PasswordValidator(password_min_len=8, upper_min_counter=0, lower_min_counter=0, special_min_counter=0)
    errors = validator.validate('1234567')
    assert "Password must have at least 8 characters" in str(errors)


def test_validate_len_positive():
    """test to short password validator"""
    validator = PasswordValidator(password_min_len=8, upper_min_counter=0, lower_min_counter=0, special_min_counter=0)
    errors = validator.validate('12345678')
    assert "Password must have at least 8 characters" not in str(errors)


def test_positive_lower_chars():
    """test lowercase chars in password validator"""
    validator = PasswordValidator(upper_min_counter=0, lower_min_counter=1, special_min_counter=0)
    errors = validator.validate('1234Aa!@')
    assert "Password must have at least 1 lowercase characters" not in str(errors)


def test_negative_lower_chars():
    """test lowercase chars in password validator"""
    validator = PasswordValidator(upper_min_counter=0, lower_min_counter=1, special_min_counter=0)
    errors = validator.validate('1234AA!@')
    assert "Password must have at least 1 lowercase characters" in str(errors)


def test_positive_upper_chars():
    """test uppercase chars in password validator"""
    validator = PasswordValidator(upper_min_counter=1, lower_min_counter=0, special_min_counter=0)
    errors = validator.validate('1234Aa!@')
    assert "Password must have at least 1 uppercase characters" not in str(errors)


def test_negative_upper_chars():
    """test uppercase chars in password validator"""
    validator = PasswordValidator(upper_min_counter=1, lower_min_counter=0, special_min_counter=0)
    errors = validator.validate('1234aa!@')
    assert "Password must have at least 1 uppercase characters" in str(errors)


def test_positive_special_chars():
    """test special chars in password validator"""
    validator = PasswordValidator(upper_min_counter=0, lower_min_counter=0, special_min_counter=1)
    errors = validator.validate('1234Aa!@')
    assert "Password must have at least 1 special characters" not in str(errors)


def test_negative_special_chars():
    """test special chars in password validator"""
    validator = PasswordValidator(upper_min_counter=0, lower_min_counter=0, special_min_counter=1)
    errors = validator.validate('1234AaBb')
    assert "Password must have at least 1 special characters" in str(errors)
