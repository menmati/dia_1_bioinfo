import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el conjunto de datos integrado 'Iris'
# Esto descarga un DataFrame de Pandas automáticamente
iris = sns.load_dataset("iris")

# 2. Exploración del DataFrame
print("--- Primeras 5 filas del dataset Iris ---")
print(iris.head())
print("\n--- Nombres de las columnas (Características y Etiqueta) ---")
print(iris.columns.tolist())

# 3. La magia de Seaborn: Un gráfico complejo con una sola lína de código principal
# Vamos a representar la longitud del sépalo vs la anchura del sépalo coloreado por especie
sns.scatterplot(data = iris, x = "sepal_length", y = "sepal_width", hue = "species")

# 4. Uso de Matplotlib para retocar y guardar
plt.title("Análisis exploratorio: Sépalo de la flor Iris")
plt.savefig("gráficos/intro_seaborn_iris.png")
print("\n¡Éxito! El gráfico inicial de Seaborn se ha guardado en 'gráficos/intro_seaborn_iris.png'.")


