import json
from bson import ObjectId
import random

def devolverlinea(archivo):
    with open(archivo, mode='r', encoding='utf-8') as archivor:
        lineas = archivor.readlines()
    return random.choice(lineas).strip()

def devolverlista(archivo, num):
    lista=[]
    while len(lista)<num:
        l=devolverlinea(archivo)
        if not l in lista:
            lista.append(l)
    return lista

def generar_enfermedad(linea_enfermedad):

    e=linea_enfermedad.split(",")

    enfermedad={
            "nombre": e[0],
            "categoria": e[1],
            "sintomas":devolverlista("tratamiento\sintomas.txt", random.randint(1,5)),
            "estado_severidad":e[2]
        }

    return enfermedad

def generar_parametros(num):
    parametros_vitales = {"Frecuencia cardíaca":
                            {
                                "unidad":"bmp",
                                "valor_referencia":"60-100"
                            }, 
                        "Presión arterial":{
                                "unidad":"mmhg",
                                "valor_referencia": "120/180"
                        }, 
                        "Temperatura corporal":{
                            "unidad":"ºC",
                            "valor_referencia": "36.5-37.5"
                        }, 
                        "Saturación de oxígeno":{
                            "unidad":"%",
                            "valor_referencia": "95-100"
                        }}
    
    parametros=[]
    incluidos=[]
    for _ in range(num):

        p=random.choice(list(parametros_vitales.keys()))
        while p in incluidos:
            p=random.choice(list(parametros_vitales.keys()))
        incluidos.append(p)
        parametro={
            "nombre_parametro":p,
            "unidad": parametros_vitales[p]["unidad"],
            "valor_referencia": parametros_vitales[p]["valor_referencia"]
          }
        parametros.append(parametro)
    return parametros

def generar_regimen():
    frecuencias = [
    "Cada 24 horas",
    "Cada 12 horas",
    "Cada 8 horas",
    "Cada 6 horas",
    "Cada 4 horas",
    "Cada 3 horas",
    "Cada 2 horas",
    "Dos veces al día",
    "Tres veces al día",
    "Cuatro veces al día",
    "Una vez al día",
    "Cada mañana",
    "Cada noche",
    "Antes de dormir",
    "Antes de las comidas",
    "Después de las comidas",
    "Cada fin de semana",
    "Cada lunes, miércoles y viernes",
    "Cada martes y jueves",
    "Cada mes",
    "Según sea necesario",
    "Cada semana",
    "En días alternos",
    "Cada 48 horas"
]

    regimen= {
      "duracion_dias": random.randint(1, 100) ,
      "frecuencia_dosis": random.choice(frecuencias),
      "via_administracion": random.choice(["IV (intravenosa)","IM (intramuscular)","SC (subcutánea)","Oral","Sublingual","Tópica","Inhalatoria","Rectal","Intranasal","Oftálmica","Intraocular","Intravesical","Transdérmica","Intracardiaca", "Intraósea","Peridural","Intratecal","Intracavitaria"]),
      "monitorizacion": {
        "frecuencia_monitorizacion": random.choice(["Cada 12 horas", "Cada 24 horas", "Cada 30 minutos", "1 hora después de tratamiento", "Cada 2 horas", "Cada 6 horas", "Cada 3 días", "Antes de cada dosis", "Después de cada procedimiento", "Al inicio de tratamiento", "Cada vez que se realice un cambio en la dosis", "Cada 48 horas", "Cada semana", "Solo cuando se presenten síntomas", "Cada 15 minutos en casos críticos", "Cada 4 horas", "Diariamente durante la primera semana", "Cada 2 días", "De forma continua durante las primeras 24 horas", "Al finalizar el tratamiento"]),
        "parametros": generar_parametros(random.randint(1,4))
      }
    }

    return regimen


def generar_medicamentos():

    m= devolverlinea("tratamiento/nombre_medicamento.txt")
    mi= devolverlinea("tratamiento/nombre_medicamento.txt")
    while(mi[0]==m[0]):
        mi= devolverlinea("tratamiento/nombre_medicamento.txt")

    medicamento={
        "nombre": m,
        #"dosis": dosis,
        "frecuencia": random.choice(["Cada 12 horas", "Cada 24 horas", "1 hora después de comer", "Cada 2 horas", "Cada 6 horas", "Cada 3 días", "Después de cada procedimiento", "Cada 48 horas", "Cada semana", "Solo cuando se presenten síntomas", "Diariamente durante la primera semana", "Cada 2 días", "Cada 8 horas", "Cada 4 horas", "Solo en caso de emergencia", "Dos veces al día", "Cada 3 horas", "Cada 72 horas", "Diariamente", "Cada 5 días", "Cada 10 horas", "Cada 1 hora", "Cada 2 semanas", "Una vez al mes", "Solo en la mañana", "Cada 36 horas", "Cada 18 horas", "Cada 7 días", "Antes de dormir", "Después de cada comida", "Cada 14 días", "Cada 15 días", "Cada 30 días", "Cada 48 horas según necesidad", "Cada 4 días", "Cada 1.5 horas", "En la mañana y en la noche", "Una vez cada 2 semanas", "En días alternos", "Cada 2 horas durante 3 días", "Cada 10 días"]),
        "efectos_secundarios": devolverlista("tratamiento/efectos_secundarios.txt", random.randint(1,6)) ,
        "interacciones": [
          {
            "medicamento_interaccion": mi,
            "efecto_interaccion": random.choice(["Inhibe", "Potencia", "Bloquea", "Reduce", "Aumenta", "Desinhibe", "Interfiere", "Modifica", "Estabiliza", "Mejora"])
          }
        ]
      }
    return medicamento

def generar_tratamiento(nombre, descripcion, enfermedad):
    tratamiento={
        "_id": str(ObjectId()),
        "nombre_tratamiento": nombre,
        "descripcion": descripcion,
        "enfermedad": generar_enfermedad(enfermedad),
        "regimen": generar_regimen(),
    }


    medicamentos=[]
    nombre_incluidos=[]
    for _ in range(random.randint(1,6)):
        m=generar_medicamentos()
        while m["nombre"] in nombre_incluidos:
            m=generar_medicamentos()
            nombre_incluidos.append(m["nombre"])
        medicamentos.append(m)

    tratamiento["medicamentos"]=medicamentos
    return tratamiento


def main():
    tratamientos=[]
    with open("tratamiento/nombre_tratamiento.txt", mode='r', encoding='utf-8') as archivo1, open("tratamiento/descripcion.txt", mode='r', encoding='utf-8') as archivo2, open("tratamiento/enfermedades.txt", mode='r', encoding='utf-8') as archivo3:
         archivo1.seek(0)
         archivo2.seek(0)
         archivo3.seek(0)
         for nombre, descripcion, enfermedad in zip(archivo1, archivo2, archivo3):

            tratamientos.append(generar_tratamiento(nombre.strip(), descripcion.strip(), enfermedad.strip()))

    with open("data/tratamientos.json", "w", encoding="utf-8") as file:
        json.dump(tratamientos, file, ensure_ascii=False, indent=4)
    

main()


# a partir del 86 las descripciones creo q no son correctas




