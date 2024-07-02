import jiwer

# Reference texts
references = [
    "Og hvis ingen gør indsigelse, betragter jeg samtykke som givet.",
    "Det første punkt på dagsordenen er indstillet fra UL til valgsprøvelse.",
    "Christian Friis Bakken nedlagde sit mandat.",
    "Og er der nogen, der ønsker ordet?",
    "Da det ikke er tilfældet, går vi til afstemning."
]

# Transcribed texts (from ASR)
transcribed_texts = [
    "Og hvis ingen går ind til disse, betragter et hjemtue som givet.",
    "Det første punkt per dag, så ønsker du at få ud til valvsbrugelsen.",
    "Kristian Højsborg, og det er segmentet.",
    "Hvad er det, Det er jo ikke det.",
    "der ikke er tilfældet, gør vi til afstand."
]

# Calculate WER for each sentence pair
for ref, trans in zip(references, transcribed_texts):
    error = jiwer.wer(ref, trans)
    print(f"Reference: {ref}")
    print(f"Transcribed: {trans}")
    print(f"WER: {error}\n")

# Calculate the average WER over all sentences
average_wer = jiwer.wer(references, transcribed_texts)
print(f"Average WER: {average_wer}")
