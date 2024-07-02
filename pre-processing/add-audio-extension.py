'''
    Adds .wav extension to the audio file name. 
    This is useful for cases where metadata doesn't contain the actual file extension.
    e.g. wavs/common_voice_da_28540401|Tak. --> wavs/common_voice_da_28540401.wav|Tak.
'''
def add_wav_extension(input_file):
    # Read the lines from the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Process each line
    for i, line in enumerate(lines):
        # Split the line by '|' to extract the audio file name
        audio_file_name = line.split('|')[0].strip()

        # Check if the audio file name already has the .wav extension
        if not audio_file_name.endswith('.wav'):
            # If not, add the .wav extension to the audio file name
            audio_file_name += '.wav'

            # Update the line with the new audio file name
            new_line = audio_file_name + '|' + '|'.join(line.split('|')[1:])
            lines[i] = new_line

    # Write the updated lines back to the input file
    with open(input_file, 'w') as file:
        file.writelines(lines)


input_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\merged_file.txt"  # Replace 'your_input_file.txt' with the path to your input file
add_wav_extension(input_file)