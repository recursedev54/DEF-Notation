import tkinter as tk
from tkinter import filedialog, messagebox
from mido import MidiFile

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def convert_drums_to_def():
    midi_path = file_entry.get()
    if not midi_path:
        messagebox.showerror("Error", "Please select a MIDI file.")
        return

    try:
        midi_file = MidiFile(midi_path)
        
        drum_map = {
            36: "B",  # C1 - Bass Drum
            38: "S",  # D1 - Snare Drum
        }

        ticks_per_sixteenth = midi_file.ticks_per_beat // 4
        total_ticks = sum(msg.time for track in midi_file.tracks for msg in track)
        total_sixteenths = (total_ticks + ticks_per_sixteenth - 1) // ticks_per_sixteenth

        pattern = ['.' for _ in range(total_sixteenths)]

        current_tick = 0
        for track in midi_file.tracks:
            for msg in track:
                current_tick += msg.time
                if msg.type == 'note_on' and msg.velocity > 0:
                    if msg.note in drum_map:
                        sixteenth_index = current_tick // ticks_per_sixteenth
                        if sixteenth_index < total_sixteenths:
                            pattern[sixteenth_index] = drum_map[msg.note]

        def_notation = ''
        for i, symbol in enumerate(pattern):
            def_notation += symbol + ' '
            if (i + 1) % 16 == 0:
                def_notation += '| '

        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, def_notation.strip())

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("MIDI to DEF Converter (Basic Drum Pattern)")

# File selection
file_frame = tk.Frame(root)
file_frame.pack(padx=10, pady=10)

file_label = tk.Label(file_frame, text="Select Drum MIDI file:")
file_label.pack(side=tk.LEFT)

file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT)

file_button = tk.Button(file_frame, text="Browse", command=select_file)
file_button.pack(side=tk.LEFT)

# Convert button
convert_button = tk.Button(root, text="Convert to DEF", command=convert_drums_to_def)
convert_button.pack(pady=10)

# Result output
result_text = tk.Text(root, height=20, width=80)
result_text.pack(padx=10, pady=10)

# Run the application
root.mainloop()