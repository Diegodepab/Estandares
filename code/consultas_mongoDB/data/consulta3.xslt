<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="styles.css" />
      </head>
      <body>
        <script src="script.js"></script>
        <h2>Información general de los tratamientos</h2>
        <table>
          <tr>
            <th>Tratamiento</th>
            <th>Descripción</th>
            <th>Enfermedad</th>
            <th>Síntomas</th>
            <th>Edad media</th>
          </tr>
          <xsl:for-each select="root/item">
            <tr>
              <td><xsl:value-of select="tratamiento"/></td>
              <td><xsl:value-of select="descripcion"/></td>
              <td><xsl:value-of select="enfermedad/nombre"/></td>
              <td>
                <xsl:for-each select="enfermedad/sintomas/item">
                    <xsl:value-of select="."/>
                    <xsl:if test="position() != last()">, </xsl:if>
                </xsl:for-each>
              </td>
              <td><xsl:value-of select="edad_media"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
