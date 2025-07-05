import streamlit as st

from modelbrain import get_ai_response_from_image_and_text
from voice_input_transcription import capture_microphone_input_as_mp3,convert_speech_to_text_with_groq,convert_text_to_speech_gtts

col1, col2 =st.columns(2)

with col1: 
    st.header("User Input")
    with st.expander ("Follow below steps:"):
        st.write("""
                1. Upload affected Aquatic animal Image
                2. Speak and record your query
                 3. Write the symptom. 
                 """)
    st.subheader("📸 Upload Image")
    uploaded_image = st.file_uploader("Upload an image of the aquatic animal", type=["jpg", "jpeg", "png"])

    st.subheader("🎙️ Record Voice Query")
    audio_output_path = "recorded_user_query1.mp3"
    voicequery = ""

    if st.button("🎤 Start Recording"):
        with st.spinner("Recording... please speak now"):
            success, result = capture_microphone_input_as_mp3(audio_output_path, timeout=10, phrase_time_limit=10)
            #time.sleep(1)

        

