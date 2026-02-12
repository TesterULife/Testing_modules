from baseclasses.response import Response

from schemas.users import User


def test_getting_users(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)

def test_another():
    assert 7 == 7


