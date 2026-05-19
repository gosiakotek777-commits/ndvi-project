import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🌍 Analiza NDVI - lesistość")

np.random.seed(42)
red = np.random.uniform(0.1, 0.8, (200, 200))
nir = np.random.uniform(0.2, 1.0, (200, 200))

ndvi = (nir - red) / (nir + red)

forest_mask = ndvi > 0.6
forest_percent = np.sum(forest_mask) / ndvi.size * 100

st.write(f"🌲 Lesistość: {forest_percent:.2f}%")

fig, ax = plt.subplots()
ax.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
ax.set_title("NDVI")
ax.axis("off")

st.pyplot(fig)
