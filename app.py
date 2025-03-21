# -*- coding: utf-8 -*-
"""Text to music.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G20-GKJv1lw4X49vJCGPnLKEOMk4zu-6
"""

!pip install audiocraft

!pip install streamlit

# Step 1: Install dependencies (Run this once in a Colab cell)
!pip install torch torchaudio audiocraft scipy streamlit ffmpeg

# Step 2: Mount Google Drive (Optional but recommended)
from google.colab import drive
drive.mount('/content/drive')

# Step 3: Import required libraries
import os
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import streamlit as st
import scipy
import torch

print("Loaded dependencies successfully!")

# Step 4: Create a directory to store generated audio
# Instead of trying to open a file that might not exist, create the directory if it doesn't exist
output_dir = "/content/drive/MyDrive/MusicGen_Audio"
os.makedirs(output_dir, exist_ok=True)

# Attempt to load audio only if it exists
audio_file_path = os.path.join(output_dir, "generated_music.wav")
if os.path.exists(audio_file_path):
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format='audio/wav')  # Display existing audio


@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(description, duration: int):
    print("Description: ", description)
    print("Duration: ", duration)

    model = load_model()
    model.set_generation_params(duration=duration)
    wav = model.generate([description])

    return wav, model.sample_rate

def save_audio(wav, sample_rate):
    """Save generated audio to Google Drive"""
    file_path = f"{output_dir}/generated_music.wav"
    for idx, one_wav in enumerate(wav):
        audio_write(file_path, one_wav.cpu(), sample_rate, strategy="loudness", loudness_compressor=True)
    return file_path

def main():
    st.title("🎵 Text to Music Generator")

    with st.expander("See explanation"):
        st.write("Music Generator using Meta's Audiocraft library (MusicGen Small Model).")

    text_area = st.text_area("Enter your description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 1, 20, 10)

    if text_area and time_slider:
         if st.button("Generate Music"):
            st.write("Generating music... ⏳")
            wav, sample_rate = generate_music_tensors(text_area, time_slider)

            st.write("Saving generated music...")
            audio_path = save_audio(wav, sample_rate)

            st.audio(audio_path, format='audio/wav') # Display the generated audio
            st.write(f"🎵 Download your music: [Click Here]({audio_path})")
# ...
if __name__ == "__main__":
    main()

# Inside your main function, after generating and saving the audio:
# ...

code = """
import os
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import streamlit as st
import scipy
import torch

print("Loaded dependencies successfully!")

# Step 4: Create a directory to store generated audio
output_dir = "/content/drive/MyDrive/MusicGen_Audio"
os.makedirs(output_dir, exist_ok=True)

@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(description, duration: int):
    print("Description: ", description)
    print("Duration: ", duration)

    model = load_model()
    model.set_generation_params(duration=duration)
    wav = model.generate([description])

    return wav, model.sample_rate

def save_audio(wav, sample_rate):
    \"\"\"Save generated audio to Google Drive\"\"\"
    file_path = f"{output_dir}/generated_music.wav"
    for idx, one_wav in enumerate(wav):
        audio_write(file_path, one_wav.cpu(), sample_rate, strategy="loudness", loudness_compressor=True)
    return file_path

def main():
    st.title("🎵 Text to Music Generator")

    with st.expander("See explanation"):
        st.write("Music Generator using Meta's Audiocraft library (MusicGen Small Model).")

    text_area = st.text_area("Enter your description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 1, 20, 10)

    if text_area and time_slider:
        if st.button("Generate Music"):
            st.write("Generating music... ⏳")
            wav, sample_rate = generate_music_tensors(text_area, time_slider)

            st.write("Saving generated music...")
            audio_path = save_audio(wav, sample_rate)

            st.audio(audio_path, format='audio/wav')
            st.write(f"🎵 Download your music: [Click Here]({audio_path})")

if __name__ == "__main__":
    main()
"""

# Save the script to app.py
with open("app.py", "w") as f:
    f.write(code)

print("✅ Script saved as app.py!")

!streamlit run app.py & npx localtunnel --port 8501
st.progress()

!curl ifconfig.me

"""Thank You
Done by Manikandan M

"""