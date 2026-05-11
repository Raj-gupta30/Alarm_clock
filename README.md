# Alarm_clock

A simple terminal-based alarm clock built using Python and Pygame.

---

# Libraries Used

## Pygame

```python
import pygame
```

Pygame is a Python library mainly used for:

- Game development
- Sound and music handling
- Graphics and animations
- Keyboard and mouse events

After importing pygame, Python gets access to modules like:

```python
pygame.mixer
pygame.display
pygame.image
pygame.event
```

---

## Time Module

```python
import time
```

The `time` module is used for time-related operations.

In this project:

```python
time.sleep(1)
```

pauses the program for 1 second during each loop iteration.

This creates the countdown effect.

---

# ANSI Escape Codes

## Clear Screen

```python
CLEAR = "\033[2J"
```

Clears the entire terminal screen.

---

## Move Cursor to Top-Left

```python
CLEAR_AND_RETURN = "\033[H"
```

Moves the cursor to row 1, column 1.

This helps update the countdown on the same screen instead of printing new lines repeatedly.

---

# ANSI Escape Code Structure

| Part | Meaning |
|------|----------|
| `\033` | ESC character |
| `[` | Start ANSI command |
| `2J` | Clear screen command |

---

# Erase Display Commands

| Code | Meaning |
|------|----------|
| `0J` | Clear below cursor |
| `1J` | Clear above cursor |
| `2J` | Clear entire screen |

---

# Pygame Mixer

```python
pygame.mixer
```

The mixer module handles audio operations such as:

- Playing music
- Playing sound effects
- Volume control
- Audio channels

---

# Initializing the Audio System

```python
pygame.mixer.init()
```

This initializes the pygame audio engine.

Internally, pygame:

- Connects to the computer's audio device
- Creates audio buffers
- Sets sample rate
- Prepares speaker output

Default configuration:

```python
pygame.mixer.init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=512
)
```

---

# Alarm Function

```python
def alarm(seconds):
```

This function starts the countdown timer.

The `seconds` parameter represents the total countdown duration in seconds.

---

# Countdown Logic

```python
time_elapsed = seconds
```

Stores the total remaining time.

---

# Countdown Loop

```python
while time_elapsed >= 0:
```

The loop continues until the countdown reaches zero.

---

# Delay Between Each Second

```python
time.sleep(1)
```

Pauses the program for 1 second during each iteration.

Without this line, the countdown would finish instantly.

---

# Decreasing the Timer

```python
time_elapsed -= 1
```

Reduces the remaining time by 1 second after each loop.

Equivalent to:

```python
time_elapsed = time_elapsed - 1
```

---

# Converting Seconds to Minutes

```python
minute_left = time_elapsed // 60
```

Uses floor division (`//`) to calculate complete minutes.

Example:

```python
125 // 60 = 2
```

---

# Remaining Seconds

```python
second_left = time_elapsed % 60
```

Uses modulus operator (`%`) to calculate remaining seconds.

Example:

```python
125 % 60 = 5
```

---

# Displaying the Countdown

```python
print(f"{CLEAR_AND_RETURN}Alarm will be sound in : {minute_left:02d}:{second_left:02d}")
```

This prints the countdown timer in digital clock format.

Example output:

```text
00:10
00:09
00:08
```

---

# What Does `:02d` Mean?

| Part | Meaning |
|------|----------|
| `0` | Fill empty spaces with zero |
| `2` | Minimum width of 2 digits |
| `d` | Integer format |

Examples:

| Number | Output |
|------|----------|
| `1` | `01` |
| `5` | `05` |
| `10` | `10` |

---

# Loading Alarm Audio

```python
pygame.mixer.music.load("alarm_sound.mp3")
```

Loads the audio file into memory.

The audio file must be in the same directory as the Python script.

Example:

```text
project/
│
├── main.py
├── alarm_sound.mp3
└── README.md
```

---

# Playing Alarm Sound

```python
pygame.mixer.music.play()
```

Starts playing the alarm sound.

---

# Keeping the Program Alive

```python
input("Press Enter to stop alarm...")
```

Without this line, the Python program may terminate immediately after starting the music.

As a result:
- the mixer shuts down
- the sound stops instantly

`input()` keeps the program running until the user presses Enter.

---

# Taking User Input

```python
minute = int(input("How many minutes to waits: "))
second = int(input("How many seconds to waits: "))
```

Takes countdown duration from the user.

`input()` returns a string, so `int()` converts it into an integer.

---

# Total Seconds Calculation

```python
total_seconds = minute * 60 + second
```

Converts minutes and seconds into total seconds.

Example:

```text
2 minutes 30 seconds
= (2 × 60) + 30
= 150 seconds
```

---

# Starting the Alarm

```python
alarm(total_seconds)
```

Calls the `alarm()` function and starts the countdown timer.
