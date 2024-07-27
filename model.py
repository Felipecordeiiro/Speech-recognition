import speech_recognition as sr
import pyttsx3
import vosk
import pyaudio
import json

# Inicializa o recognizer e o motor de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Configure o modelo Vosk (baixe um modelo adequado para seu idioma)
new_model = vosk.Model("vosk-model-small-pt-0.3")
rec = vosk.KaldiRecognizer(new_model, 16000)

# Configure o PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Começando a reconhecer. Fale algo...")

while True:
    data = stream.read(4000)
    if len(data) == 0:
        speak("Finalizando controle")
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        
        ## Comandos
        if "esquerda" in result["text"]:
            result["text"]
        elif "direita" in result["text"]:
            result["text"]
        elif "baixo" in result["text"]:
            result["text"]
        elif "cima" in result["text"]:
            result["text"]
        elif "abrir garra" in result["text"]:
            result["text"]
        elif "fechar garra" in result["text"]:
            result["text"]
        elif "escovação" in result["text"]:
            result["text"]

print("Reconhecimento finalizado.")

stream.stop_stream()
stream.close()
p.terminate()