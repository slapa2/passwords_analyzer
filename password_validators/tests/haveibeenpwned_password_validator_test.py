"""Test have i been pwned password validator"""
from password_validators.haveibeenpwned_password_validator import HaveibeenpwnedPasswordValidator


def test_has_been_pwned(requests_mock):
    """test if password has been powned"""
    requests_mock.get(
        'https://api.pwnedpasswords.com/range/B1B37',
        text='''FD9C3AE1A0892B3FFECD9608228DEEBCDED:5
FDA4292803BB5CE54BFBEB11CA56B79FC7E:1
FE45BC453E4F3CE1A62247210C85AD242C2:1
FE886AF5FC31DFA78B349BE06EACA2BCC5D:3
73A05C0ED0176787A4F1574FF0075F7521E:1
FF9E1DA839520ADC4730F40A3C0227E3704:1'''
    )

    validator = HaveibeenpwnedPasswordValidator()
    assert validator.validate('qwerty') == [f'Password has been pwned {1} times']


def test_has_not_been_pwned(requests_mock):
    """test if password has not been pwned"""
    requests_mock.get(
        'https://api.pwnedpasswords.com/range/B1B37',
        text='''FD9C3AE1A0892B3FFECD9608228DEEBCDED:5
FDA4292803BB5CE54BFBEB11CA56B79FC7E:1
FE45BC453E4F3CE1A62247210C85AD242C2:1
FE886AF5FC31DFA78B349BE06EACA2BCC5D:3
FF9E1DA839520ADC4730F40A3C0227E3704:1'''
    )

    validator = HaveibeenpwnedPasswordValidator()
    assert validator.validate('qwerty') == []


def test_has_been_pwned_les_then_max(requests_mock):
    """test if password has been pwned but less than 5 times"""
    requests_mock.get(
        'https://api.pwnedpasswords.com/range/B1B37',
        text='''FD9C3AE1A0892B3FFECD9608228DEEBCDED:5
FDA4292803BB5CE54BFBEB11CA56B79FC7E:1
FE45BC453E4F3CE1A62247210C85AD242C2:1
FE886AF5FC31DFA78B349BE06EACA2BCC5D:3
73A05C0ED0176787A4F1574FF0075F7521E:4
FF9E1DA839520ADC4730F40A3C0227E3704:1'''
    )

    validator = HaveibeenpwnedPasswordValidator(5)
    assert validator.validate('qwerty') == []


def test_has_been_pwned_more_then_max(requests_mock):
    """test if password has been pwned more than 5 times"""
    requests_mock.get(
        'https://api.pwnedpasswords.com/range/B1B37',
        text='''FD9C3AE1A0892B3FFECD9608228DEEBCDED:5
FDA4292803BB5CE54BFBEB11CA56B79FC7E:1
FE45BC453E4F3CE1A62247210C85AD242C2:1
FE886AF5FC31DFA78B349BE06EACA2BCC5D:3
73A05C0ED0176787A4F1574FF0075F7521E:6
FF9E1DA839520ADC4730F40A3C0227E3704:1'''
    )

    validator = HaveibeenpwnedPasswordValidator(5)
    assert validator.validate('qwerty') == [f'Password has been pwned {6} times']
