import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random
#from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator

#pip install deep-translator

words = {
    "fácil": ["gato", "cachorro", "maçã", "leite", "sol"],
    "médio": ["casa", "escola", "amigo", "janela", "amarelo"],
    "difícil": ["tecnologia", "universidade", "informação", "pronúncia", "imaginação"]
}

level = input("Escolha a sua dificuldade: fácil, médio our difícil?")

duration = 5  # segundos de gravação
sample_rate = 44100

RNG = words[level]
print(RNG)

print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

recognizer = sr.Recognizer()
wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse:", text)
    translated = MyMemoryTranslator(source='pt-BR', target='en-US').translate(text)
    print("🌍 Tradução para o", 'en-US' + ":", translated)
except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
    print("A fala não pôde ser reconhecida.")
except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
    print(f"Service error: {e}")

if recording == RNG:
    print("Você Acertou!")
else:
    print("Você Errour :(")