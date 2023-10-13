from fastapi import HTTPException
from pydantic import parse_obj_as


def form_validation(data, model):
    for key, value in data:

        value = value.strip()

        if not value:
            raise HTTPException(status_code=400, detail="Data validation error")

    return parse_obj_as(model, data)
