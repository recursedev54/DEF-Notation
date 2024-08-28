import tkinter as tk
from tkinter import messagebox
import numpy as np
import sounddevice as sd

def create_sound(freq, duration, noise=False):
    t = np.linspace(0, duration, int(44100 * duration), False)
    if noise:
        return np.random.normal(0, 0.1, int(44100 * duration))
    else:
        return np.sin(2 * np.pi * freq * t) * np.exp(-t * 10)

sounds = {
    'B': create_sound(60, 0.1),  # Bass drum: low tone
    'S': create_sound(0, 0.1, noise=True),  # Snare: noise
    'H': create_sound(0, 0.05, noise=True),  # Closed hi-hat: short noise
    'O': create_sound(0, 0.1, noise=True),  # Open hi-hat: longer noise
    'C': create_sound(0, 0.2, noise=True),  # Crash: long noise
    'R': create_sound(0, 0.15, noise=True),  # Ride: medium noise
    '.': np.zeros(int(44100 * 0.05))  # Rest: silence
}

def play_def_notation():
    notation = def_entry.get()
    if not notation:
        messagebox.showerror("Error", "Please enter DEF notation.")
        return

    drum_sequence = notation.replace('|', '').split()
    tempo = int(tempo_entry.get())
    beat_duration = 60 / tempo / 4  # Divide by 4 as each symbol represents a 16th note

    full_sequence = np.zeros(int(44100 * beat_duration * len(drum_sequence)))
    
    for i, drum in enumerate(drum_sequence):
        if drum in sounds:
            start = int(i * 44100 * beat_duration)
            sound = sounds[drum]
            end = min(start + len(sound), len(full_sequence))
            full_sequence[start:end] += sound[:end-start]

    sd.play(full_sequence, 44100)
    sd.wait()

# Create main window
root = tk.Tk()
root.title("DEF Notation Player")

# DEF notation input
def_frame = tk.Frame(root)
def_frame.pack(padx=10, pady=10)
def_label = tk.Label(def_frame, text="Enter DEF notation:")
def_label.pack(side=tk.LEFT)
def_entry = tk.Entry(def_frame, width=50)
def_entry.pack(side=tk.LEFT)

# Tempo input
tempo_frame = tk.Frame(root)
tempo_frame.pack(padx=10, pady=5)
tempo_label = tk.Label(tempo_frame, text="Tempo (BPM):")
tempo_label.pack(side=tk.LEFT)
tempo_entry = tk.Entry(tempo_frame, width=5)
tempo_entry.insert(0, "120")  # Default tempo
tempo_entry.pack(side=tk.LEFT)

# Play button
play_button = tk.Button(root, text="Play", command=play_def_notation)
play_button.pack(pady=10)

# Run the application
root.mainloop()