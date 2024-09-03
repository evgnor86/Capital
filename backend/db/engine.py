import json
from typing import Any

from pydantic import ValidationError
from models.salary import YearSalary


get_err_msg = lambda e: json.loads(e.json())[0]['msg']


class Session:

    _document_name: str
    _document_model: Any
    _storage_path: str
    _data: Any

    def __init__(self, 
                 document_name: str,
                 document_model,
                 storage_path: str = '/storage',
                 ) -> None:
        
        self._document_name = document_name
        self._document_model = document_model
        self._storage_path = storage_path

    # generate data -> write file
    def create(self) -> Any:
        pass

    # read file -> return data
    def read(self) -> Any:
        with open(f'./{self._storage_path}/{self._document_name}.json', 'r') as raw_json:
            try:
                self._data = self._document_model.model_validate_json(raw_json.read())
            except ValidationError as e:
                print(f'ValidationError: {get_err_msg(e)}')
                return None
            else:
                # data = salaries.years[2024]
                # data = salaries.years[2024].years[2024].months[1]
                # print(f'{self._data.model_dump_json(indent=2)}') 
                return self._data

    # read file -> add/replace data -> write file
    def update(self) -> Any:
        pass

    # read file -> remove data -> write file
    def delete(self) -> Any:
        pass