import serial
from setup import ARDUINO_SERIAL_PORT
import time


class ArduinoError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"ArduinoError: {self.mensagem}"
    

def send_to_arduino(command):
    arduino = None
    try:  # Tenta se conectar...
        arduino = serial.Serial(ARDUINO_SERIAL_PORT, 9600)
        print('Arduino connected!')

        try: # Tenta enviar....
            arduino.write(bytes(command, 'utf-8'))
            print(f'\t* Command "{command}" sent!')
        except Exception as e:
            raise ArduinoError(f'Failed to send to Arduino! {e}')

    except Exception as e:
        raise ArduinoError(f'Failed to connect to Arduino! {e}')

    finally:
        if arduino:
            arduino.flush() #Limpa a comunicação
            arduino.close() # Fecha a conexão
        print('Closed arduino connection!')