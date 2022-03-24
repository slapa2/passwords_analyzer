"""haveibeenpwned.com api based password validator"""

from hashlib import sha1
from typing import List

import requests

from password_validators.password_validator_interface import PasswordValidatorInterface


def _ask_api(password: str) -> int:
    """get pwned password count from api"""
    byte_password = password.encode('utf-8')
    hashed_password = sha1(byte_password).hexdigest().upper()
    request = requests.get(f'https://api.pwnedpasswords.com/range/{hashed_password[:5]}')
    api_data = {x.split(':')[0]: x.split(':')[1] for x in request.text.splitlines()}
    try:
        pwned_counter = int(api_data[hashed_password[5:]])
    except KeyError:
        pwned_counter = 0
    return pwned_counter


class HaveibeenpwnedPasswordValidator(PasswordValidatorInterface):
    """This validator is checking password with haveibeenpwnd.com api"""

    def __init__(self, max_pwned: int = 0):
        self.max_pwned = max_pwned

    def validate(self, password: str) -> List[str]:
        """validate password"""
        pwned_counter = _ask_api(password)
        if pwned_counter <= self.max_pwned:
            return []
        return [f'Password has been pwned {pwned_counter} times']
