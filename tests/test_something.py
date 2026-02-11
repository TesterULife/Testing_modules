import requests

from baseclasses.response import Response
from configurations import SERVICE_URL
from schemas.users import User


def test_getting_users():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)
