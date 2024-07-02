'''
    This can be used to seperate audio and corresponding text files if they are contained within a same directory.
    For instance RMHL20130002 dataset.
'''

import os
import shutil

def copy_files_to_folders(folder_path):
    # Create directories to store .wav and text files
    wav_folder = os.path.join(folder_path, 'wavs')
    text_folder = os.path.join(folder_path, 'texts')
    os.makedirs(wav_folder, exist_ok=True)
    os.makedirs(text_folder, exist_ok=True)

    # Copy .wav files to wavs folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):
            src_path = os.path.join(folder_path, file_name)
            dst_path = os.path.join(wav_folder, file_name)
            shutil.copy(src_path, dst_path)
            print(f"Copied {file_name} to wavs folder.")

    # Copy text files to texts folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            src_path = os.path.join(folder_path, file_name)
            dst_path = os.path.join(text_folder, file_name)
            shutil.copy(src_path, dst_path)
            print(f"Copied {file_name} to texts folder.")

# Replace 'RMHL20130002' with the path to your folder
folder_path = 'RMHL20130002'
copy_files_to_folders(folder_path)