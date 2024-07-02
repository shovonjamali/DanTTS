'''
This is used to handle the LJSpeech format of the Mozilla Common Dataset for Tortoise TTs.
Keep all the tsv files under a single directory and specify that folder path here.
'''

import csv
from pathlib import Path

def extract_unique_path_sentence(tsv_file, unique_paths):
    path_sentence_data = []
    with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            path = row['path']
            if path not in unique_paths:  # Check if the path is unique
                sentence = row['sentence']
                path_sentence_data.append((path, sentence))
                unique_paths.add(path)  # Add the path to the set of unique paths
    return path_sentence_data

def clean_sentence(sentence):
    # Remove unwanted characters from the sentence
    cleaned_sentence = sentence.replace('»', '').replace('«', '').replace('–', '').replace('\'', '')
    # Remove leading and trailing whitespace
    cleaned_sentence = cleaned_sentence.strip()
    return cleaned_sentence

def write_to_text_file(data, output_file):
    with open(output_file, 'a', encoding='utf-8') as file:
        for path, sentence in data:
            # Remove unwanted characters at the beginning of the sentence
            # cleaned_sentence = sentence.lstrip('»«–\'')
            # Remove leading whitespace
            # cleaned_sentence = cleaned_sentence.strip()
            cleaned_sentence = clean_sentence(sentence)
            file.write(f"wavs/{path}|{cleaned_sentence}\n")  # Writing in the specified format

# Directory containing TSV files
tsv_folder = Path(r'G:\ML_Practice\amlfall23\Thesis-pre-processing\tts-data')

# Output text file
output_file = Path(r'G:\ML_Practice\amlfall23\Thesis-pre-processing\tts-data\data.txt')

# Set to store unique paths
unique_paths = set()

# Process each TSV file
for tsv_file in tsv_folder.glob('*.tsv'):
    # Extract unique 'path' and 'sentence' pairs
    path_sentence_data = extract_unique_path_sentence(tsv_file, unique_paths)
    
    # Write to text file
    write_to_text_file(path_sentence_data, output_file)

print("Extraction completed and written to data.txt")