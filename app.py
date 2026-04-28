import streamlit as st
from faster_whisper import WhisperModel
import os
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="AI Audio Annotator", layout="wide")
st.title("🎙️ AI-Assisted STT Annotator")

@st.cache_resource
def load_model():
    # Using 'base' for speed; use 'large-v3' for maximum accuracy
    return WhisperModel("base", device="cpu", compute_type="int8")

model = load_model()

# --- SIDEBAR: FILE UPLOAD ---
with st.sidebar:
    st.header("1. Upload Audio")
    uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav", "m4a"])
    
    st.header("2. Settings")
    min_prob = st.slider("Min Probability Threshold", 0.0, 1.0, 0.5)

# --- MAIN INTERFACE ---
if uploaded_file:
    # Save temp file
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio("temp_audio.mp3")

    # Trigger Transcription
    if st.button("✨ Auto-Transcribe with Whisper"):
        with st.spinner("Analyzing audio..."):
            segments, info = model.transcribe("temp_audio.mp3", beam_size=5)
            
            # Store segments in session state for editing
            st.session_state.transcript = [
                {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()}
                for s in segments
            ]
            st.success(f"Detected language: {info.language} ({info.language_probability:.2f})")

    # --- ANNOTATION AREA ---
    if "transcript" in st.session_state:
        st.subheader("3. Edit Transcription")
        st.info("Click on the text cells below to correct the AI output.")

        # Display as an interactive data editor
        edited_data = st.data_editor(
            st.session_state.transcript,
            num_rows="dynamic",
            column_config={
                "start": st.column_config.NumberColumn("Start (s)", format="%.2f"),
                "end": st.column_config.NumberColumn("End (s)", format="%.2f"),
                "text": st.column_config.TextColumn("Transcription", width="large"),
            },
            key="transcript_editor"
        )

        # --- EXPORT ---
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💾 Save Changes"):
                st.session_state.transcript = edited_data
                st.toast("Progress saved locally!")

        with col2:
            # Convert to SRT format for export
            srt_content = ""
            for i, row in enumerate(edited_data):
                start = str(datetime.timedelta(seconds=row['start'])).replace(".", ",")[:11]
                end = str(datetime.timedelta(seconds=row['end'])).replace(".", ",")[:11]
                srt_content += f"{i+1}\n{start} --> {end}\n{row['text']}\n\n"

            st.download_button(
                label="📥 Export as .SRT",
                data=srt_content,
                file_name="annotation.srt",
                mime="text/plain"
            )
else:
    st.info("Please upload an audio file to begin.")