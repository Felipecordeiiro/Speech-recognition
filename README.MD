To run Speech Recognition in real-time using vosk, follow the steps:
- 1. Download pre-trained model vosk specialized for portuguese/BR in site: "https://alphacephei.com/vosk/models"
- 2. Move the file of pre-trained model to root directory
- 3. run the ```model.py file```

To run Speech Recognition since the start S.O, do you need follow the steps:
### Linux 
- 1. Create the service file `voice_listener.service`
```
[Unit]
Description=Voice Listener Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /caminho/para/seu/main.py
Restart=always
User=seu_usuario
Group=seu_grupo

[Install]
WantedBy=multi-user.target
```
- 2. To hability service:
```
sudo systemctl enable voice_listener.service
sudo systemctl start voice_listener.service
```
### Windows
- 1. Create a file shortcut "background_listener.py"
- 2. Open Executer from windows with "Win+R" and digit:
```
shell:startup
```
- 3. Move "background_listener.py" to initialize folder from windows