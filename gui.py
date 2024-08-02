import streamlit as st
import pyaudio
import wave
import numpy as np
import cv2
import time
import colorama
import json
import vosk
import speech_recognition as sr
import pyttsx3
from colorama import Fore, Back, Style
colorama.init()
from control.http import client
from comandos import command_dict

# Configurações de gravação
FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 16000
CHUNK = 8000

# Inicializa o recognizer e o motor de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
     engine.say(text)
     engine.runAndWait()


# Inicializa PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=FRAME_RATE, input=True, frames_per_buffer=CHUNK)
stream.start_stream()

# Título do aplicativo
st.title("Captura de Áudio")

aux_area = st.empty()
if 'model' not in st.session_state:
    # Configure o modelo Vosk (baixe um modelo adequado para seu idioma)
    new_model = vosk.Model("models/vosk-model-small-pt-0.3")
    rec = vosk.KaldiRecognizer(new_model, FRAME_RATE)
    st.session_state.model = new_model
    st.session_state.rec = rec 

text_area = st.empty()


# # Inicia a captura de áudio
# audio_frames = []
# ret, frame = cap.read()
# try:
#     if not ret:
#         aux_area.write("Erro ao capturar vídeo.")

#     # Converte a imagem de BGR para RGB
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Exibe o frame no Streamlit
#     st.image(frame, channels='RGB', use_column_width=True)
# except:
#     pass

while True:
    try:
        data = stream.read(CHUNK)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            print(f"Você disse: {result}")
            text_area.write(result['text'])
            ## Comandos
            if "esquerda" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['esquerda'])
            elif "direita" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['direita'])
            elif "baixo" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['baixo'])
            elif "cima" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['cima'])
            elif "abrir garra" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['abrir garra'])
            elif "fechar garra" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['fechar garra'])
            elif "escovação" in result["text"]:
                print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
                client.send_command(command_dict['escovação'])
    except:
        # Para o stream de áudio
        stream.stop_stream()
        stream.close()
        p.terminate()

# # Salva o áudio gravado
# if audio_frames:
#     with wave.open("audio_output.wav", 'wb') as wf:
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(audio_frames))
#     st.success("Áudio gravado com sucesso como 'audio_output.wav'.")