from random import randrange

import pytest


@pytest.fixture
def get_number():
    return randrange(1, 1001, 5)

#unused
@pytest.fixture
def calculate():
    def _calculate(a, b):
        return a + b
    return _calculate


@pytest.fixture
def make_number():
    print("\nI'm getting number")
    number = randrange(1001, 5001, 5)
    yield
    print(f'\nNumber at home {number}')