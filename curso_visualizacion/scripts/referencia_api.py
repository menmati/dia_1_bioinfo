import matplotlib.pyplot as plt

# 1. Datos simulados: Concentración de dos proteínas (mg/mL) a lo largo del tiempo
tiempo = [0, 10, 20, 30, 40, 50]
proteina_a = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6]
proteina_b = [3.0, 2.5, 1.8, 1.2, 0.7, 0.2]
# Creamos la Figure y el Axes usando la Object-Oriented API
fig, ax = plt.subplots(figsize = (8, 6))

# 2. Uso de notación abreviada (fmt)
# 'ro--' significa: red (rojo), circle marker (círculo), dashed line (línea discontinua)
ax.plot(tiempo, proteina_a, 'ro--', label = 'Proteína A (Notación fmt)')

# 3. Uso de Keyword Arguments (Recomendado)
# Más largo de escribir, pero más fácil de leer y mantener
ax.plot(tiempo, proteina_b, color = 'blue', marker = 's', # 's' de square (cuadrado)
        linestyle = 'solid', linewidth = 2, markersize = 8,
        label = 'Proteína B (Keyword args)')

# 4. Configuración del Axes usando las funciones de su clase
ax.set_title('Dinámica de Proteínas: API y parámetros de Line2D')
ax.set_xlabel('Tiempo (minutos)')
ax.set_ylabel('Concentración (mg/mL)')
ax.legend()

# 5. Guardado
plt.savefig('gráficos/comparación_api.png')
print("¡Éxito! El gráfico se ha guardado en 'gráficos/comparación_api.png'.")