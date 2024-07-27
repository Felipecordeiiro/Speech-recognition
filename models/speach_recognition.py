import wave
import pyaudio
import librosa
import soundfile as sf
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

# Configs recording voice
FRAMES_PER_BUFFER = 200
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 16000

# Audio signal parameters
'''
- Number of channels (one or two)
- Sample width
- framerate/sample_rate (44,100 Hz)
- number of frames
- values of a frame
'''

# Convert audio from some format to mp3
'''
path_audio = "audio.ogg"

audio = AudioSegment.from_ogg(path_audio)
audio.export("output.mp3", format="mp3")
'''

input_path = "audio.ogg"

def convert_to_wav(input_path:str, output_path:str, format:str):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=format)

# Use this line if show RIFF id error
#convert_to_wav(input_path, input_path.split(".")[0]+".wav", "wav")

def getInfos(audio_path):
    obj = wave.open(audio_path, "rb")

    print("Number of chanels", obj.getnchannels())
    print("Sample width", obj.getsampwidth())
    print("Frame rate", obj.getframerate())
    print("Number of frames", obj.getnframes())
    print("Paremeters", obj.getparams())

audio_path = "audio.wav"

#getInfos(audio_path)

def plotWave(audio_path):
    audio = wave.open(audio_path)
    sample_freq = audio.getframerate()
    n_samples = audio.getnframes()
    n_channels = audio.getnchannels()
    signal_wave = audio.readframes(-1)
    t_audio = n_samples/sample_freq

    signal_array = np.frombuffer(signal_wave, dtype=np.int32) #np.int16 para sample_width = 2.
    
    if n_channels > 1:
        print(n_channels)
        signal_array = signal_array.reshape((-1, n_channels))
        signal_array = signal_array.mean(axis=1)  # Calcular a média dos canais

    times = np.linspace(0, t_audio, num=n_samples)
    plt.figure(figsize=(15,5))
    plt.plot(times, signal_array/2)
    plt.title("Audio Signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (s)")
    plt.xlim(0, t_audio)
    plt.show()

#plotWave("output.wav")

def recordingVoice():
    p = pyaudio.PyAudio()
    streaming = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )
    print("Starting recording voice")

    seconds=5
    frames=[]
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = streaming.read(FRAMES_PER_BUFFER)
        frames.append(data)
    
    print("Stoping recording voice")
    streaming.stop_stream()
    streaming.close()
    p.terminate()

    audio = wave.open("output.wav", "wb")
    audio.setnchannels(CHANNELS)
    audio.setsampwidth(p.get_sample_size(FORMAT))
    audio.setframerate(RATE)
    audio.writeframes(b"".join(frames))
    audio.close

'''
Vire a base no sentido horário / Turn the base clockwise
Vire a base no sentido anti-horário / Turn the base counterclockwise
Fecha a pinça / Close the clamp
Abra a pinça / Open the clamp
Baixe o braço / Down arm / Lower your arm
Suba o braço / Up arm / Up your arm
'''

recordingVoice() 

def converttoMp3(audio_path):
    audio = AudioSegment.from_wav(audio_path)
    audio += 6
    audio *= 2
    audio = audio.fade_in(2000)
    audio.export("output_converted.mp3", format="mp3")
    
    audio_2 = AudioSegment.from_mp3("output_converted.mp3")
    print("Conversion done!")