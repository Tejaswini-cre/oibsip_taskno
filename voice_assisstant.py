import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Initialize text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Capture voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()  # Return the command in lowercase for consistency
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be a network issue.")
            return ""

# Respond to recognized commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")

    elif "date" in command:
        today = datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "search" in command:
        speak("What would you like to search for?")
        query = get_voice_input()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the search results for {query}")

    else:
        speak("Sorry, I didn't understand the command. Can you please repeat it?")

# Main loop for the assistant
def run_voice_assistant():
    speak("Hi, I am your voice assistant. How can I help you?")
    while True:
        command = get_voice_input()
        if "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! Have a great day!")
            break
        respond_to_command(command)

# Run the assistant
if __name__== "_main_":
    run_voice_assistant()