# Actualización de Tratamientos por Hospital

Este script tiene como objetivo actualizar los datos de hospitales con los tratamientos disponibles en cada uno, utilizando la información de pacientes y sus historiales médicos.

## Archivos Utilizados

- **pacientes.json**: Contiene la información de los pacientes y sus historiales médicos.
- **tratamientos.json**: Incluye los detalles de los tratamientos disponibles.
- **hospitales.json**: Contiene los datos de los hospitales registrados.

## Proceso General

1. **Cargar los datos**: 
    - Se cargan los archivos `pacientes.json`, `tratamientos.json`, y `hospitales.json`.
    
2. **Procesamiento de tratamientos**: 
    - Se recorren los historiales de los pacientes para identificar los tratamientos aplicados en cada hospital.
    - Los tratamientos se almacenan por hospital evitando duplicados.

3. **Actualización de hospitales**:
    - Los hospitales se actualizan con los tratamientos posibles, agregando este nuevo campo: `tratamientos_posibles`.

4. **Guardado de datos**: 
    - Se genera un nuevo archivo `hospitales_actualizado.json` con los hospitales actualizados.

