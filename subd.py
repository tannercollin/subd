import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print "Connected to server."

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost")

client.loop_start()
