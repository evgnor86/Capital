import json
from typing import Optional

from pydantic import BaseModel, ValidationError, field_validator
from fastapi import FastAPI


class Salary(BaseModel):

    fst_half_hours: int
    snd_half_hours: int

    base_payment: float

    prepaid_bonus: float
    postpaid_bonus: float

class MonthSalary(BaseModel):
    salary: Salary

class MonthFinances(BaseModel):

    months: dict[int, MonthSalary]

class YearFinances(BaseModel):

    years: dict[int, MonthFinances]


raw_json = """

{
  "years": 
  {
    "2024": 
    {
      "months": 
      {
        "1": 
        {
          "salary":
          {
            "fst_half_hours": 0,
            "snd_half_hours": 0,
            "base_payment": 0.00,
            "prepaid_bonus": 0.00,
            "postpaid_bonus": 0.00
          }
        }
      }
    }
  }
}

"""

finances = YearFinances.model_validate_json(raw_json)

print(finances.model_dump_json(indent=2))
