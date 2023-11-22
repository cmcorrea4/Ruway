import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Miguel Alonso Aragón")
image = Image.open('imagen voz.png')

st.image(image, width=700)


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Llegada a un nuevo mundo.")
st.subheader("Lee su historia")
st.write('Aqui encontrarás la narración de la contrucción del nuevo mundo '  
         'La historia de Miguel Alonso Aragón y su expedición y adentramiento en esta cultura. '   
         'Ponte los audifonos y acompañanos en esta increible historia. ')
           

#text = st.text_input("Ingrese el texto.")
text = ('En el siglo XV, un navegante italiano, '
        'financiado por la Corona de Castilla para encontrar una ruta a las Indias Orientales, '
        'accidentalmente llega a América, desconocida para los europeos. '
        'Después de conflictos y saqueos, Miguel Alonso Aragón, único superviviente de la expedición, '
        'es confundido por los holkanes como un ave y llevado a Uxmal. '
        'Tras aprender el idioma, Aragón convence al descendiente de Dios en Tikal de financiar una expedición a Europa. '
        'Sin embargo, al regresar con riquezas, Aragón es ejecutado por traición, desencadenando la furia maya. '
        'Durante 100 años, el Imperio Maya ataca Europa, propagando una peste que debilita al continente. '
        'Finalmente, con Europa derrotada, el continente americano, liderado por el Imperio Maya,'
        'florece tecnológicamente con Nukal como centro. ')
tld="es"

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

#if st.button("convertir"):
result, output_text = text_to_speech(text, tld)
audio_file = open(f"temp/{result}.mp3", "rb")
audio_bytes = audio_file.read()
st.markdown(f"## Escucha su historia:")
st.audio(audio_bytes, format="audio/mp3", start_time=0)

   # if display_output_text:
   # st.markdown(f"## Texto en audio:")
   # st.write(f" {output_text}")


#def remove_files(n):
 #   mp3_files = glob.glob("temp/*mp3")
 #   if len(mp3_files) != 0:
  #      now = time.time()
   #     n_days = n * 86400
    #    for f in mp3_files:
     #       if os.stat(f).st_mtime < now - n_days:
      #          os.remove(f)
       #         print("Deleted ", f)


#remove_files(7)
