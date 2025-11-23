"""
Roblox Spelling Bee Audio Bot
Automates the Spelling Bee game by recording audio, transcribing it, and typing the answer.

DISCLAIMER: For educational purposes only. Using bots in Roblox violates ToS.

Requirements:
    pip install pyaudio SpeechRecognition keyboard pynput
"""

import pyaudio
import wave
import speech_recognition as sr
import keyboard
import time
import random
from pynput.keyboard import Key, Listener

# Global flag to control program execution
running = True


# ============================================================================
# SECTION 1: AUDIO DEVICE DISCOVERY
# ============================================================================

def find_stereo_mix_device():
    """
    Discovers and lists all available audio input devices.
    Helps identify the Stereo Mix device index.

    Returns:
        int: Suggested device index for Stereo Mix (or None if not found)
    """
    p = pyaudio.PyAudio()
    print("\n" + "=" * 70)
    print("AVAILABLE AUDIO DEVICES:")
    print("=" * 70)

    stereo_mix_index = None

    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        device_name = device_info.get('name')
        max_input_channels = device_info.get('maxInputChannels')

        # Display all devices
        print(f"Device {i}: {device_name}")
        print(f"  Input Channels: {max_input_channels}")
        print(f"  Sample Rate: {int(device_info.get('defaultSampleRate'))}")

        # Try to identify Stereo Mix
        if max_input_channels > 0:
            name_lower = device_name.lower()
            if any(keyword in name_lower for keyword in ['stereo mix', 'wave out', 'loopback', 'what u hear']):
                stereo_mix_index = i
                print(f"  ✓ POTENTIAL STEREO MIX DEVICE FOUND!")

        print()

    p.terminate()

    if stereo_mix_index is not None:
        print(f"Suggested Stereo Mix device index: {stereo_mix_index}")
    else:
        print("⚠ Could not auto-detect Stereo Mix. Please enable it in Windows Sound settings.")
        print("  Control Panel → Sound → Recording → Enable 'Stereo Mix'")

    print("=" * 70 + "\n")
    return stereo_mix_index


# ============================================================================
# SECTION 2: AUDIO RECORDING
# ============================================================================

def record_audio(duration=5, device_index=None, output_filename="desktop_audio.wav"):
    """
    Records desktop audio using PyAudio from Stereo Mix device.

    Args:
        duration (int): Recording duration in seconds
        device_index (int): Audio device index (Stereo Mix)
        output_filename (str): Output WAV file path

    Returns:
        str: Path to recorded file, or None if failed
    """
    # Audio recording parameters
    CHUNK = 1024  # Buffer size
    FORMAT = pyaudio.paInt16  # 16-bit audio
    CHANNELS = 2  # Stereo
    RATE = 44100  # Sample rate (44.1kHz)

    print(f"\n🎤 Starting audio recording for {duration} seconds...")

    p = pyaudio.PyAudio()

    try:
        # Open audio stream from specified device
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index=device_index,
            frames_per_buffer=CHUNK
        )

        print("🔴 RECORDING...")
        frames = []

        # Record audio in chunks
        for i in range(0, int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)

        print("⏹ Recording complete!")

        # Stop and close stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save recording as WAV file
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        print(f"💾 Saved to: {output_filename}")
        return output_filename

    except OSError as e:
        print(f"❌ ERROR: Could not access audio device {device_index}")
        print(f"   {str(e)}")
        print("\n💡 Try running find_stereo_mix_device() to find the correct device index")
        print("   Or enable Stereo Mix in Windows Sound settings")
        p.terminate()
        return None

    except Exception as e:
        print(f"❌ Unexpected error during recording: {str(e)}")
        p.terminate()
        return None


# ============================================================================
# SECTION 3: SPEECH RECOGNITION
# ============================================================================

def transcribe_audio(filename="desktop_audio.wav"):
    """
    Transcribes audio file to text using Google Speech Recognition.
    Extracts the last word (handles "please spell [word]" format).

    Args:
        filename (str): Path to WAV audio file

    Returns:
        str: The last word from transcription, or None if failed
    """
    recognizer = sr.Recognizer()

    print("\n🎯 Transcribing audio...")

    try:
        # Load audio file
        with sr.AudioFile(filename) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Record audio data
            audio_data = recognizer.record(source)

        # Perform speech recognition using Google API
        print("🔍 Using Google Speech Recognition...")
        text = recognizer.recognize_google(audio_data)

        print(f"📝 Transcribed: '{text}'")

        # Extract last word (the word to spell)
        words = text.strip().split()
        if words:
            target_word = words[-1].strip('.,!?')  # Remove punctuation
            print(f"✓ Target word: '{target_word}'")
            return target_word
        else:
            print("⚠ No words detected in transcription")
            return None

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None

    except sr.RequestError as e:
        print(f"❌ Could not request results from Google Speech Recognition service")
        print(f"   Error: {e}")
        return None

    except FileNotFoundError:
        print(f"❌ Audio file not found: {filename}")
        return None

    except Exception as e:
        print(f"❌ Unexpected error during transcription: {str(e)}")
        return None


# ============================================================================
# SECTION 4: KEYBOARD AUTOMATION
# ============================================================================

def type_word(word):
    """
    Types the given word with human-like randomized delays.
    Simulates natural typing patterns.

    Args:
        word (str): The word to type
    """
    if not word:
        print("⚠ No word to type")
        return

    print(f"\n⌨️  Typing: '{word}'")

    # Wait before starting to type (simulate human reaction time)
    time.sleep(random.uniform(0.3, 0.6))

    # Type each character with random delay
    for char in word:
        keyboard.write(char)
        # Random delay between keystrokes (65ms to 290ms)
        delay = random.uniform(0.065, 0.29)
        time.sleep(delay)

    # Small pause before pressing Enter
    time.sleep(random.uniform(0.1, 0.3))

    # Press Enter to submit
    keyboard.press_and_release('enter')
    print("✓ Word typed and submitted!")


# ============================================================================
# SECTION 5: KEYBOARD LISTENER (HOTKEYS)
# ============================================================================

def on_press(key):
    """
    Callback function for keyboard events.

    Controls:
        - Left/Right Control: Start recording and processing
        - Escape: Exit program

    Args:
        key: The key that was pressed
    """
    global running

    try:
        # Check if Control key is pressed (either left or right)
        if key == Key.ctrl_l or key == Key.ctrl_r:
            print("\n" + "=" * 70)
            print("🚀 CONTROL KEY PRESSED - STARTING PROCESS")
            print("=" * 70)

            # Execute the full workflow
            execute_workflow()

        # Check if Escape key is pressed
        elif key == Key.esc:
            print("\n" + "=" * 70)
            print("🛑 ESCAPE KEY PRESSED - EXITING PROGRAM")
            print("=" * 70)
            running = False
            return False  # Stop listener

    except AttributeError:
        # Handle special keys that don't have char attribute
        pass


# ============================================================================
# SECTION 6: MAIN WORKFLOW
# ============================================================================

def execute_workflow(device_index=None):
    """
    Executes the complete workflow: Record → Transcribe → Type

    Args:
        device_index (int): Audio device index for Stereo Mix
    """
    # Step 1: Record audio
    audio_file = record_audio(duration=5, device_index=device_index)

    if audio_file is None:
        print("⚠ Recording failed. Aborting workflow.")
        return

    # Small delay between recording and transcription
    time.sleep(0.5)

    # Step 2: Transcribe audio
    word = transcribe_audio(audio_file)

    if word is None:
        print("⚠ Transcription failed. Aborting workflow.")
        return

    # Small delay before typing
    time.sleep(0.3)

    # Step 3: Type the word
    type_word(word)

    print("\n✅ Workflow complete!\n")


# ============================================================================
# SECTION 7: MAIN PROGRAM
# ============================================================================

def main():
    """
    Main program entry point.
    Sets up keyboard listener and handles program flow.
    """
    global running

    print("\n" + "=" * 70)
    print(" ROBLOX SPELLING BEE AUDIO BOT")
    print("=" * 70)
    print("\n⚠️  DISCLAIMER: For educational purposes only!")
    print("   Using bots in Roblox violates Terms of Service.\n")

    # Discover audio devices
    print("Step 1: Discovering audio devices...")
    suggested_device = find_stereo_mix_device()

    # Ask user for device index
    print("\nEnter the Stereo Mix device index")
    if suggested_device is not None:
        print(f"(Press Enter to use suggested index {suggested_device}): ", end='')
    else:
        print("(or press Enter to auto-detect): ", end='')

    user_input = input().strip()

    if user_input:
        device_index = int(user_input)
    elif suggested_device is not None:
        device_index = suggested_device
    else:
        device_index = None

    print(f"\n✓ Using device index: {device_index}")

    # Instructions
    print("\n" + "=" * 70)
    print("CONTROLS:")
    print("=" * 70)
    print("  CTRL (Left/Right) - Start recording and processing")
    print("  ESC               - Exit program")
    print("=" * 70)
    print("\n👂 Listening for keyboard inputs...\n")

    # Create keyboard listener with modified on_press to include device_index
    def on_press_with_device(key):
        global running
        try:
            if key == Key.ctrl_l or key == Key.ctrl_r:
                print("\n" + "=" * 70)
                print("🚀 CONTROL KEY PRESSED - STARTING PROCESS")
                print("=" * 70)
                execute_workflow(device_index=device_index)
            elif key == Key.esc:
                print("\n" + "=" * 70)
                print("🛑 ESCAPE KEY PRESSED - EXITING PROGRAM")
                print("=" * 70)
                running = False
                return False
        except AttributeError:
            pass

    # Start keyboard listener
    with Listener(on_press=on_press_with_device) as listener:
        listener.join()

    print("\n👋 Program terminated. Goodbye!\n")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Program interrupted by user (Ctrl+C)")
        print("👋 Goodbye!\n")
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        import traceback

        traceback.print_exc()
