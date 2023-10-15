from pydantic import BaseModel, validator
from validators.string import empty_string
from validators.number import zero_or_empty_number


class SignUp(BaseModel):
    username: str
    password: str
    number: int

    _empty_string = validator('username', 'password', allow_reuse=True)(empty_string)
    _zero_or_empty_number = validator('number', allow_reuse=True)(zero_or_empty_number)