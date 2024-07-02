'''
    This handles a very specific case for a particular dataset RMHL20130002.
    This set has a directory containing all the audio and corresponding transcript under a single folder.
    From there a LJSpeech dataset is created. 
'''

import os
import re

def ensure_sentence_punctuation(sentence):
    # Define a regular expression pattern to match the end of a sentence
    sentence_end_pattern = r'[\.\?!]\s*$'
    # If the sentence doesn't end with a punctuation mark, add a period at the end
    if not re.search(sentence_end_pattern, sentence):
        sentence += '.'
    return sentence

def create_index_file(folder_path):
    # Create a directory to store the index file
    if not os.path.exists('index'):
        os.makedirs('index')

    # Open the output file to write index entries
    #with open('index/output.txt', 'w', encoding='utf-8') as output_file:
    with open('index/metadata.csv', 'w', encoding='utf-8') as output_file:
        # Iterate through each file in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):  # Process only text files
                text_file_path = os.path.join(folder_path, file_name)
                # Extract the base name (without extension) to match with audio file
                base_name = os.path.splitext(file_name)[0]
                audio_file_name = base_name + '.wav'
                audio_file_path = os.path.join(folder_path, audio_file_name)
                print(f"Processing file {file_name}")
                # Read the content from text file
                with open(text_file_path, 'r', encoding='utf-8') as text_file:
                    text_content = text_file.read().strip()
                    # Split text_content into sentences
                    sentences = text_content.split('.')
                    # Ensure each sentence ends with a punctuation mark
                    sentences = [ensure_sentence_punctuation(sentence.strip()) for sentence in sentences]
                    # Reconstruct text_content with modified sentences
                    text_content = '. '.join(sentences)
                # Write the index entry to the output file
                #index_entry = f'wavs/{audio_file_name}|{text_content}\n'
                index_entry = f'{audio_file_name}|{text_content}\n'
                output_file.write(index_entry)

    print("Index creation completed!")

# Replace 'RMHL20130002' with the path to your folder
folder_path = 'RMHL20130002'
create_index_file(folder_path)