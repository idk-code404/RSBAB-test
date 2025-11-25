Roblox Spelling Bee Audio Bot

i have not tested it yet because i coded it for windows not linux

A Python bot that listens to Roblox Spelling Bee audio, transcribes the word, and types it automatically.
⚠️ DISCLAIMER

FOR EDUCATIONAL PURPOSES ONLY

Using bots in Roblox violates their Terms of Service and will get your account banned. This is a learning project for audio processing and speech recognition.
🚀 Quick Start
1. Install Python Dependencies

Bash

pip install pyaudio SpeechRecognition keyboard pynput

Windows PyAudio Fix (if pip fails):

Bash

# Download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

2. Enable Stereo Mix (Windows)

    Right-click Speaker icon → Sounds
    Go to Recording tab
    Right-click empty space → Show Disabled Devices
    Right-click Stereo Mix → Enable
    Right-click Stereo Mix → Set as Default Device

3. Run the Bot

Bash

python spelling_bee_bot.py

🎯 How to Use

    Start the bot
    Select your Stereo Mix device (or press Enter for auto-detect)
    Open Roblox Spelling Bee game
    When the game asks you to spell a word, press CTRL
    The bot will record, transcribe, and type the word
    Press ESC to exit

Controls
Key	Action
CTRL	Start recording & typing
ESC	Exit program
🔧 How It Works

text

Press CTRL → Record 5s Audio → Transcribe → Type Word → Press Enter

🐛 Common Issues

"Could not access audio device"

    Enable Stereo Mix in Windows Sound settings
    Make sure no other app is using it

"Could not understand audio"

    Turn up game volume
    Set Stereo Mix volume to 100%

"Permission denied" (keyboard module)

    Run as Administrator (Windows)
    Use sudo on Linux

PyAudio won't install

    Use pipwin install pyaudio
    Or download wheel file from here

📋 Requirements

    Python 3.7+
    Windows 10/11 (or Linux with PulseAudio)
    Internet connection (for Google Speech API)
    Stereo Mix enabled

🛠️ Linux Setup

Bash

# Install dependencies
sudo apt-get install portaudio19-dev python3-pyaudio

# Enable audio loopback
pactl load-module module-loopback

# Run with sudo
sudo python3 spelling_bee_bot.py

📝 What You'll Learn

    Audio capture with PyAudio
    Speech recognition with Google API
    Keyboard automation
    Event-driven programming with hotkeys

⚖️ Legal Notice

Using this bot:

    ❌ Violates Roblox Terms of Service
    ❌ Can get you permanently banned
    ❌ Is unfair to other players
    ✅ Is okay for learning Python
    ✅ Is okay in private test environments

Use responsibly. Don't ruin the game for others.
📄 License

MIT License - Free to use for educational purposes
