'''
    This is used to display several losses for tortoise tts
'''

import re
import matplotlib.pyplot as plt

# Read the log from the log file
with open(r"F:\MS_Thesis\tortoise-tts-ex\DA-training\DA-train-run-900\train_DA-train-run-1_240420-134852.log", "r") as file:
    text = file.read()

pattern = r"loss_text_ce:\s(\d+.\d+e[+-]\d+)\sloss_mel_ce:\s(\d+.\d+e[+-]\d+)\sloss_gpt_total:\s(\d+.\d+e[+-]\d+)"

matches = re.findall(pattern, text)

loss_text_ce = [float(x[0]) for x in matches]
loss_mel_ce = [float(x[1]) for x in matches]
loss_gpt_total = [float(x[2]) for x in matches]

plt.figure(figsize=(10, 6))

plt.plot(loss_text_ce, label="loss_text_ce")
plt.plot(loss_mel_ce, label="loss_mel_ce")
plt.plot(loss_gpt_total, label="loss_gpt_total")

plt.xlabel('Time step')
plt.ylabel('Loss value')
plt.title('Loss value over time')
plt.legend()

plt.show()