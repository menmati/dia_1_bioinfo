import os # Improtamos la librería para interactuar con el sistema operativo

# 1. Definir la ruta de la carpeta
carpeta_datos = "datos"

# 2. Obtener una lista con todos los archivos de esa carpeta
archivos = os.listdir(carpeta_datos)

# 3. Iniciar un bucle (loop) para revisar cada archivo de la lista
for archivo_nombre in archivos:
    # 4. Verificar que el archivo termina en .fasta
    if archivo_nombre.endswith(".fasta"):
        # 5. Construir la ruta completa al archivo (ej.: datos/gen1.fasta)
        ruta_completa = os.path.join(carpeta_datos, archivo_nombre)
        # 6. Abrir y leer el archivo (código de ayer)
        with open(ruta_completa, "r") as archivo_abierto:
            lineas = archivo_abierto.readlines()
        # Extraer la secuencia y calcular
        secuencia = lineas[1].strip()
        longitud = len(secuencia)
        conteo_g = secuencia.count("G")
        conteo_c = secuencia.count("C")
        # Evitar división por cero si el archivo estuviera vacío
        if longitud > 0:
            contenido_gc = ((conteo_g + conteo_c) / longitud) * 100
            print(f"Archivo: {archivo_nombre} | Secuencia: {secuencia} | Contenido GC: {contenido_gc:.2f}%")
        else:
            print(f"Archivo: {archivo_nombre} está vacío o no tiene secuencia válida.")