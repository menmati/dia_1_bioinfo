import matplotlib.pyplot as plt

# 1. Datos simulados
tiempo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen1 = [2, 5, 3, 8, 2, 11, 15, 16, 8, 3]
gen2 = [6, 7, 2, 12, 1, 14, 12, 10, 4, 2]

# 2. Crear Figura y Ejes (Subplots horizontales: 1 fila, 2 columnas)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Análisis de Expresión Génica (Interfaz OO)')

# 3. Configurar el Eje 1 (ax1)
ax1.plot(tiempo, gen1, label = 'Gen 1', color = 'red', marker = 'o',
         linestyle = 'dashed', linewidth = 2)
ax1.set_xlabel('Tiempo (horas)')
ax1.set_ylabel('Nivel de Expresión')
ax1.set_title('Dinámica del Gen 1')
ax1.legend()

# 4. Configurar el Eje 2 (ax2)
ax2.plot(tiempo, gen2, label = 'Gen 2', color = 'green', marker = '^',
         linestyle = 'dotted', linewidth = 2)
ax2.set_xlabel('Tiempo (horas)')
ax2.set_title('Dinámica del Gen 2')
ax2.legend()

# 5. GUARDAR EL GRÁFICO (Práctica profesional en lugar de plt.show())
# Guardamos la imagen directamente en nuestra carpeta 'graficos'
plt.savefig('gráficos/subplots_genes.png')
print("¡Éxito! El gráfico se ha guardado en la carpeta 'graficos'.")