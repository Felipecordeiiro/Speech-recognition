import paho.mqtt.client as mqtt

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client = client
        self.__keepalive = keepalive
    
    def start_connection(self):
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=self.__client)
        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive)
        mqtt_client.loop_start() # Define o looping para leitura de novas informações
        