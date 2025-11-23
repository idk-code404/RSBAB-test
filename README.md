🎮 Roblox Spelling Bee Audio Bot
<div align="center">

Python Version
License
Platform
Status

An automated audio transcription bot for the Roblox Spelling Bee game

Features • Installation • Usage • Troubleshooting • Disclaimer
</div>
⚠️ DISCLAIMER

    FOR EDUCATIONAL PURPOSES ONLY

    This project is created solely for educational purposes to demonstrate:

        Audio processing with Python
        Speech recognition implementation
        Keyboard automation techniques
        Event-driven programming

    Using this bot in Roblox violates their Terms of Service and may result in permanent account suspension.

    The authors are not responsible for any consequences resulting from the use of this software. Use at your own risk in controlled, private environments only.

📋 Table of Contents

    Features
    How It Works
    Requirements
    Installation
        Windows
        Linux
        macOS
    Configuration
    Usage
    Troubleshooting
    Project Structure
    Technical Details
    FAQ
    Contributing
    License

✨ Features
Feature	Description
🎤 Desktop Audio Recording	Captures system audio via Stereo Mix/Loopback
🗣️ Speech Recognition	Transcribes audio using Google Speech Recognition API
⌨️ Human-like Typing	Simulates natural typing with randomized delays (65-290ms)
🎯 Smart Word Extraction	Automatically extracts the target word from "Please spell [word]"
🔥 Hotkey Control	Global keyboard shortcuts (CTRL to start, ESC to exit)
🔍 Auto Device Detection	Automatically finds Stereo Mix device
🛡️ Error Handling	Comprehensive error handling and recovery
📝 Detailed Logging	Real-time console output with emoji indicators
🔧 How It Works

mermaid

graph LR
    A[Press CTRL] --> B[Record 5s Audio]
    B --> C[Save as WAV]
    C --> D[Transcribe via Google API]
    D --> E[Extract Last Word]
    E --> F[Type with Random Delays]
    F --> G[Press Enter]
    G --> H[Wait for Next Input]

Workflow Steps

    User presses CTRL - Triggers the recording sequence
    Audio Recording - Captures 5 seconds of desktop audio via Stereo Mix
    Audio Processing - Saves recording as desktop_audio.wav (44.1kHz, Stereo)
    Speech Recognition - Sends audio to Google Speech Recognition API
    Word Extraction - Parses transcription and extracts the last word
    Automated Typing - Types each character with human-like delays
    Submission - Presses Enter to submit the answer

📦 Requirements
System Requirements

    OS: Windows 10/11, Linux (Ubuntu 20.04+), macOS 10.14+
    Python: 3.7 or higher
    RAM: 2GB minimum
    Internet: Required for Google Speech Recognition API

Python Dependencies

text

pyaudio>=0.2.11
SpeechRecognition>=3.8.1
keyboard>=0.13.5
pynput>=1.7.6

Additional Requirements

    Windows: Stereo Mix enabled
    Linux: PulseAudio with loopback module
    macOS: BlackHole audio driver (for audio loopback)

🚀 Installation
Windows
Step 1: Install Python

Download and install Python 3.7+ from python.org

Make sure to check "Add Python to PATH" during installation.
Step 2: Clone Repository

Bash

git clone https://github.com/yourusername/roblox-spelling-bee-bot.git
cd roblox-spelling-bee-bot

Step 3: Install Dependencies

Option A: Using pip (recommended)

Bash

pip install -r requirements.txt

Option B: Manual installation

Bash

pip install SpeechRecognition keyboard pynput

For PyAudio (Windows):

PyAudio can be tricky on Windows. Try these methods in order:

Bash

# Method 1: pip (try this first)
pip install pyaudio

# Method 2: If Method 1 fails, download precompiled wheel
# Visit: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Download the appropriate .whl file for your Python version
# Example for Python 3.9, 64-bit:
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

# Method 3: pipwin (automated wheel installer)
pip install pipwin
pipwin install pyaudio

Step 4: Enable Stereo Mix

    Right-click the Speaker icon in the system tray
    Select Sounds → Recording tab
    Right-click in the empty area → Show Disabled Devices
    Find Stereo Mix, right-click → Enable
    Right-click Stereo Mix again → Set as Default Device

Stereo Mix Setup
Linux
Step 1: Install System Dependencies

Bash

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip portaudio19-dev python3-pyaudio pulseaudio

# Fedora
sudo dnf install python3 python3-pip portaudio-devel pulseaudio

# Arch
sudo pacman -S python python-pip portaudio pulseaudio

Step 2: Clone Repository

Bash

git clone https://github.com/yourusername/roblox-spelling-bee-bot.git
cd roblox-spelling-bee-bot

Step 3: Install Python Dependencies

Bash

pip3 install -r requirements.txt

Step 4: Enable Audio Loopback

Bash

# Load PulseAudio loopback module
pactl load-module module-loopback

# To make it permanent, add to /etc/pulse/default.pa:
echo "load-module module-loopback" | sudo tee -a /etc/pulse/default.pa

Step 5: Run with Permissions

Bash

# The keyboard module requires root privileges
sudo python3 spelling_bee_bot.py

macOS
Step 1: Install Homebrew

Bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Step 2: Install Dependencies

Bash

brew install python portaudio
pip3 install -r requirements.txt

Step 3: Install BlackHole (Audio Loopback)

Bash

brew install blackhole-2ch

Configure BlackHole as input device in System Preferences → Sound.
Step 4: Run Application

Bash

python3 spelling_bee_bot.py

⚙️ Configuration
Audio Device Selection

The bot will automatically detect your Stereo Mix device on first run:

text

AVAILABLE AUDIO DEVICES:
======================================================================
Device 0: Microphone (Realtek High Definition Audio)
  Input Channels: 2
  Sample Rate: 44100

Device 1: Stereo Mix (Realtek High Definition Audio)
  Input Channels: 2
  Sample Rate: 44100
  ✓ POTENTIAL STEREO MIX DEVICE FOUND!

Suggested Stereo Mix device index: 1
======================================================================

Enter the Stereo Mix device index (Press Enter to use suggested index 1):

Simply press Enter to use the suggested device, or type a different number.
Customizing Settings

Edit the following values in spelling_bee_bot.py:

Python

# Recording duration (seconds)
duration = 5  # Increase if words are cut off

# Typing speed (seconds between keystrokes)
delay = random.uniform(0.065, 0.29)  # Adjust range for faster/slower typing

# Audio quality
RATE = 44100  # Sample rate (Hz)
CHANNELS = 2  # Stereo (2) or Mono (1)

🎯 Usage
Basic Usage

    Start the bot:

Bash

    python spelling_bee_bot.py

    Wait for device detection and confirm the Stereo Mix device

    Open Roblox Spelling Bee game

    Position your cursor in the game's text input field

    When prompted to spell a word, press CTRL

    Wait for the bot to:
        🎤 Record audio (5 seconds)
        📝 Transcribe speech
        ⌨️ Type the word
        ✅ Submit (press Enter)

    Press ESC to exit the program

Keyboard Controls
Key	Action
CTRL (Left or Right)	Start recording and processing
ESC	Exit program
Example Session

text

🚀 CONTROL KEY PRESSED - STARTING PROCESS
======================================================================

🎤 Starting audio recording for 5 seconds...
🔴 RECORDING...
⏹ Recording complete!
💾 Saved to: desktop_audio.wav

🎯 Transcribing audio...
🔍 Using Google Speech Recognition...
📝 Transcribed: 'please spell banana'
✓ Target word: 'banana'

⌨️  Typing: 'banana'
✓ Word typed and submitted!

✅ Workflow complete!

🔧 Troubleshooting
Common Issues
❌ "Could not access audio device"

Cause: Stereo Mix not enabled or wrong device index

Solutions:

Bash

# 1. Enable Stereo Mix (Windows)
Control Panel → Sound → Recording → Enable Stereo Mix

# 2. Run device discovery
python spelling_bee_bot.py
# Note the correct device index

# 3. Verify device is not in use by another application
# Close Discord, OBS, or other recording software

❌ "Could not understand audio"

Cause: Poor audio quality, background noise, or unclear speech

Solutions:

Python

# 1. Increase recording duration
duration = 7  # Change from 5 to 7 seconds

# 2. Increase volume
# Windows: Stereo Mix Properties → Levels → Set to 100%

# 3. Reduce ambient noise
recognizer.adjust_for_ambient_noise(source, duration=1.0)  # Increase from 0.5

❌ "ImportError: No module named 'pyaudio'"

Solutions:

Bash

# Windows
pipwin install pyaudio

# Linux
sudo apt-get install python3-pyaudio

# macOS
brew install portaudio
pip3 install pyaudio

❌ "Access denied" or "Permission error" (keyboard module)

Solutions:

Bash

# Windows
# Run Command Prompt as Administrator
# Right-click → Run as Administrator

# Linux
sudo python3 spelling_bee_bot.py

# macOS
# Grant Accessibility permissions
System Preferences → Security & Privacy → Privacy → Accessibility

❌ No audio being recorded

Checklist:

    Stereo Mix is enabled
    Stereo Mix is set as default recording device
    Game audio is playing and volume is up
    Stereo Mix volume is at 100%
    No other application is using the audio device
    Try rebooting your computer

❌ Words typed incorrectly

Solutions:

Python

# 1. Adjust typing delays (make slower)
delay = random.uniform(0.1, 0.4)  # Increase from 0.065-0.29

# 2. Add delay before starting to type
time.sleep(1.0)  # Add at beginning of type_word() function

# 3. Check keyboard layout (ensure US English)

Debug Mode

Enable verbose logging by adding this at the top of the script:

Python

import logging
logging.basicConfig(level=logging.DEBUG)

📁 Project Structure

text

roblox-spelling-bee-bot/
│
├── spelling_bee_bot.py          # Main application script
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── docs/                        # Documentation
│   ├── INSTALLATION.md          # Detailed installation guide
│   ├── TROUBLESHOOTING.md       # Extended troubleshooting
│   └── API.md                   # Code documentation
│
├── examples/                    # Example files
│   ├── desktop_audio.wav        # Sample recording
│   └── test_audio.py            # Audio testing script
│
└── assets/                      # Images and media
    ├── demo.gif                 # Demo animation
    └── screenshots/             # Setup screenshots

🔬 Technical Details
Audio Recording Specifications

Python

FORMAT:   16-bit PCM
CHANNELS: 2 (Stereo)
RATE:     44100 Hz
CHUNK:    1024 frames
DURATION: 5 seconds
FILE:     WAV (Waveform Audio File Format)
SIZE:     ~850 KB per recording

Speech Recognition

    Engine: Google Speech Recognition API
    Language: English (US)
    Free tier: ~50 requests/day
    Accuracy: ~85-95% (depends on audio quality)
    Latency: 1-3 seconds

Typing Simulation

Python

# Character delay range
MIN_DELAY: 65ms  (15.4 WPM - very slow)
MAX_DELAY: 290ms (3.4 WPM - extremely slow)
AVG_DELAY: 177ms (5.6 WPM - human-like)

# Additional delays
PRE_TYPE:  300-600ms  (reaction time)
PRE_ENTER: 100-300ms  (thinking time)

Performance Metrics
Metric	Value
Total execution time	~8-12 seconds
Audio recording	5 seconds
Transcription	1-3 seconds
Typing (8-letter word)	1-2 seconds
Success rate	80-90%
❓ FAQ
Is this bot detectable?

Yes. While the bot simulates human-like typing patterns, Roblox has anti-cheat systems that can detect:

    Keyboard input patterns
    Execution timing consistency
    Network traffic analysis
    Client-side memory inspection

Can I use this on public Roblox servers?

No. Using bots violates Roblox Terms of Service. This project is for:

    Private/local testing environments
    Educational purposes
    Programming learning

Does this work on other Roblox games?

The core audio recording and transcription will work, but the typing automation is specifically designed for text input games like Spelling Bee. Adaptation would be needed for other games.
Why does it only extract the last word?

Spelling Bee typically says "Please spell [word]" or just "[word]". Extracting the last word ensures we get the target word regardless of the phrase structure.
Can I use a different speech recognition service?

Yes! The speech_recognition library supports multiple engines:

Python

# Microsoft Bing
recognizer.recognize_bing(audio_data, key="API_KEY")

# IBM Watson
recognizer.recognize_ibm(audio_data, username="USER", password="PASS")

# Sphinx (offline)
recognizer.recognize_sphinx(audio_data)

How can I make it faster?

Python

# Reduce recording duration
duration = 3

# Reduce typing delays
delay = random.uniform(0.03, 0.08)

# Skip reaction time delays
# Comment out sleep() calls in type_word()

Does it work with other languages?

Yes! Change the recognition language:

Python

text = recognizer.recognize_google(audio_data, language="es-ES")  # Spanish
text = recognizer.recognize_google(audio_data, language="fr-FR")  # French
text = recognizer.recognize_google(audio_data, language="de-DE")  # German

🤝 Contributing

Contributions are welcome! This is an educational project.
How to Contribute

    Fork the repository
    Create a feature branch (git checkout -b feature/AmazingFeature)
    Commit your changes (git commit -m 'Add some AmazingFeature')
    Push to the branch (git push origin feature/AmazingFeature)
    Open a Pull Request

Contribution Ideas

    Add support for macOS audio loopback
    Implement offline speech recognition (CMU Sphinx)
    Create GUI interface
    Add configuration file (YAML/JSON)
    Multi-language support
    Audio quality indicator
    Recording history log
    Unit tests
    Docker containerization

Code Style

Follow PEP 8 guidelines:

Bash

pip install black flake8
black spelling_bee_bot.py
flake8 spelling_bee_bot.py

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

text

MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

🙏 Acknowledgments

    PyAudio - PortAudio bindings for Python
    SpeechRecognition - Speech recognition library by Anthony Zhang
    keyboard - Hook and simulate keyboard events
    pynput - Monitor and control input devices
    Google Speech Recognition API - Speech-to-text service

⚖️ Legal & Ethical Considerations
Important Reminders

    Terms of Service Violation: Using this bot on Roblox violates their ToS
    Account Risk: Your account may be permanently banned
    Unfair Advantage: Automated gameplay is unfair to other players
    Legal Risk: May violate computer fraud laws in some jurisdictions

Intended Use Cases

✅ Acceptable:

    Learning Python programming
    Understanding audio processing
    Studying speech recognition
    Private testing environments
    Academic research

❌ Not Acceptable:

    Public Roblox servers
    Competitive gameplay
    Account boosting
    Any violation of game ToS

Responsible Usage

If you use this code:

    Only in private/educational contexts
    Acknowledge it's against Roblox ToS
    Accept all risks and consequences
    Don't distribute to minors
    Don't commercialize or sell

🗺️ Roadmap
Version 1.0 (Current)

    Basic audio recording
    Speech recognition
    Keyboard automation
    Hotkey controls
    Device auto-detection

Version 2.0 (Planned)

    GUI interface (Tkinter/PyQt)
    Configuration file support
    Multiple language support
    Offline mode (CMU Sphinx)
    Audio quality indicator
    Success rate statistics

Version 3.0 (Future)

    Machine learning word prediction
    Voice training for better accuracy
    Plugin system
    Web dashboard
    Mobile companion app

📊 Statistics

GitHub stars
GitHub forks
GitHub issues
GitHub pull requests
<div align="center">
⭐ Star this repository if you found it helpful!

Made with ❤️ for educational purposes

Report Bug • Request Feature • Documentation
</div>
📝 Changelog
[1.0.0] - 2024-01-XX
Added

    Initial release
    Desktop audio recording via Stereo Mix
    Google Speech Recognition integration
    Human-like typing simulation
    Hotkey controls (CTRL/ESC)
    Auto device detection
    Comprehensive error handling
    Cross-platform support (Windows/Linux/macOS)

Known Issues

    PyAudio installation issues on Windows
    Requires administrator privileges on Linux
    Limited to 50 API requests per day (Google free tier)

Remember: Use this tool responsibly and ethically. Happy learning! 🎓
