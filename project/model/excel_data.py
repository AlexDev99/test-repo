from pydantic import BaseModel


class ExcelData(BaseModel):
    id: int
    name: str
