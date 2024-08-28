import tkinter as tk
from tkinter import messagebox
import time
import numpy as np
import sounddevice as sd

def create_impulse_sound(duration):
    t = np.linspace(0, duration, int(44100 * duration), False)
    return 0.5 * np.sin(2 * np.pi * 1000 * t) * np.exp(-t * 20)

def display_lyrics_in_rhythm():
    def_lyrics = def_lyrics_entry.get("1.0", tk.END).strip()
    if not def_lyrics:
        messagebox.showerror("Error", "Please enter DEF lyrics.")
        return

    tempo = int(tempo_entry.get())
    beat_duration = 60 / tempo / 4  # Each symbol represents a 16th note

    def_lyrics_symbols = def_lyrics.replace('|', '').split()
    impulse_sound = create_impulse_sound(beat_duration)

    current_word = ""
    for symbol in def_lyrics_symbols:
        if symbol == '@':
            lyric_display.config(text="@")
            sd.play(impulse_sound, 44100)
        elif symbol == '-':
            # Extend the display of the current word
            lyric_display.config(text=current_word)
        elif symbol == '.':
            # Clear the display for rests
            lyric_display.config(text="")
            current_word = ""
        else:
            # New word or syllable
            current_word = symbol
            lyric_display.config(text=current_word)
        
        lyric_display.update()
        time.sleep(beat_duration)
        sd.stop()

    lyric_display.config(text="End")

# Create main window
root = tk.Tk()
root.title("DEF Lyrics Rhythm Display with Sound and Sustain")

# DEF lyrics input
def_lyrics_frame = tk.Frame(root)
def_lyrics_frame.pack(padx=10, pady=10)
def_lyrics_label = tk.Label(def_lyrics_frame, text="Enter DEF lyrics (use '@' for impulse sound, '-' to sustain, '.' for rest):")
def_lyrics_label.pack()
def_lyrics_entry = tk.Text(def_lyrics_frame, width=60, height=10)
def_lyrics_entry.pack()

# Tempo input
tempo_frame = tk.Frame(root)
tempo_frame.pack(padx=10, pady=5)
tempo_label = tk.Label(tempo_frame, text="Tempo (BPM):")
tempo_label.pack(side=tk.LEFT)
tempo_entry = tk.Entry(tempo_frame, width=5)
tempo_entry.insert(0, "120")  # Default tempo
tempo_entry.pack(side=tk.LEFT)

# Lyric display
lyric_display = tk.Label(root, text="", font=("Arial", 24))
lyric_display.pack(pady=20)

# Display button
display_button = tk.Button(root, text="Display Lyrics", command=display_lyrics_in_rhythm)
display_button.pack(pady=10)

# Run the application
root.mainloop()