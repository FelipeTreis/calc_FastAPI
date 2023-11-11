from fastapi import FastAPI

from src.schemas.calculation import ParamModel, ResultModel

app = FastAPI()


@app.post("/add", response_model=ResultModel)
def add(payload: ParamModel):
    return {"calculation": payload.first_param + payload.second_param}

@app.post("/subtract", response_model=ResultModel)
def add(payload: ParamModel):
    return {"calculation": payload.first_param - payload.second_param}

@app.post("/mutiply", response_model=ResultModel)
def add(payload: ParamModel):
    return {"calculation": payload.first_param * payload.second_param}

@app.post("/divide", response_model=ResultModel)
def add(payload: ParamModel):
    return {"calculation": payload.first_param / payload.second_param}
