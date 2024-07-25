import socket
from setup import *


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

command = input('Write a command: ')

client_socket.sendall(command.encode('utf-8'))
data = client_socket.recv(DATA_PAYLOAD)
print(f"{data.decode('utf-8')}")

client_socket.close()