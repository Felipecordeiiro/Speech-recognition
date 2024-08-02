from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import vosk
import colorama
import json
from colorama import Fore, Back, Style
from control.http.client import send_command
from comandos import command_dict
colorama.init()


def hello(request):   
    i = 0                                  
    return HttpResponse("Hello World!")


# @api_view(['POST'])
# def upload_audio(request):
#     if request.method == 'POST' and request.FILES:
#         audio_file = request.FILES['audio']
#         # Configure o modelo Vosk (baixe um modelo adequado para seu idioma)
#         new_model = vosk.Model("models/vosk-model-small-pt-0.3")
#         rec = vosk.KaldiRecognizer(new_model, 16000)
#         data = ...

#         # ler chunck
#         if rec.AcceptWaveform(data):
#             result = json.loads(rec.Result())
#             print(f"Você disse: {result}")
#             ## Comandos
#             if "esquerda" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['esquerda'])
#             elif "direita" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['direita'])
#             elif "baixo" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['baixo'])
#             elif "cima" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['cima'])
#             elif "abrir garra" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['abrir garra'])
#             elif "fechar garra" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['fechar garra'])
#             elif "escovação" in result["text"]:
#                 print(Fore.GREEN + f'SENDING COMMAND "{result["text"]}" TO ESP8266: ' + Style.RESET_ALL)
#                 send_command(command_dict['escovação'])

#         return Response({'message': 'Audio uploaded successfully!'}, status=200)
#     return Response({'error': 'Invalid request'}, status=400)

