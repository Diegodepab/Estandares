from rdflib import Graph

#################################_Crear Ontologia_##########################################
# Cargar la ontología en formato Turtle (generada por el script ontologia_completa.py)
g = Graph()
g.parse("ontologia_completa.ttl", format="ttl")  # Ontologia completa

#################################_Cargar Consultas_##########################################

# 1) Lista de tratamientos por hospital separados por una ', '.


# Consulta 1: Lista de tratamientos por hospital
def ejecutar_consulta_1(guardar_en_archivo=False):
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
    # Ejecutar la consulta
    result = g.query(consulta1)

    # Formatear los resultados
    resultado_formateado = "\n".join([f"Hospital: {row.hospital_nombre}\nTratamientos: {row.tratamientos}" for row in result])
    # Guardar en archivo si se especifica
    if guardar_en_archivo:
        with open("resultado_consulta_1.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"\nResultado de la consulta 1 guardado en resultado_consulta_1.txt")
    else:
        # Imprimir encabezado
        print("##################################################################")
        print("Consulta 1: Lista de tratamientos por hospital separados por una ,")
        print("##################################################################")
        # Imprimir los resultados
        print(resultado_formateado)



# 2) Resultados de Tratamiento de Diabetes Tipo 2 en mayores de 50 (DNI Fecha de Nacimiento Sexo Etnia Teléfono Correo Dirección).
def ejecutar_consulta_2(guardar_en_archivo=False):
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
    # Ejecutar la consulta
    result = g.query(consulta2)

    # Formatear los resultados
    resultado_formateado = "\n".join([f"""
    DNI: {row.paciente_dni}
    Fecha de Nacimiento: {row.paciente_fecha_nacimiento}
    Etnia: {row.paciente_etnia}
    Sexo: {row.paciente_sexo}
    Teléfono: {row.paciente_telefono}
    Correo: {row.paciente_correo}
    Enfermedad: {row.enfermedad_nombre}
    Dirección: {row.direccion}
    """ for row in result])

    # Imprimir encabezado
    if not guardar_en_archivo:
        print("\n##################################################")
        print("Consulta 2: Lista de pacientes con 'Diabetes Tipo 2'")
        print("####################################################")

        # Imprimir los resultados
        print(resultado_formateado)

    # Guardar en archivo si se especifica
    if guardar_en_archivo:
        with open("resultado_consulta_2.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"\nResultado de la consulta 2 guardado en resultado_consulta_2.txt")

# 3) Información general de los tratamientos (nombre, duración, frecuencia de dosis y vía de administración
def ejecutar_consulta_3(guardar_en_archivo=False):
    query3 = """
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
    # Ejecutar la consulta
    result = g.query(query3)

    # Formatear los resultados
    resultado_formateado = "\n".join([f"""
    Tratamiento: {row.tratamiento_nombre}
    Días de Duración: {row.tratamiento_dias_duracion}
    Frecuencia de Dosis: {row.tratamiento_frecuencia_dosis}
    Vía de Administración: {row.tratamiento_via_administracion}
    """ for row in result])

    # Imprimir encabezado
    if not guardar_en_archivo:
        print("\n#################################################")
        print("Consulta 3: Información general de los tratamientos")
        print("#################################################")

        # Imprimir los resultados
        print(resultado_formateado)

    # Guardar en archivo si se especifica
    if guardar_en_archivo:
        with open("resultado_consulta_3.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"\nResultado de la consulta 3 guardado en resultado_consulta_3.txt")


# 4) Número de tratamientos realizados a cada paciente
def ejecutar_consulta_4(guardar_en_archivo=False):
    query4 = """
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

    # Ejecutar la consulta
    result = g.query(query4)

    # Formatear los resultados
    resultado_formateado = "\n".join([f"""
    Paciente: {row.nombre_completo}
    Número de Tratamientos: {row.numero_de_tratamientos}
    """ for row in result])

    # Imprimir encabezado
    if not guardar_en_archivo:
        print("\n#################################################")
        print("Consulta 4: Número de tratamientos realizados a cada paciente")
        print("#################################################")

        # Imprimir los resultados
        print(resultado_formateado)

    # Guardar en archivo si se especifica
    if guardar_en_archivo:
        with open("resultado_consulta_4.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"\nResultado de la consulta 4 guardado en resultado_consulta_4.txt")


# 5) Veces que se ha aplicado un tratamiento con duración superior a un mes (30 días) (ordenado por duración)
consulta5 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX o: <http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#>

SELECT DISTINCT
  STR(?tratamiento_nombre) AS ?tratamiento
  STR(?tratamiento_dias_duracion) AS ?duracion
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

## 6) Información de hospitales que tienen departamento de Oncología

# Función para ejecutar la consulta y guardar/mostrar resultados
def ejecutar_consulta(consulta, numero_consulta, guardar_en_archivo=False):
    result = g.query(consulta)
    resultado_formateado = "\n".join([", ".join([str(valor) for valor in row]) for row in result])
    
    if guardar_en_archivo:
        with open(f"resultado{numero_consulta}.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"Resultado de la consulta {numero_consulta} guardado en resultado{numero_consulta}.txt")
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
        5: "Veces que se ha aplicado un tratamiento con duración superior a un mes (30 días) (ordenado por duración)."
    }
    
    print("Descripción de las consultas:")
    for consulta_num, descripcion in descripciones.items():
        print(f"Consulta {consulta_num}: {descripcion}")
    print()
    
# Menú interactivo
def menu():
    print()
    print("Seleccione una opción:")
    print("R: Recordar las descripciones de las consultas")
    print("1: Imprimir resultado de la consulta 1")
    print("2: Imprimir resultado de la consulta 2")
    print("3: Imprimir resultado de la consulta 3")
    print("4: Imprimir resultado de la consulta 4")
    print("5: Imprimir resultado de la consulta 5")
    print("6: Guardar resultado de la consulta 1 en un archivo")
    print("7: Guardar resultado de la consulta 2 en un archivo")
    print("8: Guardar resultado de la consulta 3 en un archivo")
    print("9: Guardar resultado de la consulta 4 en un archivo")
    print("10: Guardar resultado de la consulta 5 en un archivo")
    print("0: Salir")

    opcion = input("Ingrese su opción: ")
    print()

    if opcion == "1":
        ejecutar_consulta_1(guardar_en_archivo=False)
    elif opcion == "2":
        ejecutar_consulta_2(guardar_en_archivo=False)
    elif opcion == "3":
        ejecutar_consulta_3(guardar_en_archivo=False)
    elif opcion == "4":
        ejecutar_consulta_4(guardar_en_archivo=False)
    elif opcion == "5":
        ejecutar_consulta(consulta5, 5, guardar_en_archivo=False)
    elif opcion == "6":
        ejecutar_consulta_1(guardar_en_archivo=True)
    elif opcion == "7":
        ejecutar_consulta_2(guardar_en_archivo=True)
    elif opcion == "8":
        ejecutar_consulta_3(guardar_en_archivo=True)
    elif opcion == "9":
        ejecutar_consulta_4(guardar_en_archivo=True)
    elif opcion == "10":
        ejecutar_consulta(consulta5, 5, guardar_en_archivo=True)
    elif opcion.lower() == "r":
        mostrar_descripciones()
    elif opcion == "0":
        print("Saliendo...")
        return
    else:
        print("Opción no válida. Intente de nuevo.")
    
    menu()  # Volver a mostrar el menú

# Ejecutar el menú
menu()
