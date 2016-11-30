from flask import current_app

from fixtures import hashed_password, plaintext_password, user


class DescribeUser:
    def it_hashes_password_when_reseting_it(
        self, user, plaintext_password, hashed_password
    ):
        user.password = plaintext_password
        assert user.password == hashed_password
