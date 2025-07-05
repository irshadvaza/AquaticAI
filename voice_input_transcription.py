
# ==============================================
# 🔹 STEP 1: SETUP AUDIO RECORDER
# # ==============================================
import speech_recognition as sr #pip install
from pydub import AudioSegment # pip install pydub , pip
from io import BytesIO
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def capture_microphone_input_as_mp3(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from microphone and save to MP3.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")
            return True, file_path

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False, str(e)

filepath="test.mp3"
#capture_microphone_input_as_mp3(filepath)
   






# ==============================================
# 🔹 STEP 2: SETUP SPEECH TO TEXT
# ==============================================
import os
from groq import Groq

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

stt_model="whisper-large-v3"

def convert_speech_to_text_with_groq(audio_filepath):
    client=Groq(api_key=GROQ_API_KEY)
    if not isinstance(audio_filepath, str):
        raise ValueError("Expected 'audio_filepath' to be a string.")
    if not os.path.isfile(audio_filepath):
        raise ValueError(f"File not found: {audio_filepath}")
    
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )
    return transcription.text

#print(convert_speech_to_text_with_groq(filepath))





# ==============================================
# 🔹 STEP 3: SETUP TEXT TO SPEECH
# ==============================================
from gtts import gTTS

def convert_text_to_speech_gtts(input_text, output_filepath):
    language="en"

    tts_audio= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    tts_audio.save(output_filepath)

input_text="Hi Sadia, you need to clean your fish tank!"

convert_text_to_speech_gtts(input_text,"gtts_test.mp3")






























input_text="Hi Sadia, you need to clearn your fish tank"
convert_text_to_speech_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")























# # ==============================================
# # 🔹 STEP 2: SETUP SPEECH TO TEXT
# # ==============================================

# import os
# from groq import Groq

# GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
# stt_model="whisper-large-v3"



# print(convert_speech_to_text_with_groq(audio_filepath))