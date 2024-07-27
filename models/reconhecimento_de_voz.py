import speech_recognition as sr
import subprocess

def listen_for_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print("Aguardando comando...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {command}")

            if "iniciar aplicação" in command.lower():
                print("Iniciando a aplicação...")
                subprocess.Popen(['python', 'C:\Users\loqui\Desktop\speach_recognition\start_application.py'])

        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Não foi possível obter resultados do serviço de reconhecimento de voz.")

if __name__ == "__main__":
    listen_for_command()