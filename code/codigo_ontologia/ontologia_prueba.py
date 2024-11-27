import json
from rdflib import Graph, Literal, Namespace, URIRef, RDF
#from rdflib import Graph, Literal, Namespace
#from rdflib.namespace import RDF

def rellenar_ontologia(ontologia_vacia, json_file, salida_ontologia, limite_pacientes=None):
    """
    Rellena una ontología RDF vacía con datos de un archivo JSON.
    :param ontologia_vacia: Ruta del archivo RDF/Turtle con la ontología vacía.
    :param json_file: Ruta del archivo JSON con datos.
    :param salida_ontologia: Ruta del archivo RDF/Turtle de salida con la ontología enriquecida.
    :param limite_pacientes: Número máximo de pacientes a procesar (opcional).
    """
    # Crear el grafo y cargar la ontología vacía
    g = Graph()
    g.parse(ontologia_vacia, format="turtle")

    # Definir namespaces
    EX = Namespace("http://example.org/paciente#")
    SCHEMA = Namespace("http://schema.org/")
    FOAF = Namespace("http://xmlns.com/foaf/0.1/")
    g.bind("ex", EX)
    g.bind("schema", SCHEMA)
    g.bind("foaf", FOAF)

    # Leer el archivo JSON
    with open(json_file, "r", encoding="utf-8") as f:
        pacientes = json.load(f)

    # Inicializar contador de pacientes procesados
    contador = 0

    # Rellenar la ontología con los datos de los pacientes
    for paciente in pacientes:
        if limite_pacientes is not None and contador >= limite_pacientes:
            break

        paciente_uri = EX[str(paciente["_id"])]  # Crear un URI para el paciente

        # Añadir instancias y propiedades del paciente
        g.add((paciente_uri, RDF.type, EX.Paciente))
        g.add((paciente_uri, FOAF.givenName, Literal(paciente["nombre"])))
        g.add((paciente_uri, FOAF.familyName, Literal(paciente["apellido"])))
        g.add((paciente_uri, SCHEMA.birthDate, Literal(paciente["fecha_nacimiento"])))
        g.add((paciente_uri, SCHEMA.gender, Literal(paciente["sexo"])))

        # Dirección
        direccion = paciente.get("informacion_contacto", {}).get("direccion", {})
        if direccion:
            direccion_uri = EX[f"Direccion_{paciente['_id']}"]
            g.add((direccion_uri, RDF.type, SCHEMA.PostalAddress))
            g.add((direccion_uri, SCHEMA.streetAddress, Literal(direccion.get("calle", ""))))
            g.add((direccion_uri, SCHEMA.addressLocality, Literal(direccion.get("ciudad", ""))))
            g.add((direccion_uri, SCHEMA.addressCountry, Literal(direccion.get("pais", ""))))
            g.add((paciente_uri, SCHEMA.address, direccion_uri))

        # Historial médico
        for i, entrada in enumerate(paciente.get("historial", [])):
            historial_uri = EX[f"Historial_{paciente['_id']}_{i}"]
            g.add((historial_uri, RDF.type, EX.HistorialMedico))
            g.add((historial_uri, EX.tratamientos, URIRef(f"http://example.org/tratamiento#{entrada['tratamientos']}")))
            g.add((historial_uri, EX.hospital, URIRef(f"http://example.org/hospital#{entrada['hospital']}")))
            g.add((paciente_uri, EX.tieneHistorial, historial_uri))

        # Incrementar el contador
        contador += 1

    # Guardar la ontología enriquecida
    g.serialize(destination=salida_ontologia, format="turtle")
    print(f"Ontología enriquecida guardada en {salida_ontologia}")

# Ejemplo de uso
rellenar_ontologia("../../data/esquemas_ontologia_vacios/prueba.ttl", "../../data/pacientes.json", "../../data/ontologia_completa/pacientes_completos.ttl", 5)
