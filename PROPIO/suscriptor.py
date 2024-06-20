import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#") 

def on_message(client, userdata, msg):
    
    payload = msg.payload.decode()
    parts = payload.split('|')
    timestamp = parts[1]
    state = int(parts[3])
    sensor_type = parts[5]

    print(f"Topic: {msg.topic}")
    
    print(f"Timestamp: {timestamp}")
    print(f"State: {state}")
    print(f"Sensor Type: {sensor_type}")
    print(f"payload: {payload}")
    print(f"parts: {parts}")
    
    print("---")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
