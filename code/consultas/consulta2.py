import os
from pymongo import MongoClient
import xml.etree.ElementTree as ET
from lxml import etree
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()
def connect_to_mongo(uri):
    """Conecta a MongoDB usando el URI proporcionado."""
    client = MongoClient(uri)
    return client

def query_mongo_consulta2(client):
    """Ejecuta la consulta2 en MongoDB."""
    db = client["Proyecto"]  # Cambia esto por el nombre de tu base de datos
    collection = db["Paciente"]  # Cambia esto por el nombre de tu colección

    pipeline = [
        {
            "$lookup": {
                "from": "Tratamiento",
                "localField": "historial.tratamientos",
                "foreignField": "_id",
                "as": "tratamiento"
            }
        },
        {
            "$match": {
                "tratamiento.nombre_tratamiento": "Tratamiento de Diabetes Tipo 2",
                "$expr": {
                    "$lte": [
                        {"$dateFromString": {"dateString": "$fecha_nacimiento", "format": "%Y-%m-%d"}},
                        {"$dateFromString": {"dateString": "1974-11-19", "format": "%Y-%m-%d"}}
                    ]
                }
            }
        },
        {
            "$project": {
                "dni": 1,
                "fecha_nacimiento": 1,
                "sexo": 1,
                "etnia": 1,
                "informacion_contacto": 1
            }
        }
    ]

    return list(collection.aggregate(pipeline))

def convert_to_xml_consulta2(data):
    """Convierte los resultados de consulta2 en MongoDB a XML."""
    root = ET.Element("Resultados")

    for entry in data:
        persona = ET.SubElement(root, "Persona")
        ET.SubElement(persona, "_id").text = str(entry.get("_id", ""))
        ET.SubElement(persona, "dni").text = entry.get("dni", "")
        ET.SubElement(persona, "fecha_nacimiento").text = entry.get("fecha_nacimiento", "")
        ET.SubElement(persona, "sexo").text = entry.get("sexo", "")
        ET.SubElement(persona, "etnia").text = entry.get("etnia", "")

        contacto = entry.get("informacion_contacto", {})
        info_contacto = ET.SubElement(persona, "informacion_contacto")
        ET.SubElement(info_contacto, "telefono").text = contacto.get("telefono", "")
        ET.SubElement(info_contacto, "correo").text = contacto.get("correo", "")

        direccion = contacto.get("direccion", {})
        dir_element = ET.SubElement(info_contacto, "direccion")
        ET.SubElement(dir_element, "calle").text = direccion.get("calle", "")
        ET.SubElement(dir_element, "ciudad").text = direccion.get("ciudad", "")
        ET.SubElement(dir_element, "codigo_postal").text = direccion.get("codigo_postal", "")
        ET.SubElement(dir_element, "pais").text = direccion.get("pais", "")

    return ET.ElementTree(root)

def generate_xslt_consulta2(output_path):
    """Genera un archivo XSLT para transformar el XML de consulta2 con un estilo CSS externo."""
    xslt_content = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="styles.css" />
      </head>
      <body>
        <!-- Vinculamos el archivo JS -->
        <script src="script.js"></script>
        <h2>Resultados de Tratamiento de Diabetes Tipo 2 en mayores de 50</h2>
        <table>
          <tr>
           
            <th>DNI</th>
            <th>Fecha de Nacimiento</th>
            <th>Sexo</th>
            <th>Etnia</th>
            <th>Teléfono</th>
            <th>Correo</th>
            <th>Dirección</th>
          </tr>
          <xsl:for-each select="Resultados/Persona">
            <tr>
              <td><xsl:value-of select="dni"/></td>
              <td><xsl:value-of select="fecha_nacimiento"/></td>
              <td><xsl:value-of select="sexo"/></td>
              <td><xsl:value-of select="etnia"/></td>
              <td><xsl:value-of select="informacion_contacto/telefono"/></td>
              <td><xsl:value-of select="informacion_contacto/correo"/></td>
              <td>
                <xsl:value-of select="informacion_contacto/direccion/calle"/>,
                <xsl:value-of select="informacion_contacto/direccion/ciudad"/>,
                <xsl:value-of select="informacion_contacto/direccion/codigo_postal"/>,
                <xsl:value-of select="informacion_contacto/direccion/pais"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>

"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xslt_content)

def apply_xslt_to_xml_consulta(xml_path, xslt_path, output_html_path):
    """Aplica el archivo XSLT a XML de consulta2 y genera un archivo HTML."""

    # Parsear los archivos XML y XSLT
    xml_tree = etree.parse(xml_path)
    xslt_tree = etree.parse(xslt_path)

    # Crear un objeto XSLT
    transform = etree.XSLT(xslt_tree)

    # Aplicar la transformación
    html_tree = transform(xml_tree)

    # Guardar el resultado como un archivo HTML
    with open(output_html_path, "wb") as f:
        f.write(etree.tostring(html_tree, pretty_print=True, method="html"))

    print(f"Transformación completada. El archivo HTML se guardó en {output_html_path}")

if __name__ == "__main__":
    # URI del entorno (asegúrate de configurarlo)
    MONGO_URI = os.getenv("MONGO_URI")
    # Conectar a MongoDB
    client = connect_to_mongo(MONGO_URI)

    # Realizar consulta
    results = query_mongo_consulta2(client)

    # Convertir resultados a XML
    xml_tree = convert_to_xml_consulta2(results)
    xml_tree.write("output_consulta2.xml", encoding="utf-8", xml_declaration=True)

    # Generar archivo XSLT
    generate_xslt_consulta2("output_consulta2.xslt")
    apply_xslt_to_xml_consulta("output_consulta2.xml", "output_consulta2.xslt", "output_consulta2.html")
    print("Proceso completado: 'output_consulta2.xml' y 'output_consulta2.xslt' generados.")
