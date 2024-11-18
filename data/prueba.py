import json


# Repite esto para cualquier otro archivo JSON que estés cargando
# Cargar los datos desde el archivo JSON
with open('pacientes.json', 'r', encoding="utf-8") as f:
    pacientes = json.load(f)

with open('tratamientos.json', 'r', encoding="utf-8") as f:
    tratamientos = json.load(f)

with open('hospitales.json', 'r', encoding="utf-8") as f:
    hospitales = json.load(f)

# Crear un diccionario para almacenar los tratamientos por hospital
hospital_tratamientos = {}

# Paso 1: Recorrer todos los pacientes y sus historiales
for paciente in pacientes:
    for historial in paciente['historial']:
        hospital_id = historial['hospital']
        tratamiento_id = historial['tratamientos']
        
        # Paso 2: Verificar si el hospital ya tiene una lista de tratamientos
        if hospital_id not in hospital_tratamientos:
            hospital_tratamientos[hospital_id] = set()  # Usar un set para evitar duplicados

        # Añadir el tratamiento a la lista del hospital
        hospital_tratamientos[hospital_id].add(tratamiento_id)

# Paso 3: Actualizar los hospitales con la lista de tratamientos
for hospital in hospitales:
    hospital_id = hospital['_id']
    
    # Si el hospital tiene tratamientos, agregarlos al campo 'tratamientos_posibles'
    if hospital_id in hospital_tratamientos:
        # Convertir el set de tratamientos a una lista para almacenarlo en JSON
        tratamientos_ids = list(hospital_tratamientos[hospital_id])
        hospital['tratamientos_posibles'] = tratamientos_ids

# Guardar el JSON actualizado de hospitales
with open('hospitales_actualizado.json', 'w') as f:
    json.dump(hospitales, f, indent=4)

print("El JSON de hospitales ha sido actualizado con los tratamientos posibles.")
