"""
This script uses the MusicLangPredictor to generate a new musical score based on an original MIDI file and an optional chord progression.
It then saves the generated score as a MIDI file and converts it to an audio file using FluidSynth.

Settings:
- original_score_path: Path to the original MIDI file.
- chord_progression: Chord progression to guide the AI-generated score (optional).
- nb_tokens: Number of tokens to generate.
- temperature: Sampling temperature for the AI model.
- top_p: Top-p sampling parameter for the AI model.
- seed: Random seed for reproducibility.

Initialization:
- base_name: Base name of the original MIDI file.
- ml: Instance of the MusicLangPredictor.

Retrieve Original Tempo:
- original_score: Parsed original score using music21.
- tempo: Tempo of the original score.

Generate Score with AI:
- If a chord progression is provided, generate a new score based on the progression.
- If no chord progression is provided, generate a new score based on the original score.

Save Output MIDI:
- Save the generated score as a MIDI file in the 'outputs' folder.

Convert MIDI to Audio:
- Convert the generated MIDI file to an audio file using FluidSynth.
"""


import os
from musiclang_predict import MusicLangPredictor
from music21 import converter
import os
from midi2audio import FluidSynth


os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ['CURL_CA_BUNDLE'] = ''

# ---- Settings ----
original_score_path = 'inputs/TakeFive.mid'
chord_progression = "CM AbM FM D7 GM"  # Example progression or leave empty ""
nb_tokens = 1024 
temperature = 0.9 
top_p = 1.0 
seed = 3668

# ---- Initialization ----
base_name = os.path.splitext(os.path.basename(original_score_path))[0]
ml = MusicLangPredictor('musiclang/musiclang-v2')

# ---- Retrieve Original Tempo ----
original_score = converter.parse(original_score_path)
tempo = original_score.metronomeMarkBoundaries()[0][2].number

# ---- Generate Score with AI ----
if chord_progression:
    score = ml.predict_chords(
        chord_progression,
        score=original_score_path,
        time_signature=(5, 4),
        nb_tokens=nb_tokens,
        prompt_chord_range=(0, 10),
        temperature=temperature,
        topp=top_p,
        rng_seed=seed
    )
    output_name = f"{base_name}_{chord_progression.replace(' ', '_')}.mid"
else:
    score = ml.predict_chords(
        score=original_score_path,
        time_signature=(4, 4),
        nb_tokens=nb_tokens,
        temperature=temperature,
        topp=top_p,
        rng_seed=seed
    )
    output_name = f"{base_name}_original.mid"

# ---- Save Output MIDI ----
output_folder = './outputs'
os.makedirs(output_folder, exist_ok=True)
midi_path = os.path.join(output_folder, output_name)
score.to_midi(midi_path, tempo=tempo, time_signature=(5, 4))
print(f"Generated MIDI saved at: {midi_path}")

# ---- Convert MIDI to Audio ----
fs = FluidSynth("~/soundfonts/FluidR3_GM.sf2")
audio_output_name = f"{base_name}_{'audio' if chord_progression else 'original'}.wav"
audio_output_path = os.path.join(output_folder, audio_output_name)

# Convert the MIDI file to audio
fs.midi_to_audio(midi_path, audio_output_path)
print(f"Generated audio saved at: {audio_output_path}")
