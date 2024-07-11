import vosk
import pyaudio
import json

# Configure o modelo Vosk (baixe um modelo adequado para seu idioma)
model = vosk.Model("vosk-model-small-pt-0.3")
rec = vosk.KaldiRecognizer(model, 16000)

# Configure o PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Começando a reconhecer. Fale algo...")

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print(result['text'])

print("Reconhecimento finalizado.")

stream.stop_stream()
stream.close()
p.terminate()