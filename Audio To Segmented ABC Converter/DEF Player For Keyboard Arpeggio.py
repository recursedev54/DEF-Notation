import tkinter as tk
from tkinter import messagebox
import numpy as np
import sounddevice as sd

def create_key_sound(freq, duration):
    t = np.linspace(0, duration, int(44100 * duration), False)
    return 0.3 * np.sin(2 * np.pi * freq * t)

def note_to_freq(note):
    notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    octave = int(note[-1])
    note_name = note[:-1]
    semitones = notes[note_name]
    return 440 * (2 ** ((semitones - 9) / 12 + (octave - 4)))

def play_keyboard_def():
    def_notation = def_entry.get()
    if not def_notation:
        messagebox.showerror("Error", "Please enter DEF notation.")
        return

    tempo = int(tempo_entry.get())
    beat_duration = 60 / tempo / 4  # Each symbol represents a 16th note

    pattern = def_notation.replace('|', '').split()
    full_sequence = np.zeros(int(44100 * beat_duration * len(pattern)))
    
    current_note = None
    current_duration = 0
    
    for i, symbol in enumerate(pattern):
        if symbol != '-' and symbol != '.':
            if current_note:
                freq = note_to_freq(current_note)
                sound = create_key_sound(freq, beat_duration * current_duration)
                start = int((i - current_duration) * 44100 * beat_duration)
                end = start + len(sound)
                if end > len(full_sequence):
                    end = len(full_sequence)
                    sound = sound[:end-start]
                full_sequence[start:end] += sound
            current_note = symbol
            current_duration = 1
        elif symbol == '-':
            current_duration += 1
        elif symbol == '.':
            if current_note:
                freq = note_to_freq(current_note)
                sound = create_key_sound(freq, beat_duration * current_duration)
                start = int((i - current_duration) * 44100 * beat_duration)
                end = start + len(sound)
                if end > len(full_sequence):
                    end = len(full_sequence)
                    sound = sound[:end-start]
                full_sequence[start:end] += sound
                current_note = None
                current_duration = 0

    # Play the last note if there is one
    if current_note:
        freq = note_to_freq(current_note)
        sound = create_key_sound(freq, beat_duration * current_duration)
        start = int((len(pattern) - current_duration) * 44100 * beat_duration)
        end = start + len(sound)
        if end > len(full_sequence):
            end = len(full_sequence)
            sound = sound[:end-start]
        full_sequence[start:end] += sound

    sd.play(full_sequence, 44100)
    sd.wait()

# Create main window
root = tk.Tk()
root.title("DEF Player for Keyboard Arpeggio")

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
play_button = tk.Button(root, text="Play DEF", command=play_keyboard_def)
play_button.pack(pady=10)

# Run the application
root.mainloop()