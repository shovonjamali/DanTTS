'''
    Duplicates LJSpeech formatted metadata for augmentation. 
    Required for Coqui tts.
'''

# Input and output file paths
input_file = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\index\\metadata.csv"
output_file = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\index\\modified_metadata.csv"

# Open the input file for reading and the output file for writing
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    # Process each line in the input file
    for line in infile:
        # Split the line by the "|" delimiter
        parts = line.strip().split("|")
        if len(parts) >= 2:
            # Duplicate the text from the second column
            duplicated_text = parts[1]
            # Append the duplicated text to the end of the line
            modified_line = f"{line.strip()}|{duplicated_text}."
            # Write the modified line to the output file
            outfile.write(modified_line + "\n")
        else:
            # Write the original line to the output file if it doesn't have at least two columns
            outfile.write(line)

print("Modification complete. Output file:", output_file)