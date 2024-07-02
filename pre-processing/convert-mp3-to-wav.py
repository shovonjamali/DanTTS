import os
from pydub import AudioSegment

def convert_mp3_to_wav(input_dir, output_dir):
    """
    Convert MP3 files to WAV format.

    Args:
    - input_dir (str): Path to the directory containing MP3 files.
    - output_dir (str): Path to the directory where converted WAV files will be saved.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each file in the input directory
    for file_name in os.listdir(input_dir):
        # Check if the file is an MP3 file
        if file_name.endswith('.mp3'):
            # Construct the paths for input MP3 file and output WAV file
            mp3_path = os.path.join(input_dir, file_name)
            wav_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.wav')

            # Load the MP3 file
            audio = AudioSegment.from_mp3(mp3_path)

            # Export the audio to WAV format
            audio.export(wav_path, format='wav')
            print(f"Converted: {file_name}")

# Example usage:
input_directory = 'F:\\FDM Downloads\\cv-corpus-16.1-2023-12-06\\da\\clips'
output_directory = 'F:\\FDM Downloads\\cv-corpus-16-wavs-raw'

convert_mp3_to_wav(input_directory, output_directory)