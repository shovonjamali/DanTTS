'''
This is used to create a transcript file from train and validation set.
This transcript then can be used by the bpe tokenizer toolset to create custom tokenizer.
'''

transcriptions = ""
dataset_path = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset"
transcription_path = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Combined-Dataset\transcription.txt"

for stage in ["train", "val"]:
    with open(f'{dataset_path}/{stage}.txt') as f:
        for line in f.readlines():
            transcriptions += ' ' + line.split("|")[1].strip()

with open(transcription_path, "w") as f:
  f.write(transcriptions.strip())