
# J.A.R.V.I.S. Voice Assistant

A Python-based voice assistant inspired by Iron Man's J.A.R.V.I.S., allowing voice commands for various tasks like web browsing, playing music, and basic calculations.

## Features

- **Voice Interaction:** Uses Google's Speech Recognition for voice commands and Pyttsx3 for text-to-speech.
- **Task Automation:** 
  - Open websites (Google, YouTube, etc.)
  - Launch applications (Calculator, PowerPoint, etc.)
  - Play music from a designated folder
  - Perform basic arithmetic operations
- **Time & Date:** Provides current time, date, and day of the week on request.
- **Customizable:** Adjust voice speed and volume; easily add new commands or modify existing ones.

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `pyautogui` (for GUI automation)
  
You can install the necessary libraries using pip:

```bash```
pip install speech_recognition pyttsx3 pyautogui

## How to Use
**Clone the Repository:**
```bash```
git clone <your-repo-url>
**Navigate to the Project Directory:**
```bash```
cd JARVIS-Voice-Assistant
**Run the Script:**
```bash```
python main.py

Ensure your microphone is set up correctly for voice recognition.
## Interact with J.A.R.V.I.S.:
Say "Jarvis" followed by your command (e.g., "Jarvis, open Google").

## Known Limitations
- Speech recognition might not work perfectly in environments with high background noise.
- The music feature requires you to define a correct music_path.
- Some commands like 'classroom' links need to be replaced with actual URLs.

## Customization
Voice Settings: Modify the properties in the 'VOICE SETUP' section of the code for different voice effects.
Commands: Add or modify entries in the websites or apps dictionaries to personalize what J.A.R.V.I.S. can do for you.

## License
This project is open source under the MIT License (LICENSE).

## Acknowledgements
This project was inspired by the J.A.R.V.I.S. AI from the Marvel Cinematic Universe's Iron Man series.
Thanks to the creators of the libraries used.

Feel free to contribute, suggest enhancements, or report issues!
