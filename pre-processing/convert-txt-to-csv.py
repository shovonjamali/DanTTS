'''
    Converts txt file back to csv for any operation
'''

import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        for line in lines:
            # Write each line as a single cell in the CSV file
            writer.writerow([line.strip()])

# Replace 'output.csv' with the desired path for the CSV output file
txt_to_csv('G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\index\\output-without-wavs.txt', 'metadata.csv')
