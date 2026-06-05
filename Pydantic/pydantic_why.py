from multiprocessing import Value
from pydantic import BaseModel, EmailStr, AnyUrl,Field,field_validator,model_validator
from typing import List, Dict, Optional,Annotated


class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',
    description='Give the name of the patient in less than 50 chars',examples=['Nitish','Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0,lt=120)
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com','icici.com']
        # abc@gmail.com

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0< value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

@model_validator(mode='after')
def validate_emergency_contact(cls,model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print("update")


patient_info = {
    "name": "nitish",
    "email": "aditya@hdfc.com",
    "linkedin_url": "https://linkedin.com",  # Fixed
    "age": 30,
    "weight": 55.4,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "phone": "23234234"
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)