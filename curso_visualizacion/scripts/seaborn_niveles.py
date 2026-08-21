import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset integrado
iris = sns.load_dataset("iris")

# 2. Crear la Figure y los Axes (1 fila, 2 columnas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 5))
fig.suptitle('Integración Seaborn y Matplotlib: Análisis Morfológico Iris')

# 3. Gráfico 1 (Seaborn a nivel de Axes) asignado a ax1
sns.swarmplot(data = iris, x = "species", y = "petal_length", ax = ax1)
ax1.set_title('A) Distribución (Seaborn)')

# 4. Gráfico 2 (Matplotlib nativo) asignado a ax2
ax2.scatter(iris["petal_width"], iris["petal_length"], color = 'blue', alpha = 0.6)
ax2.set_xlabel('petal_width')
ax2.set_ylabel('petal_length')
ax2.set_title('B) Correlación (Matplotlib)')

# 5. Ajustar márgenes y guardar
plt.tight_layout()
plt.savefig('gráficos/seaborn_combinado.png')
print("¡Éxito! Panel combinado guardado en 'gráficos/seaborn_combinado.png'.")


