<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="styles.css" />
      </head>
      <body>
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
          <xsl:for-each select="root/item">
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

