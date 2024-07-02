'''
It cleans the metadata which contains year and some special symbols like ...
It also removes the entires that has comma at the end.
The reason behind removing those entries is because some of the audios are noisy.
'''

import os
import re

# Function to check if the content contains years
def contains_year(content):
    # Regular expression to match four-digit numbers
    year_pattern = r'\b\d{4}\b'
    # Search for years in the content
    if re.search(year_pattern, content):
        return True
    return False

# Function to read the file, filter entries, and write to a new file
def filter_and_write_entries(input_file, output_file, log_file, audio_folder):
    removed_entries = []

    with open(input_file, 'r') as file:
        with open(output_file, 'w') as filtered_file:
            for line in file:
                entry = line.strip()
                audio_name = entry.split('|')[0].split('/')[1]
                content = entry.split('|')[1]
                # if any(char.isdigit() for char in content) or '...' in content or not content.endswith('.'):
                if '...' in content or content.endswith(',') or contains_year(content) or 'Hurra!' in content:
                    removed_entries.append(entry)
                    # audio_file = os.path.join(audio_folder, audio_name + '.wav')
                    audio_file = os.path.join(audio_folder, audio_name)
                    
                    if os.path.exists(audio_file):
                        os.remove(audio_file)
                else:
                    filtered_file.write(entry + '\n')

    # Write removed entries to the log file
    with open(log_file, 'w') as log:
        log.write(f"Removed entries: {len(removed_entries)}\n")
        for entry in removed_entries:
            log.write(entry + '\n')

# Main function
def main():
    # Input and output file paths
    input_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\metadata-20131_M061_Vocals.txt"
    output_file = input_file.replace('.txt', '_filtered.txt')
    log_file = input_file.replace('.txt', '_removed_log.txt')

    # Folder containing audio files
    audio_folder = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Filtered-Audio-Dataset\20131_M061_Vocals"

    # Filter entries and write to a new file
    filter_and_write_entries(input_file, output_file, log_file, audio_folder)

if __name__ == "__main__":
    main()