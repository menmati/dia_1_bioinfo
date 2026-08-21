import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración global del estilo de Seaborn
# Cambia 'darkgrid' por 'ticks' si prefieres un diseño más limpio para artículos científicos
sns.set_style("darkgrid")

# 2. Cargar el conjunto de datos
iris = sns.load_dataset("iris")

# 3. Crear el lienzo con Matplotlib
fig, ax = plt.subplots(figsize = (8, 6))

# 4. Crear el gráfico de dispersión con Seaborn (añadiendo 'hue' para la 3ª dimensión)
# Almacenamos el resultado en la variable 'gráfico_dispersión' (que es un objeto Axes)
gráfico_dispersión = sns.scatterplot(data = iris, x = "sepal_length", y = "sepal_width", 
    hue = "species", ax = ax)

# 5. Personalización utilizando los métodos de Matplotlib sobre el objeto Axes devuelto
gráfico_dispersión.set_title("Morfología del Sépalo: Comparación entre Especies de Iris",
                             fontsize = 14)
gráfico_dispersión.set_xlabel("Longitud del Sépalo (cm)")
gráfico_dispersión.set_ylabel("Anchura del Sépalo (cm)")

# 6. Guardar en disco
plt.tight_layout()
plt.savefig('gráficos/seaborn_personalizado.png')
print("¡Éxito! El gráfico se ha guardado en la carpeta 'gráficos/seaborn_personalizado.png'.")