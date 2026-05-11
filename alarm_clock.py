import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = seconds

    print(CLEAR)

    while time_elapsed  >= 0:
        time.sleep(1)

        time_elapsed -= 1

        minute_left = time_elapsed // 60
        second_left = time_elapsed % 60

        print(f"{CLEAR_AND_RETURN}Alarm will be sound in : {minute_left:02d}:{second_left:02d}")

    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")
    pygame.mixer.music.play()
    input("Press Enter to stop alarm...")

minute = int(input("How many minutes to waits: "))
second = int(input("How many seconds to waits: "))
total_seconds = minute*60 + second

alarm(total_seconds)