import tkinter as tk
from tkinter import messagebox
import numpy as np
import sounddevice as sd

def create_bass_sound(freq, duration):
    t = np.linspace(0, duration, int(44100 * duration), False)
    return 0.5 * np.sin(2 * np.pi * freq * t)  # Removed the decay envelope

def note_to_freq(note):
    notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    octave = int(note[-1])
    note_name = note[:-1]
    semitones = notes[note_name]
    return 440 * (2 ** ((semitones - 9) / 12 + (octave - 4)))

def play_bass_def():
    def_notation = def_entry.get()
    if not def_notation:
        messagebox.showerror("Error", "Please enter DEF notation.")
        return

    tempo = int(tempo_entry.get())
    beat_duration = 60 / tempo / 4  # Each symbol represents a 16th note

    pattern = def_notation.replace('|', '').split()
    full_sequence = np.array([])
    
    current_freq = None
    current_duration = 0
    
    for symbol in pattern:
        if symbol not in ['-', '.']:
            if current_freq is not None:
                sound = create_bass_sound(current_freq, current_duration * beat_duration)
                full_sequence = np.concatenate((full_sequence, sound))
            current_freq = note_to_freq(symbol)
            current_duration = 1
        elif symbol == '-':
            current_duration += 1
        elif symbol == '.':
            if current_freq is not None:
                sound = create_bass_sound(current_freq, current_duration * beat_duration)
                full_sequence = np.concatenate((full_sequence, sound))
            full_sequence = np.concatenate((full_sequence, np.zeros(int(44100 * beat_duration))))
            current_freq = None
            current_duration = 0

    # Add the last note if there is one
    if current_freq is not None:
        sound = create_bass_sound(current_freq, current_duration * beat_duration)
        full_sequence = np.concatenate((full_sequence, sound))

    sd.play(full_sequence, 44100)
    sd.wait()

# Create main window
root = tk.Tk()
root.title("DEF Player for Bass")

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
play_button = tk.Button(root, text="Play DEF", command=play_bass_def)
play_button.pack(pady=10)

# Run the application
root.mainloop()