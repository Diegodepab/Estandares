from rdflib import Graph

#################################_Crear Ontologia_##########################################
# Cargar la ontología en formato Turtle (generada por el script ontologia_completa.py)
g = Graph()
g.parse("ontologia_completa.ttl", format="ttl")  # Ontologia completa

#################################_Cargar Consultas_##########################################

# 1) Lista de tratamientos por hospital separados por una ', '.
# Consulta 1: para la función generica
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


#Consulta 2 para función genérica
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
def ejecutar_consulta_5(guardar_en_archivo=False):
    # Definir la quinta consulta SPARQL (Veces que se ha aplicado un tratamiento con duración superior a 30 días)
    query5 = """
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

    print("Ejecutando la consulta SPARQL para obtener tratamientos de más de 30 días... (tardará más que otras consultas por el uso de ORDER by, group by y COUNT")

    # Ejecutar la consulta
    result5 = g.query(query5)

    # Verificar si result5 tiene resultados
    if len(result5) == 0:
        print("No se encontraron tratamientos con duración superior a 30 días.")
        return  # Salir si no hay resultados

    # Formatear los resultados
    resultado_formateado = "\n".join([f"""
    Tratamiento: {row.tratamiento_nombre}
    Duración: {row.tratamiento_dias_duracion} días
    Veces Aplicado: {row.veces_aplicado}
    """ for row in result5])

    # Imprimir encabezado y resultados
    if not guardar_en_archivo:
        print("\n#################################################")
        print("Consulta 5: Veces que se ha aplicado un tratamiento con duración superior a 30 días")
        print("#################################################")
        print(resultado_formateado)
    else:
        # Guardar en archivo si se especifica
        with open("resultado_consulta_5.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"\nResultado de la consulta 5 guardado en resultado_consulta_5.txt")



## 6) Información de hospitales que tienen departamento de Oncología
def ejecutar_consulta_6(guardar_en_archivo=False):
    # Definir la sexta consulta SPARQL (Información de hospitales que tienen departamento de Oncología)
    query6 = """
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

    print("Ejecutando la consulta SPARQL para obtener hospitales con departamento de Oncología...")

    try:
        # Ejecutar la consulta
        result6 = g.query(query6)

        # Verificar si result6 tiene resultados
        if len(result6) == 0:
            print("No se encontraron hospitales con departamento de Oncología.")
            return  # Salir si no hay resultados

        # Formatear los resultados
        resultado_formateado = "\n".join([f"""
        Hospital: {row.nombre_hospital}
        Calle: {row.calle}
        Ciudad: {row.ciudad}
        Código Postal: {row.codigo_postal}
        País: {row.pais}
        Servicios: {row.servicios}
        """ for row in result6])

        # Imprimir encabezado y resultados
        if not guardar_en_archivo:
            print("\n#################################################")
            print("Consulta 6: Información de hospitales con departamento de Oncología")
            print("#################################################")
            print(resultado_formateado)
        else:
            # Guardar en archivo si se especifica
            with open("resultado_consulta_6.txt", "w") as f:
                f.write(resultado_formateado)
            print(f"\nResultado de la consulta 6 guardado en resultado_consulta_6.txt")

    except Exception as e:
        print(f"Ocurrió un error al ejecutar la consulta: {e}")



# Función genérica la consulta y guardar/mostrar resultados
def ejecutar_consulta(consulta, numero_consulta, guardar_en_archivo=False):
    result = g.query(consulta)
    resultado_formateado = "\n".join([", ".join([str(valor) for valor in row]) for row in result])
    
    if guardar_en_archivo:
        with open(f"resultado{numero_consulta}_generico.txt", "w") as f:
            f.write(resultado_formateado)
        print(f"Resultado de la consulta {numero_consulta}_generico guardado en resultado{numero_consulta}.txt")
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
    print("#Opciones para probar la función genérica")
    print("G1: para usar la función genérica en la consulta 1 por pantalla")
    print("G2: para usar la función genérica en la consulta 2 por pantalla")
    print("T1: para usar la función genérica en la consulta 1 por txt")
    print("T2: para usar la función genérica en la consulta 1 por pantalla")
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
        ejecutar_consulta_5(guardar_en_archivo=False)
    elif opcion == "6":
        ejecutar_consulta_6(guardar_en_archivo=False)
    elif opcion == "7":
        ejecutar_consulta_1(guardar_en_archivo=True)
    elif opcion == "8":
        ejecutar_consulta_2(guardar_en_archivo=True)
    elif opcion == "9":
        ejecutar_consulta_3(guardar_en_archivo=True)
    elif opcion == "10":
        ejecutar_consulta_4(guardar_en_archivo=True)
    elif opcion == "11":
        ejecutar_consulta_5(guardar_en_archivo=True)
    elif opcion == "12":
        ejecutar_consulta_6(guardar_en_archivo=True)
    elif opcion == "G1":
        ejecutar_consulta(consulta1,1, guardar_en_archivo=False)
    elif opcion == "G2":
        ejecutar_consulta(consulta2,2, guardar_en_archivo=False)
    elif opcion == "T1":
        ejecutar_consulta(consulta1,1, guardar_en_archivo=True)
    elif opcion == "T2":
        ejecutar_consulta(consulta2,2, guardar_en_archivo=True)
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
