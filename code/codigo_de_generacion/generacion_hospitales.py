from faker import Faker
import random
from bson import ObjectId

fake = Faker("es_ES")

def generar_hospital():
    hospital = {
        "_id": ObjectId(),
        "nombre_hospital": f"Hospital {fake.city()}",
        "direccion": {
            "calle": fake.street_address(),
            "ciudad": fake.city(),
            "codigo_postal": fake.zipcode(),
            "pais": "España"
        },
        "departamentos": [generar_departamento("Cardiología"), generar_departamento("Neurología")],
        "contacto_emergencia": {
            "telefono": fake.phone_number(),
            "email": fake.email()
        }
    }
    return hospital

def generar_departamento(nombre):
    departamento = {
        "departamento_id": ObjectId(),
        "nombre": nombre,
        "extension": str(random.randint(1000, 9999)),
        "servicios": generar_servicios(nombre),
        "medicos": [generar_medico(nombre) for _ in range(random.randint(1, 3))]
    }
    return departamento

def generar_servicios(nombre_departamento):
    servicios = {
        "Cardiología": ["Consulta de cardiología", "Rehabilitación cardiaca", "Electrofisiología"],
        "Neurología": ["Consulta de neurología", "Terapia intensiva neurológica", "Unidad de epilepsia"]
    }
    return servicios.get(nombre_departamento, ["Consulta general"])

def generar_medico(especialidad):
    nombre = fake.name()
    medico = {
        "medico_id": ObjectId(),
        "nombre": nombre,
        "especialidad": especialidad,
        "años_experiencia": random.randint(5, 25),
        "horario": generar_horario()
    }
    return medico

def generar_horario():
    dias_laborales = random.sample(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], random.randint(2, 5))
    horas = f"{random.randint(8, 10)}:00 - {random.randint(14, 18)}:00"
    horario = {
        "dias_laborales": dias_laborales,
        "horas": horas
    }
    return horario

# Generación del hospital con datos aleatorios
hospital = generar_hospital()
print(hospital)
