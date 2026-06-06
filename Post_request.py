from IPython import core
from IPython import core
from dns import grange
from functools import _Descriptor
from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,Feild,computed_field
from typing import Annotated,Literal
import json
app= FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Feild(..., description='ID of the patient',examples=['P001'])]
    name:Annotated[str,Feild(..., description='Name of the patient')]
    city:Annotated[str,Feild(...,description='city where the patient is liying')]
    age:Annotated[int,Feild(...,gt=0,lt=120,decription='Age of the patient')]
    gender: Annotated[Literal['male','Female','Other'],Feild(..., decrition='Gender of the patient')]
    height:Annotated[float,Feild(...,gt=0,description='Height of the patient in mtrs')]
    weight: Annotated[float,Feild(...,gt=0,description='Weight of the patient in kgs')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def  verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi <30:
            return 'Normal'

        else:
            return 'Obese'
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data