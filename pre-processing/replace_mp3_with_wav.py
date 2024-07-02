'''
Mozilla common dataset provides all the audio file as .mp3. While creating the dataset from the original tsvs, 
the file path was kept as .mp3, which needs to be changed. 
'''

def modify_data_file(file_path):
    modified_entries = []

    # Read data from the original file and modify entries
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            path, sentence = line.strip().split('|')
            modified_path = path.replace('.mp3', '.wav')
            modified_entries.append(f"{modified_path}|{sentence}\n")

    # Write modified entries to a new file
    new_file_path = file_path.replace('.txt', '_modified.txt')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.writelines(modified_entries)

    print(f"New file created: {new_file_path}")

# Path to the data.txt file
data_file_path = 'G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\tts-data\\data.txt'

# Modify the data.txt file and create a new file with .wav entries
modify_data_file(data_file_path)