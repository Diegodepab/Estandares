# Proyecto final: Estándares de Datos Abiertos e Integración de Datos

Este proyecto forma parte de la asignatura de **Estándares de Datos Abiertos e Integración de Datos**. Se centra en el diseño, poblamiento y consultas de una base de datos en MongoDB, además del manejo de dicha base se probara el uso de estándares y la transformación de diversos tipos de bases de datos como puede ser XML u otros formatos. 

## Índice
1. [T1 - Diseño y Poblamiento de la Base de Datos](#diseño-y-poblamiento-de-la-base-de-datos)
2. [T2 - Documentos XML y Vistas HTML mediante XSLT](#t2---documentos-xml-y-vistas-html-mediante-xslt)
3. [Autores](#Autores)

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

## T2 - Documentos XML y Vistas HTML mediante XSLT

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

## Autores

  _Autor:_ [martacuevasr](https://github.com/martacuevasr)

  _Autor:_ [Diegodepab](https://github.com/Diegodepab)

   _Autor:_ [rgCarmen](https://github.com/rgCarmen)

   _Autor:_ [GonzaloM786](https://github.com/GonzaloM786)

 _Autor:_ [AlexSilvaa9](https://github.com/AlexSilvaa9)

