import paho.mqtt.client as paho
import time
import streamlit as st
from PIL import Image
import json
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

st.title("El DISCO DE LA ENCARNACIÓN")

st.subheader("PLEGARIAS")


image = Image.open('Invoc.png')

st.image(image)

st.write('Cada día los habitantes de tikal mandaN sus plegarias por medio del disco de la encarnación, para que una vez al año, el ascendido se encarne como hombre. '
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

#if st.button('DESACTIVAR'):
#    act1="OFF"
#    client1= paho.Client("MMMa")                           
#    client1.on_publish = on_publish                          
#    client1.connect(broker,port)  
#    message =json.dumps({"escudo_p":act1})
#    ret= client1.publish("escudo_p", message)
  
    
#else:
#    st.write('')


