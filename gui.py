import streamlit as st
import pyaudio
import wave
import numpy as np
import cv2
import time
import colorama
colorama.init()

# Configurações de gravação
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 2048

# Inicializa PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# URL do stream da câmera IP
camera_url = 'https://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1'
cap = cv2.VideoCapture(camera_url)

# Título do aplicativo
st.title("Captura de Áudio")

aux_area = st.empty()



# Inicia a captura de áudio
audio_frames = []
status_placeholder = st.empty()
while True:
    ret, frame = cap.read()
    try:
        if not ret:
            aux_area.write("Erro ao capturar vídeo.")

        # Converte a imagem de BGR para RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Exibe o frame no Streamlit
        st.image(frame, channels='RGB', use_column_width=True)
    except:
        pass


    try:
        data = stream.read(CHUNK)
        status_placeholder.write(data)
        audio_frames.append(data)
    except:
        break

# Para o stream de áudio
stream.stop_stream()
stream.close()
p.terminate()
# Libera o objeto de captura quando terminar
cap.release()

# # Salva o áudio gravado
# if audio_frames:
#     with wave.open("audio_output.wav", 'wb') as wf:
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(audio_frames))
#     st.success("Áudio gravado com sucesso como 'audio_output.wav'.")