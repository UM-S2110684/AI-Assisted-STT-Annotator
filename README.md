🎙️ AI-Assisted Speech-to-Text (STT) Annotation Tool

A lightweight, professional-grade audio annotation platform built with **Python**, **Streamlit**, and **OpenAI's Whisper (via Faster-Whisper)**. This tool allows users to upload audio, generate automatic transcriptions with timestamps, and manually refine them through an interactive UI.

## 🚀 Features

-   **AI Pre-labeling**: Automatically transcribe audio using high-performance Whisper models.
-   **Interactive Data Editor**: Edit transcripts, adjust timestamps, and manage segments in a clean, spreadsheet-like interface.
-   **Local Processing**: Privacy-focused—your audio stays on your machine.
-   **Waveform Playback**: Integrated audio player to verify transcriptions in real-time.
-   **Standard Export**: Export your final annotations in `.SRT` format for subtitles or dataset training.
-   **Scalable**: Easily switch between `tiny`, `base`, and `large-v3` models depending on your hardware.

## 🛠️ Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **Inference Engine**: [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
-   **Audio Processing**: [Librosa](https://librosa.org/)

## 📦 Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/stt-annotation-tool.git](https://github.com/yourusername/stt-annotation-tool.git)
cd stt-annotation-tool
