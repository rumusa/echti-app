import hashlib
import re

class User:

    _email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if (re.fullmatch(self._email_regex, email)):
            self._email = email
        else:
            raise ValueError(f'{email} email address is not correct. Please enter a correct email address.')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password