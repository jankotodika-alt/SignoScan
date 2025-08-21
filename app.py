import streamlit as st
from PIL import Image
import numpy as np
import os

st.title("SignoScan - Szignó felismerő")

# Fájl feltöltése
uploaded_file = st.file_uploader("Tölts fel egy szignót", type=["png","jpg","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Feltöltött szignó", use_column_width=True)

    # Szignó feldolgozás (egyszerű példa)
    st.write("Elemzés folyamatban...")
    # Itt lehetne a szignó felismerő algoritmus
    st.write("Ez egy demo. A szignót összehasonlítjuk a referencia képekkel, és a találatok itt jelennek meg.")
    
# Referencia képek feltöltése (opcionális)
st.sidebar.header("Referencia képek hozzáadása")
ref_uploaded = st.sidebar.file_uploader("Referencia kép feltöltése", type=["png","jpg","jpeg"])
if ref_uploaded is not None:
    ref_image = Image.open(ref_uploaded)
    st.sidebar.image(ref_image, caption="Referencia kép", use_column_width=True)
    st.sidebar.write("Kép hozzáadva a referencia adatbázishoz (demo).")
