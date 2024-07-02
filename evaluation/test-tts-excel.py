import jiwer
import pandas as pd

# Read the input Excel file
input_file = 'TTS_Evaluation_Data.xlsx'
data = pd.read_excel(input_file)

# Initialize lists to store the results
reference_sentences = data['Reference Sentence'].tolist()
generated_sentences = data['Generated Sentence'].tolist()
wer_list = []

# Calculate WER for each sentence pair and convert to percentage with two decimal places
for ref, trans in zip(reference_sentences, generated_sentences):
    error = jiwer.wer(ref, trans) * 100  # Convert to percentage
    wer_list.append(round(error, 2))  # Round to two decimal places

# Add the WER results to the DataFrame
data['WER (%)'] = wer_list

# Calculate the average WER over all sentences and convert to percentage with two decimal places
average_wer = round(sum(wer_list) / len(wer_list), 2)
print(f"Average WER: {average_wer:.2f}%")

# Add a row for the average WER
average_wer_row = pd.DataFrame({'Reference Sentence': ['Average'], 'Generated Sentence': [''], 'WER (%)': [average_wer]})
data = pd.concat([data, average_wer_row], ignore_index=True)

# Write the results to a new Excel file
output_file = 'TTS_Evaluation_Results.xlsx'
data.to_excel(output_file, index=False)

print(f"Results written to {output_file}")