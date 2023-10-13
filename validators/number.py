from fastapi import HTTPException


def zero_number(number: int):
    print("zero ", number)
    if number == 0:
        raise HTTPException(status_code=400, detail="Data validation error")
    return number
