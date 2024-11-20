import json
import xml.etree.ElementTree as ET
from lxml import etree  # Para trabajar con XSLT
import argparse

def leer_credenciales(archivo_credenciales):
    with open(archivo_credenciales, 'r', encoding='utf-8') as f:
        credenciales = json.load(f)
    return credenciales["uri"], credenciales["base_datos"], credenciales["coleccion"]

def cargar_consulta(archivo_consulta):
    """
    Lee una consulta desde un archivo TXT en formato JSON.
    """
    with open(archivo_consulta, 'r', encoding='utf-8') as f:
        return json.load(f)

def ejecutar_consulta(mongo_client, base_datos, coleccion, consulta):
    """
    Ejecuta una consulta en MongoDB (find o aggregate) y devuelve los documentos obtenidos.
    """
    db = mongo_client[base_datos]
    collection = db[coleccion]
    
    if isinstance(consulta, list):  # Si es un pipeline (agregación)
        resultados = collection.aggregate(consulta)
    elif isinstance(consulta, dict):  # Si es una consulta de find
        resultados = collection.find(consulta)
    else:
        raise ValueError("La consulta debe ser una lista (pipeline) o un diccionario (find).")

    return list(resultados)

def transformar_a_xml(documentos, root_name="root", item_name="item"):
    """
    Transforma una lista de documentos JSON a un formato XML,
    respetando estructuras anidadas.
    """
    def agregar_elementos(parent, key, value):
        """
        Agrega elementos al XML respetando tipos de datos complejos.
        """
        if isinstance(value, dict):
            # Crear un subelemento para los diccionarios
            sub_element = ET.SubElement(parent, key)
            for sub_key, sub_value in value.items():
                agregar_elementos(sub_element, sub_key, sub_value)
        elif isinstance(value, list):
            # Crear un subelemento para cada elemento de la lista
            list_parent = ET.SubElement(parent, key)
            for item in value:
                agregar_elementos(list_parent, "item", item)
        else:
            # Agregar texto para valores simples
            ET.SubElement(parent, key).text = str(value)

    root = ET.Element(root_name)
    for doc in documentos:
        item = ET.SubElement(root, item_name)
        for key, value in doc.items():
            agregar_elementos(item, key, value)

    return ET.tostring(root, encoding='utf-8')

def aplicar_xslt(xml_data, xslt_file):
    """
    Aplica una plantilla XSLT a un documento XML y genera un HTML.
    """
    dom = etree.fromstring(xml_data)
    xslt = etree.parse(xslt_file)
    transform = etree.XSLT(xslt)
    new_dom = transform(dom)
    return str(new_dom)

def guardar_salida(html_data, salida_html):
    """
    Guarda el documento HTML generado en un archivo.
    """
    with open(salida_html, 'w', encoding='utf-8') as f:
        f.write(html_data)

def main():
    # Configurar argparse
    parser = argparse.ArgumentParser(description="Transforma consultas de MongoDB a HTML usando XSLT.")
    parser.add_argument("--credenciales", required=True, help="Archivo JSON con credenciales de MongoDB.")
    parser.add_argument("--consulta", required=True, help="Archivo TXT con la consulta en formato JSON.")
    parser.add_argument("--xslt", required=True, help="Archivo XSLT para transformar el resultado a HTML.")
    parser.add_argument("--salida", required=True, help="Archivo HTML de salida.")

    args = parser.parse_args()

    try:
        # Leer credenciales y conectarse a MongoDB
        uri, base_datos, coleccion = leer_credenciales(args.credenciales)
        client = pymongo.MongoClient(uri)
        print("Conexión a MongoDB exitosa.")

        # Leer consulta desde el archivo (puede ser un pipeline o una consulta simple)
        consulta = cargar_consulta(args.consulta)

        print(uri + "\n" + base_datos + "\n" + coleccion)
        # Ejecutar la consulta
        documentos = ejecutar_consulta(client, base_datos, coleccion, consulta)
        if not documentos:
            print("No se encontraron documentos para la consulta proporcionada.")
            return
        print("Consulta realizada con éxito.")

        # Transformar resultados a XML
        xml_data = transformar_a_xml(documentos)

        # Aplicar plantilla XSLT
        html_data = aplicar_xslt(xml_data, args.xslt)

        # Guardar resultado en archivo HTML
        guardar_salida(html_data, args.salida)
        print(f"Documento HTML generado: {args.salida}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    main()
