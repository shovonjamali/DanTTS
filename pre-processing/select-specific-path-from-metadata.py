'''
This is used to handle the LJSpeech format of the nst_wavs for Tortoise TTS or Coqui TTS.
Coqui uses csv as source whereas tortoise uses txt. Update the flag accordingly.
Keep all the tsv files under a single directory and specify that folder path here.
'''

import os
import pandas as pd
import re

# Path to the folder containing the audio files
audio_folder = "F:\\FDM Downloads\\nst_wavs-20231031T095324Z-001\\nst_wavs\\clips"

# Path to the metadata CSV file
metadata_file = "F:\\FDM Downloads\\nst_wavs-20231031T095324Z-001\\nst_wavs\\metadata.csv"

# Variable to determine the file type to create (csv or text)
file_type = "txt"  # Change this variable as needed

# Read the metadata CSV file
metadata = pd.read_csv(metadata_file, header=None, delimiter='|')

# Initialize counter for matches found
matches_found = 0

# Initialize an empty list to store matching rows
matching_rows = []

# Loop through each filename in the clips folder
for filename in os.listdir(audio_folder):
    print(f"Checking against filename: {filename}")
    # Check if the filename exists in the metadata dataframe
    if filename in metadata[1].values:
        print(f"Match found: {filename}")
        # Get the corresponding row from metadata
        row = metadata[metadata[1] == filename].iloc[0]
        # Rearrange the fields and create the new line format
        sentence = row[0].lower()  # Lowercase the sentence
        new_text = re.sub(r'\s+', ' ', sentence)  # Remove extra spaces between words
        new_line = f"wavs/{filename}|{new_text}"
        matching_rows.append(new_line)
        matches_found += 1

# Print the total number of matches found
print(f"Total matches found: {matches_found}")

# Determine the filename and extension based on the file_type variable
if file_type == "csv":
    output_file = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\tts-data\\data_nst_wavs.csv"
else:
    output_file = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\tts-data\\data_nst_wavs.txt"

# Write the filtered metadata to a new file
with open(output_file, "w", encoding="utf-8") as file:
    for line in matching_rows:
        file.write(line + "\n")

print("Filtered metadata file created successfully.")