import numpy as np
import matplotlib.pyplot as plt

# 🔥 symulacja danych satelitarnych (jak Sentinel)
np.random.seed(42)

# "RED" i "NIR" jak z satelity
red = np.random.uniform(0.1, 0.8, (200, 200))
nir = np.random.uniform(0.2, 1.0, (200, 200))

# NDVI
ndvi = (nir - red) / (nir + red)
forest = np.sum(ndvi > 0.6)
fields = np.sum((ndvi <= 0.6) & (ndvi > 0.2))
bare = np.sum(ndvi <= 0.2)

total = ndvi.size

print("🌲 Lasy:", forest / total * 100, "%")
print("🌾 Roślinność/pola:", fields / total * 100, "%")
print("🟥 Brak roślin:", bare / total * 100, "%")

# procent lasu (NDVI > 0.4)
forest_mask = ndvi > 0.4
forest_percent = np.sum(forest_mask) / ndvi.size * 100

print(f"🌲 Lesistość NDVI: {forest_percent:.2f}%")
print("\n--- PODSUMOWANIE ---")
print(f"NDVI min: {ndvi.min():.2f}")
print(f"NDVI max: {ndvi.max():.2f}")

# mapa
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.title("NDVI - analiza lasów (symulacja danych satelitarnych)")
plt.colorbar()
plt.axis("off")
plt.show()
