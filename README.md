# Proyecto final: Estándares de Datos Abiertos e Integración de Datos

Este proyecto forma parte de la asignatura de **Estándares de Datos Abiertos e Integración de Datos**. Se centra en el diseño, poblamiento y consultas de una base de datos en MongoDB, además del manejo de dicha base se probara el uso de estándares y la transformación de diversos tipos de bases de datos como puede ser XML u otros formatos. 

## Índice
1. [T1 - Diseño y Poblamiento de la Base de Datos](#diseño-y-poblamiento-de-la-base-de-datos)
2. [T2 - Documentos XML y Vistas HTML mediante XSLT](#documentos-xml-y-vistas-html-mediante-xslt)
3. [T3 - Diseño de ontología en Protege y consultas SPARQL](#Diseño-de-ontología-en-Protege-y-consultas-SPARQL)
5. [Autores](#Autores)

## Diseño y Poblamiento de la Base de Datos

En esta primera fase, se diseña una base de datos en MongoDB, que incluye tres colecciones interconectadas:

- **Hospitales**
- **Pacientes**
- **Tratamientos**

Cada colección está organizada con varios niveles de anidamiento para permitir una estructura rica y compleja, basada en la base de datos real [eICU-CRD](https://eicu-crd.mit.edu), adaptada para proteger el anonimato de los pacientes, además de cumplir las exigencias de complejidad. Los datos han sido generados y procesados para cumplir los requerimientos del proyecto.

### Estructura de las colecciones
<details>
<summary>Haz clic para ver la estructura de las colecciones</summary>

#### Hospitales
- ID
- Nombre del hospital
- Dirección
  - Calle
  - Ciudad
  - Código postal
  - País
- Departamentos
  - ID del departamento
  - Nombre del departamento
  - Extensión
  - Servicios ofrecidos
  - Médicos
    - ID del médico
    - Nombre del médico
    - Especialidad
    - Años de experiencia
    - Horario
      - Días laborales
      - Horas
- Contacto de emergencia
  - Teléfono
  - Email
- Tratamientos posibles
  - ID de tratamiento


#### Paciente
- ID
- Nombre
- Apellido
- Fecha de nacimiento
- DNI
- NSS (Número de Seguridad Social)
- Sexo
- Etnia
- Información de contacto
  - Teléfono
  - Correo electrónico
  - Dirección
    - Calle
    - Ciudad
    - Código postal
    - País
- Historial médico
  - Tratamientos
  - Hospital
  - Fecha


#### Tratamiento
- ID
- Nombre del tratamiento
- Descripción
- Enfermedad
  - Nombre de la enfermedad
  - Categoría
  - Síntomas
  - Estado de severidad
- Régimen
  - Duración en días
  - Frecuencia de dosis
  - Vía de administración
  - Monitorización
    - Frecuencia de monitorización
    - Parámetros de monitorización
      - Nombre del parámetro
      - Unidad
      - Valor de referencia
- Medicamentos
  - Nombre del medicamento
  - Frecuencia de administración
  - Efectos secundarios
  - Interacciones
    - Medicamento de interacción
    - Efecto de la interacción


</details>

Los **archivos JSON** finales están disponibles en la carpeta `data`, mientras que los **scripts de generación** se encuentran en `code/codigo_de_generacion`.

## Documentos XML y Vistas HTML mediante XSLT

En esta segunda parte, se desarrolló un script en Python que ejecuta lo siguiente:

1. **Consultas** a la base de datos MongoDB, basadas en las relaciones establecidas entre las colecciones. Los resultados se devuelven en formato JSON.
2. **Transformación** de esos resultados a formato XML.
3. Aplicación de **plantillas XSLT** para generar documentos HTML a partir del XML.

### Entrada del script
- Credenciales de la base de datos MongoDB.
- Archivo TXT con la especificación de la consulta.
- Plantilla XSLT.

### Salida del script
- Documento HTML generado a partir de la consulta y la plantilla XSLT.

> [!warning]  
> No sé si poner las consultas aqui fuera y dentro el código de las consultas, o dentro las consultas y ya (que me faltan cambiarlas)
<details>
<summary>Ver ejemplos de consultas</summary>
 
- Consulta 1: Numero de tratamientos de cada tipo que se han aplicado en cada hospital
- Consulta 2: dni, sexo, etnia y fecha de nacimiento de los mayores de 50 que han recibido tratamiento para el tratamiento de cancer de mama triple negativo.
- Consulta 3: Por cada tratamiento, edad media de los pacientes cuando se les aplicó

</details>


El script y los ejemplos están disponibles en la carpeta `code/consultas_mongoDB`. Ten en cuenta que para ejecutar las consultas se requieren credenciales para acceder a la base de datos.

---

## Diseño de ontología en Protege y consultas SPARQL

En esta fase, se diseñó una ontología utilizando **protégé**, basada en las colecciones interconectadas de la base de datos. La ontología incluye tanto **propiedades de objeto** que reflejan las relaciones entre las clases (por ejemplo, entre *Hospital* y *Paciente*) como **propiedades de datos** que modelan los datos literales (por ejemplo, el nombre de un hospital o la fecha de un tratamiento).

### Estructura de la ontología

<details>
<summary> Clases de la ontología: </summary>
 
- **Departamento**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Departamento`

- **Historial**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Historial`

- **Hospital**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Hospital`

- **Medicamento**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Medicamento`

- **Medico**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Medico`

- **Paciente**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Paciente`

- **Parametro_Monitorizacion**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Parametro_Monitorizacion`

- **Tratamiento**  
  `http://www.semanticweb.org/ontologies/2024/10/proyectoEstandares#Tratamiento`

</details>

<details>
<summary> Propiedades de objetos de la ontología: </summary>
 
- **departamento_contiene_medicos**  
  Relación inversa: `medico_es_contenido_por_departamento`  
  Dominio: `Departamento`  
  Rango: `Medico`

- **departamento_es_contenido_por_hospital**  
  Relación inversa: `hospital_contiene_departamento`  
  Dominio: `Departamento`  
  Rango: `Hospital`

- **historial_hecho_en_hospital**  
  Relación inversa: `hospital_tiene_historial`  
  Dominio: `Historial`  
  Rango: `Hospital`

- **historial_pertenece_a_paciente**  
  Relación inversa: `paciente_tiene_historial`  
  Dominio: `Historial`  
  Rango: `Paciente`

- **historial_tiene_tratamiento**  
  Relación inversa: `tratamiento_pertenece_a_historial`  
  Dominio: `Historial`  
  Rango: `Tratamiento`

- **hospital_contiene_departamento**  
  Dominio: `Hospital`  
  Rango: `Departamento`

- **hospital_tiene_historial**  
  Dominio: `Hospital`  
  Rango: `Historial`

- **hospital_tiene_tratamiento**  
  Relación inversa: `tratamiento_hecho_en_hospital`  
  Dominio: `Hospital`  
  Rango: `Tratamiento`

- **medicamento_se_administra_en_tratamiento**  
  Relación inversa: `tratamiento_es_administrado_medicamento`  
  Dominio: `Medicamento`  
  Rango: `Tratamiento`

- **medico_es_contenido_por_departamento**  
  Dominio: `Medico`  
  Rango: `Departamento`

- **paciente_tiene_historial**  
  Dominio: `Paciente`  
  Rango: `Historial`

- **parametro_necesita_ser_monitoreado_por_tratamiento**  
  Relación inversa: `tratamiento_necesita_monitorear_parametro_de_monitorizacion`  
  Dominio: `Parametro_Monitorizacion`  
  Rango: `Tratamiento`

</details>



### Razonamiento

Se utilizó un razonador para mejorar la accesibilidad de la información y permitir la inferencia de nuevas relaciones, tal como se indica.

### Consultas SPARQL

Se diseñaron 6 consultas **SPARQL** para explorar el espacio de búsqueda de la ontología. A continuación se muestran ejemplos de las consultas implementadas:

1. **Lista de tratamientos por hospital**.
2. **Listar los tratamientos aplicados a pacientes mayores de 50 años**.
?

Las consultas y sus resultados se encuentran en el archivo `consultas.txt`, mientras que la ontología generada y razonada está en los archivos `?.owl`.

### Generación de grafo RDF y ejecución de consultas en Python

Se implementó un **script en Python** utilizando la librería **RDFlib** para:

1. Generar un grafo de tripletas **RDF** con los individuos extraídos de la base de datos **MongoDB**.
2. Ejecutar las consultas **SPARQL** diseñadas en el punto anterior sobre el grafo generado.

El script se encuentra en el archivo `?.py`.



## Autores

  _Autor:_ [martacuevasr](https://github.com/martacuevasr)

  _Autor:_ [Diegodepab](https://github.com/Diegodepab)

   _Autor:_ [rgCarmen](https://github.com/rgCarmen)

   _Autor:_ [GonzaloM786](https://github.com/GonzaloM786)

 _Autor:_ [AlexSilvaa9](https://github.com/AlexSilvaa9)

