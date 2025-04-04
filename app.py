import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st
st.title("Esto es una app")
 
year = st.selectbox("Seleccione un año", [2022, 2023, 2024])
 
 
 
if year == 2022:
 
    tgp_M = gpd.read_parquet('hombres22.parquet')
    tgp_F = gpd.read_parquet('mujeres22.parquet')
 
elif year == 2023:
    tgp_M = gpd.read_parquet('hombres23.parquet')
    tgp_F = gpd.read_parquet('mujeres23.parquet')
 
else:
    tgp_M = gpd.read_parquet('hombres.parquet')
    tgp_F = gpd.read_parquet('mujeres.parquet')
 
 
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
tgp_M.plot(column='FT', ax=ax[0], legend=True)
tgp_F.plot(column='FT', ax=ax[1], legend=True)
 
ax[0].set_title('TGP - Hombres')
ax[1].set_title('TGP - Mujeres')
ax[0].axis('off')
ax[1].axis('off')
 
fig.tight_layout()
fig.savefig('tgp.png')
 
st.pyplot(fig)