import os
import requests
import tempfile
from pydub import AudioSegment
from pydub.utils import make_chunks
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"
WHISPER_API_KEY = os.environ["WHISPER_API_KEY"]

MAX_CHUNK_SIZE = 25 * 1024 * 1024  # 25 MB

def transcribe_audio(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(
            WHISPER_API_URL,
            headers={
                "Authorization": f"Bearer {WHISPER_API_KEY}"
            },
            files={"file": f},
            data={"model": "whisper-1"}
        )
    response.raise_for_status()
    return response.json()["text"]

def main():
    st.title("Audio/Video Transcription")
    st.write("Upload an audio or video file to get the transcript")

    uploaded_file = st.file_uploader("Choose an audio or video file", type=["wav", "mp3", "mp4", "avi", "mkv", "flv", "m4a"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
            temp_audio_file.write(uploaded_file.getvalue())
            temp_audio_file.flush()

            audio = AudioSegment.from_file(temp_audio_file.name)
            audio.export("temp_audio_file.mp4", format="mp4")

            audio = AudioSegment.from_file("temp_audio_file.mp4")
            bitrate = audio.frame_rate * audio.sample_width * audio.channels
            max_chunk_duration_ms = (MAX_CHUNK_SIZE * 8000) // bitrate
            audio_chunks = make_chunks(audio, max_chunk_duration_ms)

            transcriptions = []
            for i, chunk in enumerate(audio_chunks):
                chunk.export(f"temp_audio_chunk_{i}.mp4", format="mp4")
                transcription = transcribe_audio(f"temp_audio_chunk_{i}.mp4")
                transcriptions.append(transcription)

            full_transcription = "\n".join(transcriptions)

            # Display the transcription on the screen
            st.text(full_transcription)
            
            # Save the transcription to a .txt file
            txt_filename = uploaded_file.name.split('.')[0] + ".txt"
            with open(txt_filename, "w") as txt_file:
                txt_file.write(full_transcription)
            
            # Provide download option for the .txt file
            with open(txt_filename, "rb") as txt_file:
                txt_data = txt_file.read()
                st.download_button("Download Transcript", data=txt_data, file_name=txt_filename, mime="text/plain")


if __name__ == "__main__":
    main()
