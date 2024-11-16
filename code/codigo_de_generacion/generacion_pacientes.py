import random
import json
from datetime import datetime, timedelta
from bson.objectid import ObjectId  # Usamos esta librería para generar ObjectId


def seleccionar_linea_aleatoria(archivo):
    """
    Abre un archivo de texto y devuelve una línea seleccionada aleatoriamente.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        lineas = [linea.strip() for linea in lineas if linea.strip()]
        return random.choice(lineas) if lineas else None
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def seleccionar_id_aleatorio(json_file):
    """
    Abre un archivo JSON y selecciona un _id aleatorio.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        ids = [item["_id"] for item in datos if "_id" in item]
        return random.choice(ids) if ids else None
    except FileNotFoundError:
        print(f"Error: El archivo '{json_file}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def generar_fecha_aleatoria(inicio, fin):
    """
    Genera una fecha aleatoria entre dos fechas.
    """
    rango_dias = (fin - inicio).days
    fecha_aleatoria = inicio + timedelta(days=random.randint(0, rango_dias))
    return fecha_aleatoria.strftime('%Y-%m-%d')


def generar_historial(n, hospitales_file, tratamientos_file, fecha_nacimiento):
    """
    Genera un historial médico aleatorio para un paciente.

    :param n: Número de entradas en el historial.
    :param hospitales_file: Archivo JSON con hospitales.
    :param tratamientos_file: Archivo JSON con tratamientos.
    :param fecha_nacimiento: Fecha mínima (en formato YYYY-MM-DD).
    :return: Lista con entradas del historial médico.
    """
    fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    fecha_inicio = fecha_nacimiento_dt + timedelta(days=365 * 18)  # Desde los 18 años
    fecha_fin = datetime.now()

    # Si la fecha_inicio supera a la fecha actual, ajustarla
    if fecha_inicio > fecha_fin:
        fecha_inicio = fecha_fin - timedelta(days=1)  # Aseguramos un rango válido

    historial = []
    for _ in range(n):
        historial.append({
            "tratamientos": seleccionar_id_aleatorio(tratamientos_file),
            "hospital": seleccionar_id_aleatorio(hospitales_file),
            "fecha": generar_fecha_aleatoria(fecha_inicio, fecha_fin)
        })
    return historial

def generar_paciente(nombres_m_file, nombres_f_file, apellidos_file, etnias_file, hospitales_file, tratamientos_file):
    """
    Genera un diccionario con la información de un paciente.
    """
    _id = str(ObjectId())
    sexo = random.choice(["masculino", "femenino"])
    nombre_file = nombres_m_file if sexo == "masculino" else nombres_f_file
    nombre = seleccionar_linea_aleatoria(nombre_file)
    apellido = seleccionar_linea_aleatoria(apellidos_file)
    etnia = seleccionar_linea_aleatoria(etnias_file)
    fecha_nacimiento = generar_fecha_aleatoria(
        datetime(1920, 1, 1), datetime(2023, 1, 1)
    )
    dni = f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    nss = random.randint(100000000000, 999999999999)
    
    paciente = {
        "_id": _id,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "dni": dni,
        "nss": nss,
        "sexo": sexo,
        "etnia": etnia,
        "informacion_contacto": {
            "telefono": f"+34 {random.randint(600, 699)} {random.randint(100, 999)} {random.randint(100, 999)}",
            "correo": f"{nombre.lower().replace(' ', '_')}.{apellido.lower().replace(' ', '_')}@gmail.com",
            "direccion": {
                "calle": f"Calle {random.choice(['Mayor', 'Menor', 'Central', 'Nueva'])} {random.randint(1, 100)}",
                "ciudad": random.choice(["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]),
                "codigo_postal": f"{random.randint(10000, 99999)}",
                "pais": "España"
            }
        },
        "historial": generar_historial(
            random.randint(1, 5), hospitales_file, tratamientos_file, fecha_nacimiento
        )  # Genera entre 1 y 5 entradas en el historial
    }
    
    return paciente


def main():
    """
    Función principal para generar la información de pacientes.
    """
    # Archivos de datos
    ruta_base = "./../../rellenoPacientes/"
    apellidos_file = ruta_base + "apellido_paciente.txt"
    etnias_file = ruta_base + "etnia_paciente.txt"
    nombres_m_file = ruta_base + "nombre_masculino_paciente.txt"
    nombres_f_file = ruta_base + "nombre_femenino_paciente.txt"
    hospitales_file = "../../data/hospitales.json"
    tratamientos_file = "../../data/tratamientos.json"
    
    # Lista para almacenar pacientes
    pacientes = []
    
    # Número de pacientes a generar
    num_pacientes = 1000
    
    for _ in range(num_pacientes):
        paciente = generar_paciente(nombres_m_file, nombres_f_file, apellidos_file, etnias_file, hospitales_file, tratamientos_file)
        pacientes.append(paciente)
    
    # Comprobar unicidad de los _id
    ids = [paciente["_id"] for paciente in pacientes]
    ids_unicos = set(ids)
    
    if len(ids) != len(ids_unicos):
        print(f"Advertencia: Se encontraron IDs duplicados. Generados: {len(ids)}, Únicos: {len(ids_unicos)}")
        # Opcional: Lanzar una excepción si es crítico
        raise ValueError("Se encontraron IDs duplicados en los pacientes generados.")
    
    # Guardar pacientes en un archivo JSON
    with open("../../data/pacientes.json", "w", encoding="utf-8") as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=4)
    
    print(f"Se generaron {num_pacientes} pacientes y se guardaron en 'pacientes.json'.")

'''
# Ejemplo de uso
ruta_base = "./../../rellenoPacientes/"
ruta_etnias = ruta_base + "etnia_paciente.txt"
etnia_aleatoria = seleccionar_linea_aleatoria(ruta_etnias)
print(f"Etnia seleccionada: {etnia_aleatoria}")
'''

main()