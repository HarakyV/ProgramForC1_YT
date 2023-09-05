import tkinter
from tkinter import *
import random
import time
import os
import pygame
import keyboard
import threading  # Import the threading module

listOfSong = [r"Funny_Musics\song1.mp3", r"Funny_Musics\song2.mp3", r"Funny_Musics\song3.mp3", r"Funny_Musics\song4.mp3", r"Funny_Musics\song5.mp3", r"Funny_Musics\song6.mp3", r"Funny_Musics\song7.mp3", r"Funny_Musics\song8.mp3", r"Funny_Musics\song9.mp3", r"Funny_Musics\song10.mp3", r"Funny_Musics\song11.mp3", r"Funny_Musics\song12.mp3", r"Funny_Musics\song13.mp3", r"Funny_Musics\song14.mp3", r"Funny_Musics\song15.mp3", ]

buttonToClick = "="

print("Starting the program....")

def play_background_music():
    mp3_file = random.choice(listOfSong)
    print("Choose song number: " + mp3_file)
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play(1)

root = Tk()

def GUI():
    root.iconbitmap("icon.ico")
    root.geometry("450x450")
    root.title("Random MP3 Funny Musics Player - By Hcracky")

    text1 = Label(root, text="Program is Active!")
    text1.pack(pady=5)

    text2 = Label(root, text="Click" + buttonToClick + "to play music")
    text2.pack(pady=5)


    text3 = Label(root,text="15 Random mp3s in Funny_Musics folder!")
    text3.pack(pady=5)



    def play_music_thread():  # Define a function to run play_background_music in a thread
        while True:
            if keyboard.is_pressed(buttonToClick):
                if not last_key_state:
                    play_background_music()
                    last_key_state = True
            else:
                last_key_state = False
            time.sleep(0.1)

    # Start the play_music_thread in a separate thread
    threading.Thread(target=play_music_thread, daemon=True).start()

    root.mainloop()

GUI()
