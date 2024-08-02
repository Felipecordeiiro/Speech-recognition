import swift
import roboticstoolbox as rtb
import numpy as np
import time
import threading
import queue
import speech_simulation as ss

env = swift.Swift()
env.launch(realtime=True)

robot = rtb.models.wx250s()
robot.q = robot.qr

env.add(robot)

sutil = False

dt = 0.1

brush_duration = 5 # Tempo da escovação em segundos
start_time = 0 

def execute_command(command, sutil):
    if command == "descansar":
        robot.q = robot.qr
        
    elif command == "frente":
        if not sutil:
            robot.q[1] += 0.1
        else:
            robot.q[1] += 0.05

    elif command == "trás":
        if not sutil:
            robot.q[1] -= 0.1
        else:
            robot.q[1] -= 0.05

    elif command == "cima":
        if not sutil:
            robot.q[2] += 0.1
        else:
            robot.q[2] += 0.05

    elif command == "baixo":
        if not sutil:
            robot.q[2] -= 0.1
        else:
            robot.q[2] -= 0.05

    elif command == "direita":
        if not sutil:
            robot.q[0] -= np.pi / 12 # Vira 15 graus para a direita
        else:
            robot.q[0] -= np.pi / 36 # Vira 5 graus para a direita

    elif command == "esquerda":
        if not sutil:
            robot.q[0] += np.pi / 12 # Vira 15 graus para a esquerda
        else:
            robot.q[0] += np.pi / 36 # Vira 5 graus para a esquerda

    elif command == "abrir garra":
        robot.q[7] += 0.1
        robot.q[8] -= 0.1

    elif command == "fechar garra":
        robot.q[7] -= 0.1
        robot.q[8] += 0.1

    elif command == "escovar":
        if not sutil:
            sutil = True
            temp = True
        start_time = time.time()
        while time.time() - start_time < brush_duration:
            execute_command("direita", sutil)
            env.step(dt)
            execute_command("esquerda", sutil)
            env.step(dt)

        if temp: # Se tiver sido colocado no modo sutil apenas temporariamente
            sutil = False 

    else:
        print("Comando invalido")


def process_commands(command_queue, sutil):
    while True:
        if not command_queue.empty():
            command = command_queue.get()
            if "cima" in command:
                execute_command("cima", sutil)
            elif "baixo" in command:
                execute_command("baixo", sutil)
            elif "frente" in command:
                execute_command("frente", sutil)
            elif "trás" in command:
                execute_command("trás", sutil)
            elif "esquerda" in command:
                execute_command("esquerda", sutil)
            elif "direita" in command:
                execute_command("direita", sutil)
            elif "abrir" in command:
                execute_command("abrir garra", sutil)
            elif "fechar" in command:
                execute_command("fechar garra", sutil)
            elif "escovar" in command:
                execute_command("escovar", sutil)
            elif "sutil" in command:
                sutil = not sutil
            elif "parar" in command:
                break
            else:
                pass

            env.step(dt)
        

    env.hold()

#def main():
#    while True:
#        command = input("Comando: ").strip().lower()
#        if command == "sair":
#            break
#        execute_command(command)
#        print(f"Angulos das juntas: {robot.q}")
#        
#        env.step(dt)
#
#    env.hold()

if __name__ == "__main__":
    command_queue = queue.Queue()

    # Create threads for speech recognition and command processing
    speech_thread = threading.Thread(target=ss.capture_speech, args=(command_queue,))
    command_thread = threading.Thread(target=process_commands, args=(command_queue, sutil))

    # Start the threads
    speech_thread.start()
    command_thread.start()

    # Join the threads to the main thread
    speech_thread.join()
    command_thread.join()
