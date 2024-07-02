import os
import librosa
import soundfile as sf

input_path = r"F:\MS_Thesis\dataset\data-segmented\20131_M061_Vocals"               
output_path = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Processed-Dataset\20131_M061_Vocals"

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(input_path):
    if filename.endswith(".wav"):
        # Load the .wav file
        filepath = os.path.join(input_path, filename)
        y, sr = librosa.load(filepath, sr=22050)

        # Trim silence
        # trimmed_audio, _ = librosa.effects.trim(y, top_db=20)

        # Normalize audio
        # normalized_audio = librosa.util.normalize(trimmed_audio)

        # Save processed .wav file to the output folder
        output_filepath = os.path.join(output_path, filename)
        # sf.write(output_filepath, normalized_audio, sr, subtype='PCM_16')
        sf.write(output_filepath, y, sr, subtype='PCM_16')

print("All .wav files have been preprocessed and saved to the output folder.")