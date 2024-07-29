import speech_recognition as sr
import pyttsx3
import vosk
import pyaudio
import json
import queue

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

print("Começando a reconhecer. Fale algo...")
def capture_speech(command_queue):
    # Inicializa o recognizer e o motor de texto para fala
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    # Configure o modelo Vosk (baixe um modelo adequado para seu idioma)
    new_model = vosk.Model("models/vosk-model-small-pt-0.3")
    rec = vosk.KaldiRecognizer(new_model, 16000)

    # Configure o PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    stream.start_stream()
    while True:
        data = stream.read(4000)
        if len(data) == 0:
            speak(engine, "Finalizando controle")
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            
            ## Comandos
            if "esquerda" in result["text"]:
                result["text"]
                command_queue.put("esquerda")
            elif "direita" in result["text"]:
                result["text"]
                command_queue.put("direita")
            elif "baixo" in result["text"]:
                result["text"]
                command_queue.put("baixo")
            elif "cima" in result["text"]:
                result["text"]
                command_queue.put("cima")
            elif "abrir" in result["text"]:
                result["text"]
                command_queue.put("abrir")
            elif "fechar" in result["text"]:
                result["text"]
                command_queue.put("fechar")
            elif "escovar" in result["text"]:
                result["text"]
                command_queue.put("escovar")

    print("Reconhecimento finalizado.")
    stream.stop_stream()
    stream.close()
    p.terminate()   
    