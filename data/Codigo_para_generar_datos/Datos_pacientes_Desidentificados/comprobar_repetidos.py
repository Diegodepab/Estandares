def verificar_repetidos(archivo):
    try:
        # Intentamos abrir el archivo con codificación 'utf-8'
        with open(archivo, 'r', encoding='utf-8') as file:
            # Leer todas las líneas del archivo y eliminar los saltos de línea
            lineas = [linea.strip() for linea in file.readlines()]
        
        # Crear un conjunto para verificar los elementos repetidos
        elementos_vistos = set()
        repetidos = []

        # Recorrer las líneas y verificar si ya se ha visto alguna
        for linea in lineas:
            if linea in elementos_vistos:
                repetidos.append(linea)
            else:
                elementos_vistos.add(linea)

        # Imprimir los resultados
        if repetidos:
            print("Se encontraron elementos repetidos:")
            for elemento in repetidos:
                print(elemento)
        else:
            print("No se encontraron elementos repetidos.")
    
    except UnicodeDecodeError:
        print(f"Error de codificación al intentar leer el archivo {archivo}.")
    except Exception as e:
        print(f"Se ha producido un error: {e}")

# Llamada a la función, pasando el nombre del archivo de texto
archivo = 'nombre_masculino_paciente.txt'  # Asegúrate de tener el archivo lista.txt en el mismo directorio
verificar_repetidos(archivo)
