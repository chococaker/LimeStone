import os
import numpy as np
import wave

NUM_VARIATIONS = 1
MIN_NOTE = 54 # F#3
MAX_NOTE = 78 # F#5
NOISE_LEVEL = 0.02
INPUT_FILE_NAME = "./noteblock_tone_base/F♯.wav"
OUTPUT_DIR_NAME = "../note"

NOTE_NAMES = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, INPUT_FILE_NAME)
OUTPUT_DIR = os.path.join(BASE_DIR, OUTPUT_DIR_NAME)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def midi_to_note_name(midi_number):
    note = NOTE_NAMES[midi_number % 12]
    octave = midi_number // 12 - 1
    return f"{note}{octave}"

def read_wav(filename):
    with wave.open(filename, 'rb') as wf:
        n_channels = wf.getnchannels()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        audio = np.frombuffer(wf.readframes(n_frames), dtype=np.int16)
        if n_channels > 1:
            audio = audio.reshape(-1, n_channels).mean(axis=1).astype(np.int16)
    return audio, framerate

def write_wav(filename, audio, framerate):
    audio = audio.astype(np.int16)
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(framerate)
        wf.writeframes(audio.tobytes())

def pitch_shift(audio, semitones):
    factor = 2 ** (semitones / 12.0)
    new_length = int(len(audio) / factor)
    return np.interp(np.linspace(0, len(audio), new_length), np.arange(len(audio)), audio)

audio, framerate = read_wav(INPUT_FILE)

for target_note in range(MIN_NOTE, MAX_NOTE + 1):
    semitones = target_note - MIN_NOTE

    new_audio = pitch_shift(audio, semitones)

    new_audio = new_audio * (32767 / np.max(np.abs(new_audio)))

    note_name = midi_to_note_name(target_note)
    output_file = os.path.join(OUTPUT_DIR, f"{note_name}.wav")

    counter = 1
    while os.path.exists(output_file):
        output_file = os.path.join(OUTPUT_DIR, f"{note_name}_{counter}.wav")
        counter += 1

    write_wav(output_file, new_audio, framerate)
    print(f"Saved {output_file}")
    