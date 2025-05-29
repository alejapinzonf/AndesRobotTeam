from gtts import gTTS
import os
import pygame

pygame.mixer.init()

while True:
    texto = input("Ingrese el texto que desea escuchar (escriba 'salir' para terminar): ")
    if texto.lower().strip() == "salir":
        print("Programa finalizado.")
        break

    tts = gTTS(text=texto, lang='en')
    filename = "voz.mp3"
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Esperar a que termine de reproducir
    while pygame.mixer.music.get_busy():
        continue

    os.remove(filename)
