from pydantic import BaseModel, field_validator

from enums.user_enums import Genders, Statuses

class User(BaseModel):
    id: int
    name: int
    email: str
    gender: Genders
    status: Statuses

    @field_validator('email')
    def check_that_dog_in_email_adress(cls, email):
        unusable_symb = ' ()[]{}<>,"\'\\|/:;!?+=*&^%$#~`'

        for ch in email:
            if ch in unusable_symb:
                raise ValueError("Invalid character in email")

        if email.count('@') != 1:
            raise ValueError("Email must contain one @")

        local, domain = email.split('@')

        if not local or not domain:
            raise ValueError("Invalid email structure")

        if '.' not in domain:
            raise ValueError("Domain must contain dot")

        return email
