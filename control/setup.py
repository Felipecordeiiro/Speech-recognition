# commands serve para restringir o que chega no arduino. Possivelmente usaremos regex para caso o 
# modelo retorne uma palavra errada, mas semelhante a alguma chave existente.
# ANALISAR SE FAZ SENTIDO TER ESSE DICT!

commands = [
    'Ligar',
    'Desligar',
]

DATA_PAYLOAD = 2048
SERVER_ADDRESS = ('localhost', 12345)
ARDUINO_SERIAL_PORT = '/dev/ttyACM0'