<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Tratamientos Médicos</title>
        <link rel="stylesheet" type="text/css" href="styles.css"/>
      </head>
      <body>
        <h1>Lista de Tratamientos </h1>
        <table border="1">
          <tr>
            <th>Nombre del Tratamiento</th>
            <th>Descripción</th>
            <th>Enfermedad</th>
            <th>Síntomas</th>
            <th>Edad Media</th>
          </tr>
          <!-- Recorremos cada tratamiento -->
          <xsl:for-each select="tratamientos/tratamiento">
            <tr>
              <td><xsl:value-of select="tratamiento"/></td>
              <td><xsl:value-of select="descripcion"/></td>
              <td><xsl:value-of select="enfermedad/nombre"/></td>
              <td>
                <ul>
                  <xsl:for-each select="enfermedad/sintomas/item">
                    <li><xsl:value-of select="."/></li>
                  </xsl:for-each>
                </ul>
              </td>
              <td><xsl:value-of select="edad_media"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
