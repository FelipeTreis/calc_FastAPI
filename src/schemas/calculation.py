from pydantic import BaseModel


class ParamModel(BaseModel):
    first_param: float
    second_param: float


class ResultModel(BaseModel):
    calculation: float
