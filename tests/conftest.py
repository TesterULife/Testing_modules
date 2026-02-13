from random import randrange

import pytest

from generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player


@pytest.fixture
def get_number():
    return randrange(1, 1001, 5)


# unused
@pytest.fixture
def calculate():
    def _calculate(a, b):
        try:
            return a + b
        except TypeError:
            return None

    return _calculate



