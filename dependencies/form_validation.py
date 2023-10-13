from fastapi import HTTPException
from pydantic import parse_obj_as

# sample class dependency only
class FormValidation:
    def __init__(
            self,
            data,
            model
    ):
        self.data = data
        self.model = model

    def __call__(self):
        data = self.data
        model = self.model

        for key, value in data:
            print(key, value)
            if not value:
                raise HTTPException(status_code=400, detail="Data validation error")

        return parse_obj_as(model, data)
