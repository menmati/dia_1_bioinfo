# Abrir y leer el archivo FASTA
with open("datos/adn.fasta", "r") as archivo:
    lineas = archivo.readlines()

# Extraer solo la secuencia de ADN (la segunda línea)
secuencia = lineas[1].strip()

# Contar la longitud de la cadena
longitud = len(secuencia)

print(f"El archivo ha sido leído con éxito.")
print(f"La secuencia analizada es: {secuencia}")
print(f"La longitud de la secuencia de ADN es de {longitud} nucleótidos.")