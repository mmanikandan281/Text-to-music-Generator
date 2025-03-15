
# 🎵 Text-to-Music Generator with Meta’s Audiocraft (MusicGen)  

This project uses Meta’s Audiocraft library to generate music from text descriptions. It leverages the **MusicGen Small Model** to create unique audio pieces based on user input.


![Screenshot (77)](https://github.com/user-attachments/assets/b375af8c-ecc6-4348-bd17-615a4b0e278e)



## 🚀 Features  
- Generate music from text descriptions.  
- Adjust the duration of generated music (1 to 20 seconds).  
- Save generated audio to Google Drive.  
- Listen to generated audio directly in the app.  
- Simple UI built with **Streamlit**.  

---

## 📦 Installation  

1. Clone this repository:  
   ```bash
   https://github.com/mmanikandan281/Text-to-music-Generator.git
   cd your-repo-name
   ```

2. Install dependencies:  
   ```bash
   pip install torch torchaudio audiocraft scipy streamlit ffmpeg
   ```

3. Install the required packages(if running in vscode): 
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Setup (Optional but Recommended)  

Mount Google Drive if using Google Colab:  
```python
from google.colab import drive
drive.mount('/content/drive')
```

---

## 🏃‍♂️ Running the App  

1. Save the script as `app.py` (already included in this repo).  
2. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

If you're using Colab, expose the app using LocalTunnel:  
```bash
!streamlit run app.py & npx localtunnel --port 8501
```

---

## 📝 Usage  

1. Enter a text prompt describing the music you want.  
2. Choose the duration using the slider.  
3. Click the **"Generate Music"** button.  
4. Listen to the generated audio directly or download it.  

---

## 📜 Code Overview  

- **Model Loading:** Uses `facebook/musicgen-small` from Audiocraft.  
- **Text-to-Music Generation:** Generates audio tensors based on the provided description and duration.  
- **Audio Saving:** Saves generated music as `generated_music.wav` in Google Drive.  
- **UI:** Built with Streamlit, allowing a simple interface for input and audio playback.  

---

## 🔗 Google Colab Link  

Run this project on Google Colab:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1G20-GKJv1lw4X49vJCGPnLKEOMk4zu-6?usp=sharing)  

---

## 📧 Contact  

If you have any questions or feedback, feel free to reach out! 🚀  

---

Let me know if you’d like to add or modify anything else! 🌟
