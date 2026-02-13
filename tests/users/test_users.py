import pytest

from baseclasses.response import Response

from schemas.users import User


def test_getting_users(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.production
@pytest.mark.skip('For future updates')
def test_another():
    assert 7 == 7

@pytest.mark.development
@pytest.mark.parametrize(
    'first_value, second_value, result',[
        (1, 2, 3),
        (-1, 2, 1),
        (-7, -2, -9),
        ('a', 2, None),
        ('b', 'c', 'bc')

])

def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
