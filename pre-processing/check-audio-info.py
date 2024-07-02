'''
Checks the sample rate and channel of the audios.
It makes sure the processed audios have specific sample rate and channel.
Writes the output in a text file.
'''

import os
import librosa

def get_audio_info(audio_folder, output_file):
    with open(output_file, 'w') as f:
        f.write("File Name, Sample Rate, Channels\n")
        for file_name in os.listdir(audio_folder):
            if file_name.endswith('.wav'):
                file_path = os.path.join(audio_folder, file_name)
                try:
                    y, sr = librosa.load(file_path, sr=None, mono=False)
                    channels = y.shape[0] if len(y.shape) > 1 else 1
                    f.write(f"{file_name}, {sr}, {channels}\n")
                except Exception as e:
                    print(f"Error processing {file_name}: {e}")

# Usage
audio_folder = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\wavs"
output_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\audio_info.txt"

get_audio_info(audio_folder, output_file)

print("Audio info written to", output_file)