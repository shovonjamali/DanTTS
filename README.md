# DanTTS
A zero-shot Danish voice cloning system was developed by fine-tuning the Tortoise TTS model, achieving 15.5% coverage of frequent Danish words and demonstrating cross-lingual transfer learning. The system also integrated a translation pipeline to assist immigrant patients, enabling seamless Danish-to-other-language communication for improved accessibility in healthcare.

## Data sources
[FT Speech](https://ftspeech.github.io/)<br>
[Nota audio and text data](https://sprogteknologi.dk/dataset/notalyd-ogtekstdata?)<br>
[Mozilla common voice](https://commonvoice.mozilla.org/en/datasets)<br>
[NST Danish ASR Database](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-55/?)<br>
[Audio books](http://www.kloerkonge.dk/content/sindssygt-langt-ude-koebenhavnske-godnathistorier)<br>

## Technical Stack
- **Python**
- **TortoiseTTS**
- **Whisper**
- **FFMPEG**
- **META NLLB**

## Key Features
- Processed 19,000+ audio clips (26+ hours, ~4GB) from diverse datasets: FTSpeech, Mozilla Common Voice, NST Danish ASR, Nota Audio.
- Integrated Whisper for transcription and NLLB for translation, creating a multilingual communication pipeline.
- Evaluated system performance using Word Error Rate (WER) and comparative analysis against existing translation models.
- Trained a Byte Pair Encoding (BPE) tokenizer for Danish text and implemented audio noise removal across 19,000+ samples.
- Conducted an in-depth ethical analysis covering legal, privacy, and security concerns related to voice cloning in healthcare.

## Results and Impact
- Achieved a Word Error Rate (WER) of 55.43%.
- Performed extensive Exploratory Data Analysis (EDA) on text and audio data to ensure high-quality preprocessing and dataset insights.
