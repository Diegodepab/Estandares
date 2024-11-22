<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="styles.css" />
      </head>
      <body>
        <h2>Lista de Tratamientos por Hospital</h2>
        <table border="1">
          <tr>
            <th>Hospital</th>
            <th>Tratamiento</th>
            <th>Número de Aplicaciones</th>
          </tr>
          <xsl:for-each select="tratamientos/tratamiento">
            <tr>
              <td rowspan="{count(tratamientos/item)}"><xsl:value-of select="hospital"/></td>
              <xsl:for-each select="tratamientos/item">
                <td><xsl:value-of select="tratamiento"/></td>
                <td><xsl:value-of select="num_aplicado"/></td>
              </xsl:for-each>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
