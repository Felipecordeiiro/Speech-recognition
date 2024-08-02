from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from control.http.client import send_command


def hello(request):   
    i = 0                                  
    return HttpResponse("OIi")


@api_view(['POST'])
def upload_audio(request):
    if request.method == 'POST' and request.FILES:
        audio_file = request.FILES['audio']
        # Salvar o arquivo (ajuste o caminho conforme necessário)
        with open(os.path.join('caminho/para/salvar', audio_file.name), 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        return Response({'message': 'Audio uploaded successfully!'}, status=200)
    return Response({'error': 'Invalid request'}, status=400)

