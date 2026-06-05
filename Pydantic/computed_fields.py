
from pydantic import BaseModel ,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):

    name:str
    email: EmailStr
    age: int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi   
    
def update_patient_data(patient:Patient):

        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('BMI',patient.calculate_bmi)

patient_info = {
    "name": "nitish",
    "email": "aditya@hdfc.com",
    "age": '30' ,
    "weight": 55.4,
    "height": 1.72,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "phone": "23234234"
           }

}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
