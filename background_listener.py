import subprocess

def start_background_listener():
    subprocess.Popen(['python', 'C:\Users\..\speach-recognition\main.py']) # Verificar path

if __name__ == "__main__":
    start_background_listener()
    # Seu código principal aqui, se necessário