# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:48:36 2024

@author: DiegoDePablo
"""

from rdflib import Graph
import csv

def ejecutar_consulta(ontology_path, query_path, output_csv_path):
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

# Rutas a los archivos
ontology_file = "ontologia_completa.ttl" 
query_file = "consultas_ontologia/consulta1.txt"
output_csv_file = "resultados.csv" 

# Ejecutar la función
ejecutar_consulta(ontology_file, query_file, output_csv_file)