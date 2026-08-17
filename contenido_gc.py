# 1. Abrir y leer el nuevo archivo FASTA
with open("datos/gen_gc.fasta", "r") as archivo:
    lineas = archivo.readlines()

# 2. Extraer y limpiar la secuencia (segunda línea)
secuencia = lineas[1].strip()

# 3. Contar la longitud total (como la vez anterior)
longitud = len(secuencia)

# 4. Contar cuántas 'G' y 'C' hay en la secuencia
conteo_g = secuencia.count("G")
conteo_c = secuencia.count("C")

# 5. Calcular el porcentaje de contenido GC
contenido_gc = ((conteo_g + conteo_c) / longitud) * 100

# 6. Mostrar el resultado formateado
print(f"Secuencia analizada: {secuencia}")
print(f"Longitud total: {longitud} nucleótidos.")
# El .2f dentro de las llaves le dice a Python que solo muestre 2 decimales
print(f"El Contenido GC es del {contenido_gc:.2f} %.")



