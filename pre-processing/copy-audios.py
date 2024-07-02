'''
There are more number than audios than the text due to collecting them from different sources such as common data voice.
This copies the audio to a new directory for which it has an entry in the metadata file.
This helps to keep the number of the entries in the metadata and number of audios same.
'''

import os
import shutil

def copy_audio_files(text_file, audio_dir, new_audio_dir):
    # Create the new directory if it doesn't exist
    if not os.path.exists(new_audio_dir):
        os.makedirs(new_audio_dir)

    # Open the text file
    with open(text_file, 'r') as file:
        # Read each line in the text file
        for line in file:
            # Split the line into audio file name and text content
            audio_file_name = line.split('|')[0].split('/')[1]
            # Add the .wav extension
            # audio_file_name += '.wav'
            # Construct the full path of the source audio file
            source_audio_path = os.path.join(audio_dir, audio_file_name)
            # Construct the full path of the destination audio file
            destination_audio_path = os.path.join(new_audio_dir, audio_file_name)
            # Copy the audio file to the new directory
            shutil.copyfile(source_audio_path, destination_audio_path)

    # Print a message when the copying is done
    print("Audio files copied successfully!")

# Example usage
text_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\merged_file.txt"

audio_dir = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\wavs-full"
new_audio_dir = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\wavs"

copy_audio_files(text_file, audio_dir, new_audio_dir)