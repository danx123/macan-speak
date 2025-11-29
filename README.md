Macan Speak (notes_speech)
Macan Speak is a standalone, lightweight speech-to-text engine designed as a companion module for Macan Notes Pro. It leverages Google's Speech Recognition API to provide accurate, real-time voice transcription (specifically optimized for the Indonesian language) without impacting the performance of the main application.
🚀 Overview
Processing real-time audio and communicating with external APIs can be resource-intensive. To ensure Macan Notes Pro maintains a fluid, non-blocking user interface (UI), the speech recognition logic is decoupled into this separate executable (notes_speech.exe).
Key Features:
Non-Blocking Operation: Runs as a separate process, preventing UI freezes in the main application.
Standard Output Communication: Transmits transcribed text via stdout, allowing easy integration with any application capable of spawning subprocesses (e.g., QProcess in Qt/PySide6).
Optimized Configuration: Pre-configured energy thresholds for optimal voice detection in various environments.
Indonesian Support: Hardcoded support for id-ID locale.
🛠️ Architecture
Macan Speak operates as a Console Application. It does not have a graphical user interface (GUI).
Spawn: The main app (Macan Notes) launches notes_speech.exe.
Listen: The engine listens to the default system microphone.
Transcribe: Audio is processed using speech_recognition and Google Web Speech API.
Output: The result is printed to stdout (UTF-8 encoded).
Ingest: Macan Notes captures the standard output and inserts the text into the active editor.
📦 Installation (For End Users)
If you are a user of Macan Notes Pro and need to enable the "Speech to Text" feature, follow these steps:
Download the latest release of notes_speech.exe from the Releases Page.
Create the following directory path on your Windows system if it does not exist:
Plaintext
C:\Program Files\Macan Angkasa\Macan Speak\

Move the downloaded notes_speech.exe into that folder.
Final Path: C:\Program Files\Macan Angkasa\Macan Speak\notes_speech.exe
Restart Macan Notes Pro.
🔧 Development & Build Instructions
If you wish to modify the source code or build the executable yourself.
Prerequisites
Python 3.8+
Virtual Environment (Recommended)
1. Install Dependencies
Bash
pip install SpeechRecognition pyaudio pyinstaller

Note: You may need to install PortAudio headers if you are not on Windows, though pip install pyaudio usually includes the binary wheels for Windows.
2. Running from Source
You can test the script directly. Note that it will print the transcribed text to your terminal.
Bash
python notes_speech.py

3. Building the Executable
To compile the script into a standalone .exe that runs in the background (without a console window), use PyInstaller:
Bash
pyinstaller --noconsole --onefile --name "notes_speech" notes_speech.py

--noconsole: Prevents a terminal window from popping up when the app is launched by Macan Notes.
--onefile: Bundles everything into a single .exe file.
The output file will be located in the dist/ folder.
📝 License
This project is part of the Macan Angkasa ecosystem. Copyright © 2025 Danx Exodus. All Rights Reserved.

Disclaimer: This module relies on the Google Web Speech API. An active internet connection is required for transcription to work.
