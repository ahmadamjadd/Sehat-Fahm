from gtts import gTTS
import pygame
import time

text = "آپ کی رپورٹ بالکل نارمل ہے، مبارک ہو!"

tts = gTTS(text=text, lang='ur', slow=False)
tts.save("urdu_output.mp3")

pygame.mixer.init()
pygame.mixer.music.load("urdu_output.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.5)
