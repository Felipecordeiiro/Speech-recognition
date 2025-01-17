from application.configs.broker_configs import mqtt_broker_configs
from .mqtt_connection.mqtt_client_connect import MqttClientConnection

def start():
    mqtt_client_connection = MqttClientConnection(
        mqtt_broker_configs["HOST"],
        mqtt_broker_configs["PORT"],
        mqtt_broker_configs["CLIENT_NAME"],
        mqtt_broker_configs["KEPPALIVE"]
        )
    mqtt_client_connection.start_connection()