import whisper
import pyaudio
import numpy as np

# Carregue o modelo Whisper (escolha o tamanho adequado)
model = whisper.load_model("small")

# Configure o PyAudio para captura de áudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=2048)

try:
    while True:
        # Capture áudio
        print("Estamos capturando seu microfone")
        data = stream.read(2048)
        audio_data = np.frombuffer(data, dtype=np.float32)
        
        # Transcreva o áudio
        result = model.transcribe(audio_data)
        
        # Imprima o resultado
        print(result["text"])
        
except KeyboardInterrupt:
    print("Transcrição encerrada.")

finally:
    # Encerre o stream de áudio
    stream.stop_stream()
    stream.close()
    p.terminate()