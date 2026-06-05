from pydantic import  BaseModel

class Patient(BaseModel):

    name :str
    age:int
    weight:float
def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('update')

patient_info =  {'name': 'nitish','age':30,'weight':55.4}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
