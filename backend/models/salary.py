from typing import Optional

from pydantic import BaseModel, model_validator


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

class YearSalary(BaseModel):

    years: dict[int, MonthSalary]