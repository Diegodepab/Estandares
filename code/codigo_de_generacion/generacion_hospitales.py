from faker import Faker
import random
from bson import ObjectId
import json

# Configuración de Faker
fake = Faker("es_ES")
Faker.seed(0)

# Definición de departamentos y servicios
departamentos_servicios = {
    "Cardiología": ["Consulta de cardiología", "Rehabilitación cardiaca", "Electrofisiología", "Ecocardiografía", "Cardiología intervencionista"],
    "Neurología": ["Consulta de neurología", "Terapia intensiva neurológica", "Unidad de epilepsia", "Estudio del sueño", "Neurofisiología"],
    "Oncología": ["Consulta de oncología", "Quimioterapia", "Radioterapia", "Inmunoterapia", "Oncología pediátrica"],
    "Pediatría": ["Consulta de pediatría", "Urgencias pediátricas", "Unidad de neonatología", "Cuidados intensivos pediátricos", "Pediatría de atención ambulatoria"],
    "Ginecología": ["Consulta de ginecología", "Unidad de fertilidad", "Control prenatal", "Ginecología oncológica", "Salud reproductiva"],
    "Traumatología": ["Consulta de traumatología", "Cirugía ortopédica", "Rehabilitación física", "Unidad de fracturas", "Terapia de dolor"],
    "Dermatología": ["Consulta de dermatología", "Dermatología oncológica", "Tratamientos láser", "Dermatología estética", "Alergias cutáneas"],
    "Oftalmología": ["Consulta de oftalmología", "Cirugía de cataratas", "Retinopatía", "Tratamientos de glaucoma", "Terapia de visión"],
    "Endocrinología": ["Consulta de endocrinología", "Tratamiento de diabetes", "Trastornos tiroideos", "Control de peso", "Endocrinología pediátrica"],
    "Gastroenterología": ["Consulta de gastroenterología", "Endoscopia", "Hepatología", "Unidad de colonoscopia", "Tratamiento de enfermedad inflamatoria intestinal"],
    "Reumatología": ["Consulta de reumatología", "Unidad de artritis", "Terapia de osteoporosis", "Tratamiento de lupus", "Control de espondilitis"],
    "Neumología": ["Consulta de neumología", "Función pulmonar", "Unidad de asma", "Terapia de apnea del sueño", "Tratamiento de EPOC"],
    "Psiquiatría": ["Consulta de psiquiatría", "Terapia psicológica", "Unidad de salud mental", "Tratamiento de adicciones", "Psiquiatría infantil"],
    "Cirugía general": ["Consulta de cirugía", "Cirugía laparoscópica", "Cirugía de hernias", "Urgencias quirúrgicas", "Unidad de cirugía ambulatoria"],
    "Urología": ["Consulta de urología", "Urología oncológica", "Tratamiento de cálculos renales", "Endourología", "Disfunción eréctil"],
    "Nefrología": ["Consulta de nefrología", "Diálisis", "Transplante renal", "Tratamiento de insuficiencia renal", "Control de hipertensión"],
    "Otorrinolaringología": ["Consulta de otorrinolaringología", "Audiología", "Cirugía de oído", "Tratamiento de vértigo", "Rinología"],
    "Medicina interna": ["Consulta de medicina interna", "Control de enfermedades crónicas", "Terapia de dolor", "Tratamiento de infecciones", "Unidad de cuidados paliativos"]
}

def generar_hospital():
    hospital = {
        "_id": str(ObjectId()),
        "nombre_hospital": f"Hospital {fake.city()}",
        "direccion": {
            "calle": fake.street_address(),
            "ciudad": fake.city(),
            "codigo_postal": fake.postcode(),
            "pais": "España"
        },
        "departamentos": [generar_departamento(nombre) for nombre in departamentos_servicios],
        "contacto_emergencia": {
            "telefono": fake.phone_number(),
            "email": fake.email()
        }
    }
    return hospital

def generar_departamento(nombre):
    departamento = {
        "departamento_id": str(ObjectId()),
        "nombre": nombre,
        "extension": str(random.randint(1000, 9999)),
        "servicios": random.sample(departamentos_servicios[nombre], random.randint(2, 5)),
        "medicos": [generar_medico(nombre) for _ in range(random.randint(1, 3))]
    }
    return departamento

def generar_medico(especialidad):
    nombre = fake.name()
    medico = {
        "medico_id": str(ObjectId()),
        "nombre": nombre,
        "especialidad": especialidad,
        "años_experiencia": random.randint(5, 25),
        "horario": generar_horario()
    }
    return medico

def generar_horario():
    dias_laborales = random.sample(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sabado","Domingo"], random.randint(2, 5))
    horas = f"{random.randint(8, 10)}:00 - {random.randint(14, 18)}:00"
    horario = {
        "dias_laborales": dias_laborales,
        "horas": horas
    }
    return horario

# Generación de varios hospitales
hospitales = [generar_hospital() for _ in range(50)]

# Guardar en archivo JSON
with open("../../data/hospitales.json", "w", encoding="utf-8") as file:
    json.dump(hospitales, file, ensure_ascii=False, indent=4)

print("Hospitales generados y guardados en 'hospitales.json'")
