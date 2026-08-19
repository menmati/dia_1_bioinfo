import matplotlib.pyplot as plt

# 1. Datos simulados: Tiempo (horas) y cantidad de bacterias (UFC)
tiempo = [0, 2, 4, 6, 8, 10]
cepa_salvaje = [10, 50, 200, 800, 1500, 1600]
cepa_mutante = [10, 30, 80, 200, 400, 450]

# 2. Estilos predefinidos
# Aplicamos un estilo limpio (equivalente a 'seaborn')
plt.style.use('ggplot')

# 3. Representar varias líneas con personalización
plt.plot(tiempo, cepa_salvaje, label = "Cepa Salvaje", color = "blue",
         marker = "o", linestyle = "solid", linewidth = 2, markersize = 8)
# Usamos alpha=0.6 para darle transparencia a la línea de la mutante
plt.plot(tiempo, cepa_mutante, label = "Cepa Mutante", color = "red",
         marker = "x", linestyle = "dashed", linewidth = 2, markersize = 8,
         alpha=0.6)

# 4. Añadir etiquetas y título
plt.xlabel("Tiempo (horas)")
plt.ylabel("Bacterias (UFC)")
plt.title("Curva de Crecimiento Bacteriano (Interfaz Pyplot)")

# 5. Ajustar manualmente los límites de los ejes
# [x_min, x_max, y_min, y_max]
plt.axis([0, 10, 0, 1800])

# 6. Mostrar la leyenda
plt.legend()

# 7. Guardar el gráfico
plt.savefig('gráficos/intro_crecimiento.png')
print("¡Éxito! El gráfico de crecimiento se ha guardado" \
"en 'graficos/intro_crecimiento.png'.")



