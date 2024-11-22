
Hola Carmen o quien quiera que lea, simplificando

### 1. `nombre_tratamiento`
Este campo contiene los nombres de los tratamientos médicos utilizados para diversas condiciones y enfermedades. Los tratamientos pueden ser farmacológicos, terapias físicas, intervenciones quirúrgicas, o cualquier otro tipo de intervención utilizada en la atención médica. Ejemplos incluyen "Tratamiento Antirretroviral", "Terapia con Insulina", "Tratamiento de Cáncer de Pulmón", entre otros. (puse 200)

### 2. `descripcion`
En este campo se describe el tratamiento en detalle. La descripción incluye información sobre cómo funciona el tratamiento, sus objetivos, y cómo debe ser administrado. Ejemplos pueden ser "Tratamiento con medicamentos antivirales para controlar la replicación del VIH y mejorar la función inmunitaria." o "Protocolo de medicamentos y cambios en el estilo de vida para reducir la presión arterial elevada."**(puse 200 intentando que estuviera en orden al nombre de tratamiento ya que no tiene sentido poner tratamiento de covid y que la descripción sea curar las ronchas generadas por sarna)**

### 3. `enfermedades`
Este campo incluye el nombre de la enfermedad o condición que el tratamiento está diseñado para abordar. Ejemplos incluyen "COVID-19", "Hipertensión Arterial", "Diabetes Tipo 2", entre otros.

#### Campos adicionales para `enfermedades`:
- **`categoria`**  
  Indica la categoría o clasificación general de la enfermedad. Ejemplos incluyen "Infección viral", "Enfermedad crónica", "Trastorno metabólico", entre otros.

- **`sintomas`**  
  Contiene los síntomas asociados con la enfermedad. Ejemplos incluyen "Fiebre", "Fatiga", "Dolor en el pecho", "Náuseas".

- **`estado_severidad`**  
  Descripción del nivel de severidad de la enfermedad o tratamiento. Ejemplos incluyen "Leve (1)", "Moderado (2)", "Severo(3)", "Crítico(5)", etc. poniendo el número para indicar la severidad junto a una palabra que ayude a interpretar

### 4. `regimen`
Este grupo de datos describe los parámetros asociados con el tratamiento de los pacientes, tales como la duración, frecuencia de la dosis y el método de administración.

#### Campos de `regimen`:
- **`duracion_dias`**  
  La duración del tratamiento en días. Ejemplo: 7, 14, 30 días.

- **`frecuencia_dosis`**  
  Especifica cuán frecuentemente debe administrarse el tratamiento. Ejemplos incluyen "Cada 12 horas", "Diariamente", "Cada 3 días".

- **`via_administracion`**  
  Indica cómo debe administrarse el tratamiento. Ejemplos incluyen "Oral", "Intravenosa (IV)", "Subcutánea".

#### **`monitorizacion`**:
Especifica el seguimiento y monitoreo del paciente durante el tratamiento.

- **`frecuencia_monitorizacion`**  
  Indica la frecuencia con la que se debe realizar la monitorización del paciente. Ejemplos incluyen "Cada 24 horas", "Cada 3 días", "1 hora después de la dosis".

##### **`parametros`**:
Describe los parámetros que deben ser monitoreados.

- **`nombre_parametro`**  
  El nombre del parámetro que se monitoriza. Ejemplos incluyen "Glucosa en sangre", "Niveles de oxígeno", "Presión arterial".

-  **IMPORTANTE BORRE LE PARAMETRO UNIDAD PORQUE 1 QUE COÑAZO 2 ME PARECE QUE SOLO ES AUMENTAR LA PROBABILIDAD DE OBTENER RESULTADOS SIN SENTIDOS**

- **`valor_referencia`**  
  El valor de referencia para el parámetro monitorizado. Ejemplos incluyen "70-100 mg/dL", "95-100", "120/80". **este tuve problema imaginando que poner que quede bien en caso de automatizar aleatoriamente :)** 

### 5. `medicamentos`
Este grupo incluye los detalles relacionados con los medicamentos administrados a los pacientes.

- **`nombre`**  
  El nombre del medicamento. Ejemplos incluyen "Ibuprofeno", "Acetaminofén", "Insulina".

- **`frecuencia`**  
  La frecuencia con la que debe tomarse el medicamento. Ejemplos incluyen "Cada 8 horas", "Diariamente", "Solo cuando se presenten síntomas".

- **`efectos_secundarios`**  
  Los efectos secundarios posibles del medicamento. Ejemplos incluyen "Náuseas", "Somnolencia", "Mareos", "Dolor de estómago".

#### **`interacciones`**:
Describe las interacciones con otros medicamentos.

- **`medicamento_interaccion`**  
  El nombre del medicamento con el que puede haber una interacción. Ejemplos incluyen "Hidroxicloroquina", "Insulina".

- **`efecto_interaccion`**  
  Describe el efecto que la interacción puede causar. Ejemplos incluyen "Inhibe la eficacia", "Aumenta la toxicidad", "Reduce la absorción".
