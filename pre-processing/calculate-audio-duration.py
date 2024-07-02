'''
This calculates the total duraion for the audios in hour and minutes.
'''

import os
import wave

def get_audio_duration(audio_file):
    with wave.open(audio_file, 'rb') as audio:
        # Get the number of frames and frame rate
        num_frames = audio.getnframes()
        frame_rate = audio.getframerate()

        # Calculate the duration in seconds
        duration_seconds = num_frames / float(frame_rate)
        
    return duration_seconds

def format_duration(duration_seconds):
    # Convert seconds to hours and minutes
    hours = int(duration_seconds // 3600)
    minutes = int((duration_seconds % 3600) // 60)

    return hours, minutes

def calculate_total_duration(audio_folder):
    total_duration_seconds = 0

    # Iterate over all audio files in the folder
    for file_name in os.listdir(audio_folder):
        if file_name.endswith('.wav'):
            audio_file = os.path.join(audio_folder, file_name)
            total_duration_seconds += get_audio_duration(audio_file)

    # Format total duration to hours and minutes
    total_hours, total_minutes = format_duration(total_duration_seconds)

    return total_hours, total_minutes

audio_folder = r"F:\MS_Thesis\dataset\tortoise-model-training-v2\Filtered-Audio-Dataset\Svenskerne_version7_Vocals"
total_hours, total_minutes = calculate_total_duration(audio_folder)
print(f'Total duration of audio files: {total_hours} hours and {total_minutes} minutes')