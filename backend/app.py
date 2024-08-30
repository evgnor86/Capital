import json
from typing import Optional

from pydantic import BaseModel, ValidationError, model_validator
from fastapi import FastAPI


class Salary(BaseModel):

    fst_half_hours: int
    snd_half_hours: int

    base_payment: float

    prepaid_bonus: float
    postpaid_bonus: float

    @model_validator(mode='after')
    def _validate(self):
        if self.base_payment <= 0:
            raise ValueError('Base payment must be > 0')
        else:
            return self

class MonthSalary(BaseModel):

    months: dict[int, Salary]

    @model_validator(mode='after')
    def _validate(self):
        if len(self.months) < 12:
            raise ValueError('Months count must be = 12')
        else:
            return self  

class MonthFinances(BaseModel):

    salary: MonthSalary      

class YearFinances(BaseModel):

    years: dict[int, MonthFinances]


get_err_msg = lambda e: json.loads(e.json())[0]['msg']

with open('finances.json', 'r') as raw_json:
    try:
        finances = YearFinances.model_validate_json(raw_json.read())
    except ValidationError as e:
        print(f'ValidationError: {get_err_msg(e)}')
    else:
        data = finances.years[2024].salary.months[1]
        print(data.model_dump_json(indent=2))
