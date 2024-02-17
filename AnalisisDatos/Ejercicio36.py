#Datos geoespaciales

import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Crear un GeoDataFrame de ejemplo
np.random.seed(42)
gdf = gpd.GeoDataFrame(geometry=[Point(np.random.uniform(-180, 180), np.random.uniform(-90, 90)) for _ in range(100)])
gdf['variable_a_visualizar'] = np.random.rand(100)
gdf['variable_b_visualizar'] = np.random.rand(100)

# Solución
sns.kdeplot(data=gdf, x='variable_a_visualizar', y='variable_b_visualizar', fill=True, cmap='viridis')
plt.title('Visualización Geoespacial')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()
