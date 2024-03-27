import pyautogui
import win32api
import time
import pygame
import os

pygame.mixer.init()

# TTS from: https://elevenlabs.io/

STRATAGEMS = [
    {
        'title': 'eagle_airstrike',
        'keybind': '0x49',
        'sequence': ['up', 'right', 'down', 'right'],
        'sound_dir': '\\assets\\Eagle_Airstrike.mp3'
    },
    {
        'title': 'orbital_precision_strike',
        'keybind': '0x4f',
        'sequence': ['right', 'right', 'up'],
        'sound_dir': '\\assets\\Orbital_Precision_Strike.mp3'
    },
    {
        'title': 'reinforce',
        'keybind': '0x50',
        'sequence': ['up', 'down', 'right', 'left', 'up'],
        'sound_dir': '\\assets\\Reinforce.mp3'
    }
]


while True:
    for item in STRATAGEMS:
        if win32api.GetKeyState(int(item['keybind'], 16)) in (-127, -128):
            print(f"LAUNCHING {item['title']}")
            pygame.mixer.music.load(os.getcwd() + item['sound_dir'])
            pygame.mixer.music.play()
            for arrow_key in item['sequence']:
                pyautogui.press(arrow_key)
                time.sleep(0.01)