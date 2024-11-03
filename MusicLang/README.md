
# MusicLangPredictor MIDI Generator

This script uses the **MusicLangPredictor** to generate a new musical score based on an original MIDI file and an optional chord progression. It then saves the generated score as a MIDI file and converts it to an audio file using **FluidSynth**.

## Features

- Generate a new musical score from an existing MIDI file.
- Optionally use a chord progression to guide the AI-generated score.
- Save the generated score as a MIDI file.
- Convert the MIDI file to an audio file format.

## Requirements

- Python 3.x
- Required packages:
    - `musiclang_predict`
    - `music21`
    - `midi2audio`
    - `FluidSynth` (with appropriate soundfont)

You can install the required packages using pip:

```bash
pip install musiclang_predict music21 midi2audio
```

## Creating a Virtual Environment

It is recommended to create a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

After activating the virtual environment, install the required packages:

```bash
pip install musiclang_predict music21 midi2audio
```

## Usage

### Settings

You can customize the following settings in the script:

- `original_score_path`: Path to the original MIDI file (e.g., `'inputs/TakeFive.mid'`).
- `chord_progression`: Chord progression to guide the AI-generated score (optional).
- `nb_tokens`: Number of tokens to generate.
- `temperature`: Sampling temperature for the AI model.
- `top_p`: Top-p sampling parameter for the AI model.
- `seed`: Random seed for reproducibility.

### Initialization

The script initializes the `MusicLangPredictor` instance and retrieves the original tempo from the MIDI file.

### Generating a Score

- If a chord progression is provided, the script generates a new score based on that progression.
- If no chord progression is provided, a new score is generated based on the original MIDI score.

### Saving Output

The generated score is saved as a MIDI file in the `outputs` folder. 

### Converting MIDI to Audio

The generated MIDI file is converted to an audio file using FluidSynth and saved in the same `outputs` folder.

## Example

```python
# Example settings in the script
original_score_path = 'inputs/TakeFive.mid'
chord_progression = "CM AbM FM D7 GM"  # Example progression or leave empty ""
nb_tokens = 1024 
temperature = 0.9 
top_p = 1.0 
seed = 3668
```

## Output

After running the script, you will find the generated MIDI and audio files in the `outputs` folder:

- MIDI file: `outputs/{base_name}_{chord_progression}.mid` or `outputs/{base_name}_original.mid`
- Audio file: `outputs/{base_name}_audio.wav` or `outputs/{base_name}_original.wav`

## Notes

- Make sure to have FluidSynth installed and a soundfont available at the specified path (e.g., `~/soundfonts/FluidR3_GM.sf2`).
- Adjust the `time_signature` and other parameters as necessary based on your requirements.

## Acknowledgements

Thanks to the following projects:

- [MusicLangPredictor](https://github.com/your-repo/musiclang_predict) - for the music generation capabilities.
- [FluidSynth](https://www.fluidsynth.org/) - for MIDI to audio conversion.

