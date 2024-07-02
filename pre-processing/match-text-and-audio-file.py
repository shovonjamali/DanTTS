'''
This matches generated metadata after segmenting audio using ffmpeg.
It ensures the number of entires present in the text data matches with the number of segmented audios.
If not shows the unmatched entries.
'''

import os

# Audio and text path
audio_folder = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Filtered-Dataset\Svenskerne_version7_Vocals"
text_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\metadata-Svenskerne_version7_Vocals_filtered.txt"

# Extract filenames from text file
def extract_filenames_from_text(text_file):
    with open(text_file, 'r') as file:
        lines = file.readlines()
        # filenames = [line.split('|')[0].strip().split('/')[-1] + ".wav" for line in lines]
        filenames = [line.split('|')[0].strip().split('/')[-1] for line in lines]
    return filenames

# Check if audio files exist
def check_audio_files_exist(audio_folder, filenames):
    missing_files = []
    for filename in filenames:
        audio_file = os.path.join(audio_folder, filename)
        if not os.path.exists(audio_file):
            missing_files.append(filename)
    return missing_files

def main():
    filenames = extract_filenames_from_text(text_file)
    missing_files = check_audio_files_exist(audio_folder, filenames)

    if missing_files:
        print("The following entries do not have corresponding audio files:")
        for filename in missing_files:
            print(filename)
    else:
        print("All entries have corresponding audio files.")

if __name__ == "__main__":
    main()
