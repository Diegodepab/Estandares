from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD
import json

def rellenar_ontologia_completa(json_path_pacientes, json_path_hospitales, json_path_tratamientos, salida_path, max_items=-1):
    """
    Rellena una ontología con datos de un JSON de pacientes, hospitales y tratamientos.
    
    :param ontologia_vacia_path: Ruta al archivo Turtle con la ontología vacía.
    :param json_path: Ruta al archivo JSON con los datos.
    :param salida_path: Ruta para guardar la ontología rellenada.
    :param max_items: Número máximo de pacientes a procesar, opcional.
    """

    # Definir el namespace base
    BASE = Namespace("http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#")

    g = Graph()
    g.bind("base", BASE)

    #################################################################
    #    Classes
    #################################################################

    # Definir las clases utilizando el namespace base
    DEPARTAMENTO = BASE.Departamento 
    HISTORIAL = BASE.Historial # Pacientes
    HOSPITAL = BASE.Hospital
    MEDICAMENTO = BASE.Medicamento # Tratamientos
    MEDICO = BASE.Medico
    PACIENTE = BASE.Paciente # Pacientes
    PARAMETRO_MONITORIZACION = BASE.Parametro_Monitorizacion # Tratamientos
    TRATAMIENTO = BASE.Tratamiento # Tratamientos


    # Añadir las clases al grafo
    g.add((DEPARTAMENTO, RDF.type, BASE.Class))
    g.add((HISTORIAL, RDF.type, BASE.Class))
    g.add((HOSPITAL, RDF.type, BASE.Class))
    g.add((MEDICAMENTO, RDF.type, BASE.Class))
    g.add((MEDICO, RDF.type, BASE.Class))
    g.add((PACIENTE, RDF.type, BASE.Class))
    g.add((PARAMETRO_MONITORIZACION, RDF.type, BASE.Class))
    g.add((TRATAMIENTO, RDF.type, BASE.Class))

    #################################################################
    #    Object Properties
    #################################################################

    # Definir propiedades de objeto
    properties = [
        ("departamento_contiene_medicos", BASE.departamento_contiene_medicos, BASE.Departamento, BASE.Medico, BASE.medico_es_contenido_por_departamento), #
        ("departamento_es_contenido_por_hospital", BASE.departamento_es_contenido_por_hospital, BASE.Departamento, BASE.Hospital, BASE.hospital_contiene_departamento), #
        ("historial_hecho_en_hospital", BASE.historial_hecho_en_hospital, BASE.Historial, BASE.Hospital, BASE.hospital_tiene_historial), #
        ("historial_pertenece_a_paciente", BASE.historial_pertenece_a_paciente, BASE.Historial, BASE.Paciente, BASE.paciente_tiene_historial), #
        ("historial_tiene_tratamiento", BASE.historial_tiene_tratamiento, BASE.Historial, BASE.Tratamiento, BASE.tratamiento_pertenece_a_historial), #
        ("hospital_contiene_departamento", BASE.hospital_contiene_departamento, BASE.Hospital, BASE.Departamento, None), #
        ("hospital_tiene_historial", BASE.hospital_tiene_historial, BASE.Hospital, BASE.Historial, None), #
        ("hospital_tiene_tratamiento", BASE.hospital_tiene_tratamiento, BASE.Hospital, BASE.Tratamiento, BASE.tratamiento_hecho_en_hospital), #
        ("medicamento_se_administra_en_tratamiento", BASE.medicamento_se_administra_en_tratamiento, BASE.Medicamento, BASE.Tratamiento, BASE.tratamiento_es_administrado_medicamento), #
        ("medico_es_contenido_por_departamento", BASE.medico_es_contenido_por_departamento, BASE.Medico, BASE.Departamento, None), #
        ("paciente_tiene_historial", BASE.paciente_tiene_historial, BASE.Paciente, BASE.Historial, None), #
        ("parametro_necesita_ser_monitoreado_por_tratamiento", BASE.parametro_necesita_ser_monitoreado_por_tratamiento, BASE.Parametro_Monitorizacion, BASE.Tratamiento, BASE.tratamiento_necesita_monitorear_parametro_de_monitorizacion), #
        ("tratamiento_es_administrado_medicamento", BASE.tratamiento_es_administrado_medicamento, BASE.Tratamiento, BASE.Medicamento, None), #
        ("tratamiento_hecho_en_hospital", BASE.tratamiento_hecho_en_hospital, BASE.Tratamiento, BASE.Hospital, None), #
        ("tratamiento_necesita_monitorear_parametro_de_monitorizacion", BASE.tratamiento_necesita_monitorear_parametro_de_monitorizacion, BASE.Tratamiento, BASE.Parametro_Monitorizacion, None), #
        ("tratamiento_pertenece_a_historial", BASE.tratamiento_pertenece_a_historial, BASE.Tratamiento, BASE.Historial, None), #
    ]

    # Añadir propiedades de objeto al grafo
    for _, prop, domain, range_, inverse in properties:
        g.add((prop, RDF.type, OWL.ObjectProperty))
        g.add((prop, RDFS.domain, domain))
        g.add((prop, RDFS.range, range_))
        if inverse:
            g.add((prop, OWL.inverseOf, inverse))

    #################################################################
    #    Data Properties
    #################################################################

    # Lista de propiedades de datos
    data_properties = [
        ("departamento_extension", BASE.departamento_extension, BASE.Departamento, XSD.string),
        ("departamento_nombre", BASE.departamento_nombre, BASE.Departamento, XSD.string),
        ("departamento_servicio", BASE.departamento_servicio, BASE.Departamento, XSD.string),
        ("enfermedad_categoria", BASE.enfermedad_categoria, BASE.Tratamiento, XSD.string),
        ("enfermedad_nombre", BASE.enfermedad_nombre, BASE.Tratamiento, XSD.string),
        ("enfermedad_severida", BASE.enfermedad_severida, BASE.Tratamiento, XSD.string),
        ("enfermedad_sintoma", BASE.enfermedad_sintoma, BASE.Tratamiento, XSD.string),
        ("historial_fecha", BASE.historial_fecha, BASE.Historial, XSD.date),
        ("hospital_calle", BASE.hospital_calle, BASE.Hospital, XSD.string),
        ("hospital_ciudad", BASE.hospital_ciudad, BASE.Hospital, XSD.string),
        ("hospital_codigo_postal", BASE.hospital_codigo_postal, BASE.Hospital, XSD.string),
        ("hospital_email", BASE.hospital_email, BASE.Hospital, XSD.string),
        ("hospital_nombre", BASE.hospital_nombre, BASE.Hospital, XSD.string),
        ("hospital_pais", BASE.hospital_pais, BASE.Hospital, XSD.string),
        ("hospital_telefono", BASE.hospital_telefono, BASE.Hospital, XSD.string),
        ("medicamento_efecto_secundario", BASE.medicamento_efecto_secundario, BASE.Medicamento, XSD.string),
        ("medicamento_nombre", BASE.medicamento_nombre, BASE.Medicamento, XSD.string),
        ("medicamiento_frecuencia", BASE.medicamiento_frecuencia, BASE.Medicamento, XSD.string),
        ("medico_anos_experiencia", BASE.medico_anos_experiencia, BASE.Medico, XSD.integer),
        ("medico_dia_laboral", BASE.medico_dia_laboral, BASE.Medico, XSD.string),
        ("medico_especialidad", BASE.medico_especialidad, BASE.Medico, XSD.string),
        ("medico_horas", BASE.medico_horas, BASE.Medico, XSD.string),
        ("medico_nombre", BASE.medico_nombre, BASE.Medico, XSD.string),
        ("paciente_apellido", BASE.paciente_apellido, BASE.Paciente, XSD.string),
        ("paciente_calle", BASE.paciente_calle, BASE.Paciente, XSD.string),
        ("paciente_ciudad", BASE.paciente_ciudad, BASE.Paciente, XSD.string),
        ("paciente_codigo_postal", BASE.paciente_codigo_postal, BASE.Paciente, XSD.string),
        ("paciente_correo", BASE.paciente_correo, BASE.Paciente, XSD.string),
        ("paciente_dni", BASE.paciente_dni, BASE.Paciente, XSD.string),
        ("paciente_etnia", BASE.paciente_etnia, BASE.Paciente, XSD.string),
        ("paciente_fecha_nacimiento", BASE.paciente_fecha_nacimiento, BASE.Paciente, XSD.date),
        ("paciente_id", BASE.paciente_id, BASE.Paciente, XSD.string),
        ("paciente_nombre", BASE.paciente_nombre, BASE.Paciente, XSD.string),
        ("paciente_nss", BASE.paciente_nss, BASE.Paciente, XSD.int),
        ("paciente_pais", BASE.paciente_pais, BASE.Paciente, XSD.string),
        ("paciente_sexo", BASE.paciente_sexo, BASE.Paciente, XSD.string),
        ("paciente_telefono", BASE.paciente_telefono, BASE.Paciente, XSD.string),
        ("parametro_nombre", BASE.parametro_nombre, BASE.Parametro_Monitorizacion, XSD.string),
        ("parametro_referencia", BASE.parametro_referencia, BASE.Parametro_Monitorizacion, XSD.string),
        ("parametro_unidad", BASE.parametro_unidad, BASE.Parametro_Monitorizacion, XSD.string),
        ("tratamiento_dias_duracion", BASE.tratamiento_dias_duracion, BASE.Tratamiento, XSD.int),
        ("tratamiento_frecuencia_dosis", BASE.tratamiento_frecuencia_dosis, BASE.Tratamiento, XSD.string),
        ("tratamiento_id", BASE.tratamiento_id, BASE.Tratamiento, XSD.string),
        ("tratamiento_nombre", BASE.tratamiento_nombre, BASE.Tratamiento, XSD.string),
        ("tratamiento_via_administracion", BASE.tratamiento_via_administracion, BASE.Tratamiento, XSD.string),
    ]

    # Añadir propiedades de datos al grafo
    for _, prop, domain, range_ in data_properties:
        g.add((prop, RDF.type, OWL.DatatypeProperty))
        g.add((prop, RDFS.domain, domain))
        g.add((prop, RDFS.range, range_))

    #################################################################
    #    Datatypes
    #################################################################

    # Añadir la definición del tipo de dato xsd:date
    g.add((XSD.date, RDF.type, RDFS.Datatype))

    # Leer los archivos JSON
    with open(json_path_pacientes, "r", encoding="utf-8") as f:
        pacientes = json.load(f)

    with open(json_path_hospitales, "r", encoding="utf-8") as f:
        hospitales = json.load(f)

    with open(json_path_tratamientos, "r", encoding="utf-8") as f:
        tratamientos = json.load(f)


    #################################################################
    #    Primera iteración sobre los JSON
    #################################################################

    # Crear los individuos de todas las clases y object properties posibles
    # Crear individuos de paciente para cada entrada de paciente
    for paciente in pacientes:
        # Crear individuo del paciente
        paciente_uri = URIRef(f"{BASE}{paciente['_id']}")
        g.add((paciente_uri, RDF.type, PACIENTE))

        # Crear individuos de historial para cada entrada de historial
        for historial in paciente.get("historial", []):
            historial_id = f"{paciente['_id']}_historial_{paciente['historial'].index(historial)}"
            historial_uri = URIRef(f"{BASE}{historial_id}")
            g.add((historial_uri, RDF.type, HISTORIAL))
            
            # Relaciones
            g.add((paciente_uri, BASE.paciente_tiene_historial, historial_uri))
            g.add((historial_uri, BASE.historial_pertenece_a_paciente, paciente_uri))
            

    # Crear individuos para los tratamientos y sus parámetros y medicamentos
    for idx1, tratamiento in enumerate(tratamientos):
        # Crear individuo del tratamiento
        tratamiento_uri = URIRef(f"{BASE}{tratamiento['_id']}")
        g.add((tratamiento_uri, RDF.type, TRATAMIENTO))

        # Crear individuos para los medicamentos asociados al tratamiento
        for idx3, _ in enumerate(tratamiento.get("medicamentos", [])):
            medicamento_id = f"{idx1}_{idx3}"
            medicamento_uri = URIRef(f"{BASE}{medicamento_id}")
            g.add((medicamento_uri, RDF.type, MEDICAMENTO))

            # Relaciones
            g.add((tratamiento_uri, BASE.tratamiento_es_administrado_medicamento, medicamento_uri))
            g.add((medicamento_uri, BASE.medicamento_se_administra_en_tratamiento, tratamiento_uri))
            

        # Crear individuos para los parámetros de monitorización asociados al tratamiento
        for idx2, _ in enumerate(tratamiento.get("regimen").get("monitorizacion").get("parametros", [])):
            parametro_id = f"{idx1}_{idx2}"
            parametro_uri = URIRef(f"{BASE}{parametro_id}")
            g.add((parametro_uri, RDF.type, PARAMETRO_MONITORIZACION))

            # Relaciones
            g.add((tratamiento_uri, BASE.tratamiento_necesita_monitorear_parametro_de_monitorizacion, parametro_uri))
            g.add((parametro_uri, BASE.parametro_necesita_ser_monitoreado_por_tratamiento, tratamiento_uri))

    # Crear individuos para los hospitales y sus departamentos y medicos
    for hospital in hospitales:
        # Crear individuo del hospital
        hospital_uri = URIRef(f"{BASE}{hospital['_id']}")
        g.add((hospital_uri, RDF.type, HOSPITAL))

        for tratamiento in hospital.get("tratamientos_posibles", []):
            tratamiento_uri = URIRef(f"{BASE}{tratamiento}")

            # Relaciones
            g.add((tratamiento_uri, BASE.tratamiento_hecho_en_hospital, hospital_uri))
            g.add((hospital_uri, BASE.hospital_tiene_tratamiento, tratamiento_uri))

        for departamento in hospital.get("departamentos", []):
            departamento_uri = URIRef(f"{BASE}{departamento['departamento_id']}")
            g.add((departamento_uri, RDF.type, DEPARTAMENTO))

            # Relaciones
            g.add((departamento_uri, BASE.departamento_es_contenido_por_hospital, hospital_uri))
            g.add((hospital_uri, BASE.hospital_contiene_departamento, departamento_uri))

            for medico in departamento.get("medicos", []):
                medico_uri = URIRef(f"{BASE}{medico['medico_id']}")
                g.add((medico_uri, RDF.type, MEDICO))

                # Relaciones
                g.add((medico_uri, BASE.medico_es_contenido_por_departamento, departamento_uri))
                g.add((departamento_uri, BASE.departamento_contiene_medicos, medico_uri))

    #################################################################
    #    Segunda iteración sobre los JSON
    #################################################################

    for paciente in pacientes:
        for historial in paciente.get("historial", []):
            historial_id = f"{paciente['_id']}_historial_{paciente['historial'].index(historial)}"
            historial_uri = URIRef(f"{BASE}{historial_id}")

            hospital_uri = URIRef(f"{BASE}{historial["hospital"]}")
            tratamiento_uri = URIRef(f"{BASE}{historial["tratamientos"]}")

            # Relaciones
            g.add((historial_uri, BASE.historial_hecho_en_hospital, hospital_uri))
            g.add((hospital_uri, BASE.hospital_tiene_historial, historial_uri))

            g.add((historial_uri, BASE.historial_tiene_tratamiento, tratamiento_uri))
            g.add((tratamiento_uri, BASE.tratamiento_pertenece_a_historial, historial_uri))


            

    # Guardar la ontologia
    g.serialize(salida_path, format="turtle")

    '''
    PROPIEDADES = {
        "id": BASE.paciente_id,
        "nombre": BASE.paciente_nombre,
        "apellido": BASE.paciente_apellido,
        "fecha_nacimiento": BASE.paciente_fecha_nacimiento,
        "sexo": BASE.paciente_sexo,
        "dni": BASE.paciente_dni,
        "nss": BASE.paciente_nss,
        "correo": BASE.paciente_correo,
        "telefono": BASE.paciente_telefono,
        "calle": BASE.paciente_calle,
        "ciudad": BASE.paciente_ciudad,
        "codigo_postal": BASE.paciente_codigo_postal,
        "pais": BASE.paciente_pais,
        "etnia": BASE.paciente_etnia
    }

    for paciente in pacientes:
        paciente_uri = URIRef(f"{BASE}{paciente['id']}")  # Usar id como URI única para cada paciente
    g.add((paciente_uri, RDF.type, PACIENTE))
    
    for key, prop in PROPIEDADES.items():
        if key in paciente and paciente[key]:  # Verificar si el campo existe y no está vacío
            value = paciente[key]
            if key in ["nss"]:  # Tipos de datos específicos
                value_literal = Literal(value, datatype=XSD.int)
            elif key in ["fecha_nacimiento"]:  # Fechas
                value_literal = Literal(value, datatype=XSD.date)
            else:  # Por defecto, strings
                value_literal = Literal(value, datatype=XSD.string)
            
            g.add((paciente_uri, prop, value_literal))

'''


'''
def insertar_pacientes(g, pacientes, BASE):
    """
    Inserta los pacientes en el grafo RDF a partir de los datos JSON.
    
    :param g: Grafo RDF donde se insertarán los datos.
    :param pacientes: Lista de diccionarios con información de los pacientes.
    :param BASE: Namespace base de la ontología.
    """
    PACIENTE = BASE.Paciente
    PROPIEDADES = {
        "_id": BASE.paciente_id,
        "nombre": BASE.paciente_nombre,
        "apellido": BASE.paciente_apellido,
        "fecha_nacimiento": BASE.paciente_fecha_nacimiento,
        "dni": BASE.paciente_dni,
        "nss": BASE.paciente_nss,
        "sexo": BASE.paciente_sexo,
        "etnia": BASE.paciente_etnia,
    }
    CONTACTO_PROPIEDADES = {
        "telefono": BASE.paciente_telefono,
        "correo": BASE.paciente_correo,
    }
    DIRECCION_PROPIEDADES = {
        "calle": BASE.paciente_calle,
        "ciudad": BASE.paciente_ciudad,
        "codigo_postal": BASE.paciente_codigo_postal,
        "pais": BASE.paciente_pais,
    }

    for paciente in pacientes:
        paciente_uri = URIRef(f"{BASE}{paciente['_id']}")  # Usar _id como URI única
        g.add((paciente_uri, RDF.type, PACIENTE))
        
        # Insertar propiedades de nivel superior
        for key, prop in PROPIEDADES.items():
            if key in paciente and paciente[key]:  # Verificar si el campo existe y no está vacío
                value = paciente[key]
                if key in ["nss"]:  # Tipos de datos específicos
                    value_literal = Literal(value, datatype=XSD.int)
                elif key in ["fecha_nacimiento"]:  # Fechas
                    value_literal = Literal(value, datatype=XSD.date)
                else:  # Por defecto, strings
                    value_literal = Literal(value, datatype=XSD.string)
                
                g.add((paciente_uri, prop, value_literal))
        
        # Insertar información de contacto
        if "informacion_contacto" in paciente and paciente["informacion_contacto"]:
            contacto = paciente["informacion_contacto"]
            for key, prop in CONTACTO_PROPIEDADES.items():
                if key in contacto and contacto[key]:  # Verificar si el campo existe y no está vacío
                    value_literal = Literal(contacto[key], datatype=XSD.string)
                    g.add((paciente_uri, prop, value_literal))
            
            # Insertar dirección
            if "direccion" in contacto and contacto["direccion"]:
                direccion = contacto["direccion"]
                for key, prop in DIRECCION_PROPIEDADES.items():
                    if key in direccion and direccion[key]:  # Verificar si el campo existe y no está vacío
                        value_literal = Literal(direccion[key], datatype=XSD.string)
                        g.add((paciente_uri, prop, value_literal))
                          
    '''
rellenar_ontologia_completa(json_path_pacientes = "../../data/pacientes.json",
                             json_path_hospitales = "../../data/hospitales.json",
                               json_path_tratamientos = "../../data/tratamientos.json",
                                 salida_path  = "../../data/ontologia_completa/ontologia_completa.ttl",
                                   max_items=None)