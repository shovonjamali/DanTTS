'''
Checks the sample rate of the audios.
Writes the output in a text.
'''

import os
import wave

def get_sample_rate(audio_file):
    try:
        with wave.open(audio_file, 'r') as wf:
            sample_rate = wf.getframerate()
        return sample_rate
    except Exception as e:
        print(f"Error reading sample rate for {audio_file}: {e}")
        return None

def check_sample_rates(input_folder, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".wav"):
                    audio_file = os.path.join(root, file)
                    sample_rate = get_sample_rate(audio_file)
                    if sample_rate:
                        f.write(f"{file}: {sample_rate} Hz\n")

if __name__ == "__main__":
    input_folder = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\wavs"
    output_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\sample_rates.txt"

    check_sample_rates(input_folder, output_file)

    print("Sample rates written to", output_file)