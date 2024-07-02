'''
This is used to clean the LJSpeech formatted dataset.
'''

# Path to the metadata CSV file
metadata_file = "F:\\MS_Thesis\\raw\\filterd_metadata.csv"

# Path to the cleaned metadata CSV file
cleaned_metadata_file = "F:\\MS_Thesis\\raw\\cleaned_metadata.csv"

# Open the metadata file for reading and cleaned metadata file for writing
with open(metadata_file, "r", encoding="utf-8") as file_read, open(cleaned_metadata_file, "w", encoding="utf-8") as file_write:
    # Iterate through each line in the metadata file
    for line in file_read:
        # Strip leading and trailing whitespace characters, including quotation marks
        line = line.strip().strip('"')
        # Split the line by the "|" delimiter
        parts = line.split("|")
        if len(parts) >= 2:
            # Extract the filename and the text
            filename = parts[1]
            text = parts[0]
            # Clean the text by removing extra whitespace and ensuring a period at the end if not already present
            text = ' '.join(text.split()).strip()
            if text[-1] != '.':
                text += '.'
            # Write the filename and cleaned text to the cleaned metadata file
            file_write.write(f"{filename}|{text}\n")

print("Cleaned metadata file created successfully.")