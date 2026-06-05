from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print("update")


patient_info = {
    "name": "nitish",
    "email": "aditya@gmail.com",
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