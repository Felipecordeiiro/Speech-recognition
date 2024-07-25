import serial
import socket
from setup import *
""" socket client (command) -> socket server (listen + send signals) -> arduino -> ... """


class ArduinoError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"ArduinoError: {self.mensagem}"


def send_to_arduino(command):
    try:  # Tenta se conectar....
        arduino = serial.Serial(ARDUINO_SERIAL_PORT, 9600)
        print('Arduino conectado')

        try: # Tenta enviar....
            if command == 'l': #Se a resposta for "l", ele envia este comando ao Arduino
                arduino.write('l'.encode())

            elif command == 'd': #Senão, envia o "d"
                arduino.write('d'.encode())
        except ArduinoError('Failed to send to Arduino!') as ae:
            print(str(ae))


    except ArduinoError('Failed to connect to Arduino!') as ae2:
        print(str(ae2))

    finally:
        arduino.flush() #Limpa a comunicação

   

def run_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(1)
    print(f"Server is listening in port {SERVER_ADDRESS[1]}...")


    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        data = conn.recv(DATA_PAYLOAD).decode('utf')
        try:
            command = commands[data]
            print(f"Command received: {command}")
            # send_to_arduino(command)
            conn.sendall(b"Hello from the server!")

        except KeyError:
            conn.sendall(b'ERROR: Invalid Command!')

        except ArduinoError as ae:
            conn.sendall(bytes(f'ERROR: {str(ae)}'))
            

        finally:
            conn.close()


if __name__ == "__main__":
    run_server()