'''
This removes the mismatched entries found in the result from match-text-and-audio-file.py.
This takes the entries as an input from a text file and delete the corresponding audio files.
'''

# Read the content of the first text file
remove_entries_file_path = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\remove-entries.txt"
metadata_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\metadata-20141_M094_Vocals_filtered.txt"

with open(remove_entries_file_path, "r") as file:
    first_content = file.readlines()

# Read the content of the second text file
with open(metadata_file, "r") as file:
    second_content = file.readlines()

# Extract filenames from the first text file
filenames_to_remove = [line.strip()[:-4] for line in first_content]

# Filter out matching entries from the second text file
filtered_content = [line for line in second_content if not any(filename in line for filename in filenames_to_remove)]

# Write the filtered content back to the second text file
with open(metadata_file, "w") as file:
    file.writelines(filtered_content)