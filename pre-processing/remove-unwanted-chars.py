'''
This is used to remove unwanted chars from metadata.txt.
'''

import re

# Define the characters to filter
invalid_characters = {'é', 'í', 'ó', 'ö', 'ü', 'É', 'Í', 'Ó', 'Ö', 'Ü'}

# Initialize a counter for filtered items
filtered_count = 0

dataset_path = "F:\\MS_Thesis\\dataset\\tortoise-model-training\\metadata.txt"
filtered_dataset_path = "F:\\MS_Thesis\\dataset\\tortoise-model-training\\updated_metadata.txt"

# Open the original metadata file for reading
with open(dataset_path, 'r', encoding='utf-8') as original_file:
    # Open a new file for writing the filtered rows
    with open(filtered_dataset_path, 'w', encoding='utf-8') as updated_file:
        # Iterate through each line in the original file
        for line in original_file:
            # Split the line into audio path and text
            audio_path, text = line.strip().split('|')
            # Check if the text contains any invalid characters
            if any(char in invalid_characters for char in text):
                # Increment the counter for filtered items
                filtered_count += 1
            else:
                # Write the line to the updated file
                updated_file.write(f"{audio_path}|{text}\n")

# Print the number of filtered items
print(f"Created filtered metadata. Filtered count: {filtered_count}")