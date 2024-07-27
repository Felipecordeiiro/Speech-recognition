import socket
from setup import *
from microcontrollers import arduino
""" socket client (command) -> socket server (listen + send signals) -> arduino -> ... """


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

        data = conn.recv(DATA_PAYLOAD).decode('utf-8')
        try:
            command = data
            print(f'Command received: "{command}". Sending to arduino...')
            arduino.send_to_arduino(command)

        except KeyError:
            conn.sendall(b'ERROR: Invalid Command!')

        except arduino.ArduinoError as ae:
            conn.sendall(bytes(f'ERROR: {str(ae)}'))
            

        finally:
            conn.close()


if __name__ == "__main__":
    run_server()