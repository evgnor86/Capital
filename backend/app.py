import json

from pydantic import ValidationError
from fastapi import FastAPI

from db.engine import Session
from models.salary import YearSalary


get_err_msg = lambda e: json.loads(e.json())[0]['msg']

db_session = Session('salaries', YearSalary)
_data = db_session.read()

# _data = _data.years[2024]
# _data = _data.years[2024].months[1]
# print(f'{_data.model_dump_json(indent=2)}') 

for year in (2024,):
    for month in (10, 11, 12,):
        print(f'{_data.years[year].months[month].model_dump_json(indent=2)}')