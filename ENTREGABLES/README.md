Explicación de los archivos entregados:
1. Ontologia_rellena.rdf: corresponde a la ontología añadida a mano.
2. Ontologia_razonada.rdf: corresponde a la ontología anterior razonada.
3. Ontologia_completa.py: es un script  en python que usando RDFlib genera un grafo de tripletas RDF con los individuos desde la base de datos de mongo, creando la ontología con todos los datos de las practicas anteriores
4. Ontologia_completa.ttl: Archivo generado del script anterior, es la ontologia con todos los datos usados en MongoDB
5. Carpeta Consultas_Ontologias: archivos .txt que contienen las 6 consultas
6. Consultas_RDF.py: Es un script de python capaz de realizar las consultas propuestas. Dicho script tiene una función genérica capaz de compilar todas las consultas separando por ', ' los resultados, dicho script tiene cargado automaticamente la ontolgia y las consultas para que la evaluación sea más fácil, en caso de querer comprobar la función genérica capaz de trabajar con cualquier ontología, cualquier consulta al ejecutar tendra la opción de ejecutar P en el menu de la consola para personalizar los parámetros
   