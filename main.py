import speech_recognition as sr
import pyttsx3
import os

# Inicializa o recognizer e o motor de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        speak("Escutando comandos")
        print("\nListening for commands...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError:
            print("Erro ao se comunicar com o serviço de reconhecimento de voz.")
            return None

def execute_command(command):
    if "código principal" in command or "principal" in command:
        script_path = "model.py" 
        speak("Iniciando o reconhecimento de voz do robô")
        os.system(f"python {script_path}")

if __name__ == "__main__":
    speak("------------ Iniciando aplicação -----------")
    command = listen_command()
    if command:
        execute_command(command)
