from rdflib import Graph
import csv

#################################_Crear Ontologia_##########################################
# Cargar la ontología en formato Turtle (generada por el script ontologia_completa.py)
g = Graph()
g.parse("ontologia_completa.ttl", format="ttl")  # Ontologia completa

#################################_Cargar Consultas_##########################################

# 1) Lista de tratamientos por hospital separados por una ', '.
consulta1 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

SELECT
  ?hospital_nombre
  (GROUP_CONCAT(?tratamiento_nombre; separator=", ") AS ?tratamientos)
WHERE {
  ?hospital rdf:type o:Hospital .
  ?hospital o:hospital_nombre ?hospital_nombre .
  ?hospital o:hospital_tiene_tratamiento ?tratamiento .
  ?tratamiento o:tratamiento_nombre ?tratamiento_nombre .
}
GROUP BY ?hospital_nombre
"""




#Consulta 2 Resultados de Tratamiento de Diabetes Tipo 2 en mayores de 50 (DNI Fecha de Nacimiento Sexo Etnia Teléfono Correo Dirección).
consulta2 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

SELECT
  ?paciente_dni
  ?paciente_fecha_nacimiento
  ?paciente_etnia
  ?paciente_sexo
  ?paciente_telefono
  ?paciente_correo
  ?enfermedad_nombre
  (CONCAT(?paciente_ciudad, ", ", ?paciente_codigo_postal) AS ?direccion)
WHERE {
  ?paciente rdf:type o:Paciente .
  ?paciente o:paciente_dni ?paciente_dni .
  ?paciente o:paciente_fecha_nacimiento ?paciente_fecha_nacimiento .
  ?paciente o:paciente_sexo ?paciente_sexo .
  ?paciente o:paciente_etnia ?paciente_etnia .
  ?paciente o:paciente_telefono ?paciente_telefono .
  ?paciente o:paciente_correo ?paciente_correo .
  ?paciente o:paciente_ciudad ?paciente_ciudad .
  ?paciente o:paciente_codigo_postal ?paciente_codigo_postal .
  ?paciente o:paciente_tiene_historial ?historial .
  ?historial o:historial_tiene_tratamiento ?tratamiento .
  ?tratamiento o:enfermedad_nombre ?enfermedad_nombre .
  FILTER(?enfermedad_nombre = "Diabetes Tipo 2"^^<http://www.w3.org/2001/XMLSchema#string>)
}
"""



# 3) Información general de los tratamientos (nombre, duración, frecuencia de dosis y vía de administración
consulta3 = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

    SELECT  
      ?tratamiento
      ?tratamiento_nombre
      ?tratamiento_dias_duracion
      ?tratamiento_frecuencia_dosis
      ?tratamiento_via_administracion
    WHERE {
      ?tratamiento rdf:type o:Tratamiento .
      ?tratamiento o:tratamiento_nombre ?tratamiento_nombre .
      ?tratamiento o:tratamiento_dias_duracion ?tratamiento_dias_duracion .
      ?tratamiento o:tratamiento_frecuencia_dosis ?tratamiento_frecuencia_dosis .
      ?tratamiento o:tratamiento_via_administracion ?tratamiento_via_administracion .
    }
    """

# 4) Número de tratamientos realizados a cada paciente
consulta4 = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

    SELECT
      (CONCAT(?paciente_nombre, " ", ?paciente_apellido) AS ?nombre_completo)
      (COUNT(DISTINCT ?tratamiento) as ?numero_de_tratamientos)
    WHERE {
      ?paciente rdf:type o:Paciente.
      ?paciente o:paciente_nombre ?paciente_nombre .
      ?paciente o:paciente_apellido ?paciente_apellido .
      ?paciente o:paciente_tiene_historial ?historial .
      ?historial o:historial_tiene_tratamiento ?tratamiento .
    }
    GROUP BY ?paciente_nombre ?paciente_apellido
    ORDER BY DESC(?numero_de_tratamientos)
    """

# 5) Veces que se ha aplicado un tratamiento con duración superior a un mes (30 días) (ordenado por duración)
consulta5 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

SELECT
  ?tratamiento_nombre
  ?tratamiento_dias_duracion
  (COUNT(?historial) AS ?veces_aplicado)
WHERE {
  ?paciente rdf:type o:Paciente .
  ?paciente o:paciente_nombre ?paciente_nombre .
  ?paciente o:paciente_apellido ?paciente_apellido .
  ?paciente o:paciente_tiene_historial ?historial .
  ?historial o:historial_tiene_tratamiento ?tratamiento .
  ?tratamiento rdf:type o:Tratamiento .
  ?tratamiento o:tratamiento_nombre ?tratamiento_nombre .
  ?tratamiento o:tratamiento_dias_duracion ?tratamiento_dias_duracion .
  
  FILTER (?tratamiento_dias_duracion > 30)
}
GROUP BY ?tratamiento_nombre ?tratamiento_dias_duracion
ORDER BY DESC(?tratamiento_dias_duracion)
"""

# 6) Información de hospitales que tienen departamento de Oncología
consulta6 = """
PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

SELECT 
  ?nombre_hospital
  ?calle
  ?ciudad
  ?codigo_postal
  ?pais
  (GROUP_CONCAT(DISTINCT ?departamento_servicio; separator=", ") AS ?servicios)
WHERE {
  ?hospital rdf:type o:Hospital .
  ?hospital o:hospital_nombre ?nombre_hospital .
  ?hospital o:hospital_calle ?calle .
  ?hospital o:hospital_ciudad ?ciudad .
  ?hospital o:hospital_codigo_postal ?codigo_postal .
  ?hospital o:hospital_pais ?pais .

  ?hospital o:hospital_contiene_departamento ?departamento .
  ?departamento o:departamento_nombre ?departamento_nombre .
  ?departamento o:departamento_servicio ?departamento_servicio .

  FILTER (str(?departamento_nombre) = "Oncología")
}
GROUP BY ?nombre_hospital ?calle ?ciudad ?codigo_postal ?pais ?departamento_nombre
ORDER BY ?nombre_hospital
"""


#################################_Funcion para ejecutar consulta_##########################################

def ejecutar_consulta(consulta, numero_consulta, guardar_en_archivo=False):
    result = g.query(consulta)
    
    # Definir las columnas de acuerdo a las variables de la consulta
    columns = result.vars  # Esto extrae los nombres de las variables 
    
    # Formatear los resultados para mostrar en la consola
    resultado_formateado = "\n".join([", ".join([str(valor) for valor in row]) for row in result])

    if guardar_en_archivo:
        # Guardar los resultados en un archivo CSV
        with open(f"resultado_consulta{numero_consulta}.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Escribir las cabeceras (nombres de las columnas)
            writer.writerow(columns)

            # Escribir los resultados de la consulta en el archivo CSV
            for row in result:
                writer.writerow(row)  # Escribir una fila por cada resultado
        print(f"Resultados guardados como resultado_consulta{numero_consulta}.csv")
    else:
        print(f"Resultado de la consulta {numero_consulta}:")
        print(resultado_formateado)



# Función para mostrar las descripciones de las consultas
def mostrar_descripciones():
    descripciones = {
        1: "Lista de tratamientos por hospital separados por una ', '.",
        2: "Resultados de Tratamiento de Diabetes Tipo 2 en mayores de 50 (DNI, Fecha de Nacimiento, Sexo, Etnia, Teléfono, Correo, Dirección).",
        3: "Información general de los tratamientos (nombre, duración, frecuencia de dosis y vía de administración).",
        4: "Número de tratamientos realizados a cada paciente.",
        5: "Veces que se ha aplicado un tratamiento con duración superior a un mes (30 días) (ordenado por duración).",
        6: "Información de hospitales que tienen departamento de Oncología"
    }
    
    print("Descripción de las consultas:")
    for consulta_num, descripcion in descripciones.items():
        print(f"Consulta {consulta_num}: {descripcion}")
    print()
    
    
def consulta_generica(ontology_path, query_path, output_csv_path):
    """
    Carga una ontología desde un archivo .ttl, ejecuta una consulta SPARQL desde un archivo .txt
    y guarda los resultados en un archivo CSV.

    :param ontology_path: Ruta al archivo de la ontología (.ttl).
    :param query_path: Ruta al archivo con la consulta SPARQL (.txt).
    :param output_csv_path: Ruta al archivo donde se guardarán los resultados en formato CSV.
    """
    # Cargar la ontología
    g = Graph()
    g.parse(ontology_path, format="turtle")
    print(f"Ontología cargada desde: {ontology_path}")

    # Leer la consulta SPARQL desde el archivo
    with open(query_path, "r", encoding="utf-8") as f:
        sparql_query = f.read()

    print(f"Consulta SPARQL leída desde: {query_path}")
    print("Ejecutando consulta...")

    # Ejecutar la consulta
    results = g.query(sparql_query)

    # Extraer nombres de las columnas desde la consulta SPARQL
    columns = results.vars  # Esto obtiene las variables de SELECT como una lista

    # Guardar los resultados en un archivo CSV
    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Escribir las cabeceras (nombres de las columnas)
        writer.writerow(columns)

        # Escribir los resultados
        for result in results:
            writer.writerow(result)

    print(f"Resultados guardados en: {output_csv_path}")


    
# Menú interactivo
def menu():
    print()
    print("Seleccione una opción:")
    print("R: Recordar las descripciones de las consultas")
    print("#Opciones para mostrar por consola")
    print("1: Imprimir resultado de la consulta 1")
    print("2: Imprimir resultado de la consulta 2")
    print("3: Imprimir resultado de la consulta 3")
    print("4: Imprimir resultado de la consulta 4")
    print("5: Imprimir resultado de la consulta 5")
    print("6: Imprimir resultado de la consulta 6")
    print("#Opciones para guardar resultados en un .txt")
    print("7: Guardar resultado de la consulta 1 en un archivo.txt")
    print("8: Guardar resultado de la consulta 2 en un archivo.txt")
    print("9: Guardar resultado de la consulta 3 en un archivo.txt")
    print("10: Guardar resultado de la consulta 4 en un archivo.txt")
    print("11: Guardar resultado de la consulta 5 en un archivo.txt")
    print("12: Guardar resultado de la consulta 6 en un archivo.txt")
    print("P: Ingresar rutas personalizadas para ejecutar la consulta")
    print("0: Salir")

    opcion = input("Ingrese su opción: ")
    print()

    if opcion == "1":
        ejecutar_consulta(consulta1, 1, guardar_en_archivo=False)
    elif opcion == "2":
        ejecutar_consulta(consulta2, 2, guardar_en_archivo=False)
    elif opcion == "3":
        ejecutar_consulta(consulta3, 3, guardar_en_archivo=False)
    elif opcion == "4":
        ejecutar_consulta(consulta4, 4, guardar_en_archivo=False)
    elif opcion == "5":
        ejecutar_consulta(consulta5, 5, guardar_en_archivo=False)
    elif opcion == "6":
        ejecutar_consulta(consulta6, 6, guardar_en_archivo=False)
    elif opcion == "7":
        ejecutar_consulta(consulta1, 1, guardar_en_archivo=True)
    elif opcion == "8":
        ejecutar_consulta(consulta2, 2, guardar_en_archivo=True)
    elif opcion == "9":
        ejecutar_consulta(consulta3, 3, guardar_en_archivo=True)
    elif opcion == "10":
        ejecutar_consulta(consulta4, 4, guardar_en_archivo=True)
    elif opcion == "11":
        ejecutar_consulta(consulta5, 5, guardar_en_archivo=True)
    elif opcion == "12":
        ejecutar_consulta(consulta6, 6, guardar_en_archivo=True)
    elif opcion.lower() == "r":
        mostrar_descripciones()
    elif opcion.lower() == "p":
        # Solicitar rutas personalizadas al usuario
        ontology_file = input("Ingrese la ruta del archivo de la ontología (ej. ontologia_completa.ttl): ")
        query_file = input("Ingrese la ruta del archivo de la consulta SPARQL (ej. consultas_ontologia/consulta1.txt): ")
        output_csv_file = input("Ingrese la ruta para guardar el archivo CSV de resultados (ej. resultados.csv): ")
        
        # Ejecutar la consulta con las rutas personalizadas
        consulta_generica(ontology_file, query_file, output_csv_file)
    elif opcion == "0":
        print("Saliendo...")
        return
    else:
        print("Opción no válida. Intente de nuevo.")
    
    menu()  # Volver a mostrar el menú

# Ejecutar el menú
menu()
