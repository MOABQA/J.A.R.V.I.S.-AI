
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

```bash
pip install speech_recognition pyttsx3 pyautogui
```
## How to Use

**Clone the Repository:**

```bash
git clone <your-repo-url>
```
**Navigate to the Project Directory:**

```bash
cd JARVIS-Voice-Assistant
```
**Run the Script:**
```bash
python main.py
```
Ensure your microphone is set up correctly for voice recognition.
## Interact with J.A.R.V.I.S.:

**Activate J.A.R.V.I.S.:** 

Start any command with "Jarvis". For example, say "Jarvis" followed by your command like:
- "Jarvis, open Google" to launch the Google homepage.
- "Jarvis, play music" to start playing songs from your defined music folder.
- "Jarvis, what's the time?" to hear the current time.
**Common Commands:**
- Open Websites: Say "Jarvis, open [website name]" (e.g., YouTube, Google).
- Launch Applications: Say "Jarvis, open [application name]" (e.g., Calculator, PowerPoint). Ensure the application names match those on your system.
- Basic Calculations: Say "Jarvis, what is [number] plus/minus/times/divided by [number]?"
- Check Date and Time: Use commands like "Jarvis, what day is today?" or "Jarvis, tell me the date."

**Tips for Best Use:**

- Voice Recognition: Speak clearly and at a moderate pace. Background noise can affect recognition accuracy, so consider using this in a quiet environment.
Customization: Before running, you might want to adjust the music_path in the script to point to your music directory for the music feature to work correctly.

- Command Accuracy: If J.A.R.V.I.S. does not recognize your command, try rephrasing or speaking more distinctly.

**Troubleshooting:**

If commands aren't working, check your microphone settings or ensure the necessary applications and websites are correctly configured or linked in the script.

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
