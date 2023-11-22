import streamlit as st
from PIL import Image

st.title("Proyecto de cosplay Ruway")

st.header("Proyecto de cosplay original diseñado y desarrollado por la Universidad EAFIT")

image = Image.open("bocetación.png")
st.image(image, caption="Ruway")

st.write("Para saber más acerca del proyeto, ingresa en el siguiente link")

link_text = "[Más información](https://sites.google.com/view/proyectoqijtikal/inicio)"

# Mostrar el hipervínculo utilizando st.markdown
st.markdown(link_text, unsafe_allow_html=True)


