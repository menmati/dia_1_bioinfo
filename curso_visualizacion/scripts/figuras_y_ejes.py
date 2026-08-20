import matplotlib.pyplot as plt

# 1. Datos simulados
tiempo = [0, 2, 4, 6, 8, 10]
crecimiento = [100, 250, 500, 1200, 2100, 3000]
gen_a = [1.2, 2.4, 5.1, 8.0, 12.5, 15.0]
gen_b = [15.0, 14.2, 10.1, 5.5, 2.1, 1.0]
gen_c = [0.5, 0.6, 1.2, 3.1, 8.0, 14.2]

# 2. Crear la Figure (lienzo completo) y una matriz de 2x2 de Axes (subgráficos)
# figsize=(10, 8) define el ancho y alto del lienzo completo en pulgadas
fig, ax = plt.subplots(2, 2, figsize = (10, 8))
# Título global aplicado al objeto Figure
fig.suptitle('Figura 1: Ensayo Transcriptómico y Crecimiento', fontsize=16)

# 3. Configurar cada Axes mediante su posición (fila, columna)
# Panel A: Arriba a la izquierda [0, 0]
ax[0, 0].plot(tiempo, crecimiento, color = 'purple', marker = 'o')
ax[0, 0].set_title('A) Crecimiento Celular (OD600)')
ax[0, 0].set_xlabel('Tiempo (h)')
ax[0, 0].set_ylabel('Densidad Óptica')
# Panel B: Arriba a la derecha [0, 1]
ax[0, 1].plot(tiempo, gen_a, color = 'blue', marker = 's')
ax[0, 1].set_title('B) Gen A (Inducido)')
ax[0, 1].set_xlabel('Tiempo (h)')
ax[0, 1].set_ylabel('Nivel relativo')
# Panel C: Abajo a la izquierda [1, 0]
ax[1, 0].plot(tiempo, gen_b, color = 'red', marker = '^')
ax[1, 0].set_title('C) Gen B (Reprimido)')
ax[1, 0].set_xlabel('Tiempo (h)')
ax[1, 0].set_ylabel('Nivel relativo')
# Panel D: Abajo a la derecha [1, 1]
ax[1, 1].plot(tiempo, gen_c, color='green', marker='d')
ax[1, 1].set_title('D) Gen C (Tardío)')
ax[1, 1].set_xlabel('Tiempo (h)')
ax[1, 1].set_ylabel('Nivel relativo')

# 4. Ajustar el espaciado automático entre subplots para evitar solapamientos
plt.tight_layout()

# 5. Guardar la Figure completa en disco
plt.savefig('gráficos/panel_4_expresión.png')
print("¡Éxito! El panel de 4 subplots se ha guardado en 'gráficos/panel_4_expresión.png'.")


