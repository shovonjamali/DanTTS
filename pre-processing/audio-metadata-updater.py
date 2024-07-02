'''
    Update audio metadata: track, title
    Update audio metadata for wavs
'''

### Updated for me
import os
import shutil
import taglib

def update_metadata(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.wav'):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name)

            # Load WAV file and update metadata
            with taglib.File(input_file) as audio:
                # Set the title to match the file name without the extension
                audio.tags["TITLE"] = [os.path.splitext(file_name)[0]]
                # Set the track number to match the file name without the extension
                audio.tags["TRACKNUMBER"] = [os.path.splitext(file_name)[0]]

                # Save updated WAV file
                audio.save()

            # Copy the updated file to the output folder instead of moving it
            shutil.copy2(input_file, output_file)

            print(
                f"Updated metadata for {file_name}: title='{os.path.splitext(file_name)[0]}', track number={os.path.splitext(file_name)[0]}")
        else:
            print(f"Ignoring non-WAV file: {file_name}")

if __name__ == "__main__":
    input_folder = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\wavs_second"  # Your path
    output_folder = "G:\\ML_Practice\\amlfall23\\Thesis-pre-processing\\wavs"  # Your path
    update_metadata(input_folder, output_folder)
