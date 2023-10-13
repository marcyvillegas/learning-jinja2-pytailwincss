from fastapi import HTTPException


def empty_string(string: str):
    string = string.strip()

    if not string:
        raise HTTPException(status_code=400, detail="Data validation error")
    return string
