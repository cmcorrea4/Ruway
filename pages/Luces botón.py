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

st.title("Luces")
st.subheader("CONTROL POR BOTÓN")

image = Image.open('Casco render.png')

st.image(image, width=400)


if st.button('Encender'):
    act1="ON"
    client1= paho.Client("MMMa")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"casco":act1})
    ret= client1.publish("Cosplay/Casco", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Apagar'):
    act1="OFF"
    client1= paho.Client("MMMa")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"casco":act1})
    ret= client1.publish("Cosplay/Casco", message)
  
    
else:
    st.write('')


