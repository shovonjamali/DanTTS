'''
Split main data source to train, test, and validation set.
'''

import random
import os

def split_dataset(input_file, train_file, val_file, test_file=None, test_ratio=0.0, val_ratio=0.15):
    """
    Split the main data source into train, test, and validation sets.

    Args:
    - input_file (str): Path to the input file containing the data.
    - train_file (str): Path to save the train file.
    - val_file (str): Path to save the validation file.
    - test_file (str): Path to save the test file (optional, default=None).
    - test_ratio (float): Ratio of data to allocate for the test set (default=0.1).
    - val_ratio (float): Ratio of data to allocate for the validation set (default=0.1).
    """
    # Read the lines from the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Shuffle the lines randomly
    random.shuffle(lines)

    # Calculate the number of lines for each set
    total_lines = len(lines)
    train_size = int(total_lines * (1 - test_ratio - val_ratio))
    val_size = int(total_lines * val_ratio)

    # Split the lines into training, test, and validation sets
    train_lines = lines[:train_size]
    val_lines = lines[train_size:train_size + val_size]
    test_lines = lines[train_size + val_size:] if test_file else None

    # Write the lines to the corresponding output files
    with open(train_file, 'w') as f:
        f.writelines(train_lines)

    with open(val_file, 'w') as f:
        f.writelines(val_lines)

    if test_file:
        with open(test_file, 'w') as f:
            f.writelines(test_lines)

    print("Splitting completed!")

# Define the paths for input and output files
input_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\metadata.txt"

train_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\train.txt"
test_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\test.txt"
val_file = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\val.txt"

# Define whether to generate test file or not
generate_test = False  # Set this to True if you want to generate test file, False otherwise

# Call the function to split the dataset
if generate_test:
    split_dataset(input_file, train_file, val_file, test_file=test_file)
else:
    split_dataset(input_file, train_file, val_file)


# simple alternate

# import random

# random.shuffle(all_transcribed_audio_samples)
# num_train_samples = int(len(all_transcribed_audio_samples) * 0.85)

# train_dataset = transcribed_audio_samples[:num_train_samples]
# val_dataset = transcribed_audio_samples[num_train_samples:]