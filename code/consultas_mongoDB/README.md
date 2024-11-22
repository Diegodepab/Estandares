## Consultas

#### Consulta 1
Lista de tratamientos realizados en cada Hospital, y el número de veces que se han realizado. Solo se han mostrados aquellos realizados más de 1 vez.

#### Consulta 2
Información de los pacientes  mayores de 50 que han recibido un tratamiento de Diabetes Tipo 2.

#### Consulta 3
Información general de los tratamientos y la edad media de los pacientes que lo han recibido.

---

## Ejecución

<code> python3 queryRunner.py --credenciales *credenciales.json* --consulta *fichero_consulta* --xslt *fichero_xslt* --salida *nombre_salida* <code>

Ejemplo:
<code> python3 queryRunner.py --credenciales ./data/credenciales.json --consulta ./data/consulta1.txt --xslt ./data/consulta1.xslt --salida consulta1.html <code>