from fastapi import HTTPException


def zero_or_empty_number(number: int):
    if number == 0 or not number:
        raise HTTPException(status_code=400, detail="Data validation error")
    return number
