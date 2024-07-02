'''
This merges the metadata from different segmented audios. 
'''

import os

def merge_text_files(input_dir, output_file):
    # List all files in the input directory
    files = os.listdir(input_dir)

    # Open the output file in append mode
    with open(output_file, 'a') as output:
        # Iterate over each file in the directory
        for file_name in files:
            # Check if the file is a text file
            if file_name.endswith('.txt'):
                file_path = os.path.join(input_dir, file_name)
                # Open each text file and append its contents to the output file
                with open(file_path, 'r') as input_file:
                    output.write(input_file.read())
                    # Add a newline character to separate the contents of different files
                    output.write('\n')
    
    # Print a message when the task is done
    print("Text files merged successfully!")

input_dir = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Filtered-Text"
output_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\merged_file.txt"
merge_text_files(input_dir, output_file)