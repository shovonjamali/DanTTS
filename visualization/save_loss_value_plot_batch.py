import os
import re
import matplotlib.pyplot as plt

# Define input and output directories
input_directory = r"F:\MS_Thesis\tortoise-tts-ex\DA-training\logs"
output_directory = r"F:\MS_Thesis\tortoise-tts-ex\DA-training\plots"

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate over each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".log"):
        # Construct full file path
        file_path = os.path.join(input_directory, filename)
        
        # Read the log from the log file
        with open(file_path, "r") as file:
            text = file.read()

        # Define the pattern to extract loss values
        pattern = r"loss_text_ce:\s(\d+\.\d+e[+-]\d+)\sloss_mel_ce:\s(\d+\.\d+e[+-]\d+)\sloss_gpt_total:\s(\d+\.\d+e[+-]\d+)"

        # Find all matches in the text
        matches = re.findall(pattern, text)

        # Extract loss values
        loss_text_ce = [float(x[0]) for x in matches]
        loss_mel_ce = [float(x[1]) for x in matches]
        loss_gpt_total = [float(x[2]) for x in matches]

        # Plot the loss values
        plt.figure(figsize=(10, 6))
        plt.plot(loss_text_ce, label="loss_text_ce")
        plt.plot(loss_mel_ce, label="loss_mel_ce")
        plt.plot(loss_gpt_total, label="loss_gpt_total")
        plt.xlabel('Time step')
        plt.ylabel('Loss value')
        plt.title('Loss value over time')
        plt.legend()

        # Save the plot as an image to the output directory
        output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.png")
        plt.savefig(output_path)
        plt.close()

print("Plots saved successfully.")
