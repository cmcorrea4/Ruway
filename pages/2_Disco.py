import paho.mqtt.client as paho
import time
import streamlit as st
from PIL import Image
import json
from streamlit_drawable_canvas import st_canvas
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("MMMa")
client1.on_message = on_message

st.title("El DISCO DE LA ENCARNACIÓN.")

with st.sidebar:
    st.subheader("Acerca de:")
    st.subheader("En esta aplicación veremos la capacidad que ahora tiene una máquina de interpretar un boceto")
    bg_image = st.sidebar.file_uploader("Cargar Imagen:", type=["png", "jpg"])
    bg_color = st.color_picker("Color de Fondo", "#FFFFFF",key="2")
    stroke_color = st.color_picker("Color de Trazo", "#000000",key="1")
    stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5,key="A")
    #H_= st.sidebar.slider('Selecciona la altura del tablero ', 1, 400, 10,key="B")
    #W_= st.sidebar.slider('Selecciona el ancho del tablero', 1, 400, 10,key="C")
    
st.subheader("Dibuja el boceto en el panel  y presiona el botón para analizarla")


#realtime_update = st.sidebar.checkbox("Update in realtime", True)
drawing_mode = st.sidebar.selectbox(
    "Herramienta de dibujo:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    height=400,
    width=400,
    drawing_mode=drawing_mode,
    key="canvas",
)



image = Image.open('Invoc.png')

st.image(image)

st.write('Cada día los habitantes de tikal mandan sus plegarias por medio del disco de la encarnación, para que una vez al año, el ascendido se encarne como hombre. '
         'Poco a poco este se carga de la esencia de los mortales.')

if st.button('ELEVAR PLEGARIA'):
    act1="ON"
    client1= paho.Client("MMMa")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"escudo_p":act1})
    ret= client1.publish("escudo_p", message)
 
    
    
    
else:
    st.write('')

image = Image.open("logo.png")
st.image(image)
#if st.button('DESACTIVAR'):
#    act1="OFF"
#    client1= paho.Client("MMMa")                           
#    client1.on_publish = on_publish                          
#    client1.connect(broker,port)  
#    message =json.dumps({"escudo_p":act1})
#    ret= client1.publish("escudo_p", message)
  
    
#else:
#    st.write('')


