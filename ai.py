from playsound import playsound
import speech_recognition as speech
from gtts import gTTS
import os

FILE_NAME = "speech"
file_num = 1
KEYWORD = "jarvis"

RECOGNIZER = speech.Recognizer()

def main():
    
    result = listen().lower()
    
    while "stop" not in result:
        
        if KEYWORD in result:
            say = result
            
            if "are you there" in result:
                say = "yes I am"
            
            speak(say.replace(KEYWORD, ''))
            
        result = listen().lower()
        
        
def listen():
    
    result = "stop"
    
    with speech.Microphone() as source:
        audio = RECOGNIZER.listen(source)
        
    try:
        result = RECOGNIZER.recognize_google(audio)
    except speech.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except TypeError:
        print("Type error")
        
    return result

def speak(phrase):
    global file_num
    
    new_name = FILE_NAME + str(file_num) + ".mp3"
    
    text_to_speech = gTTS(phrase)
    text_to_speech.save(new_name)
    
    try:
        playsound(new_name)
    except FileNotFoundError:
        print("Failed to play audio '" + new_name + "'")
        
    os.remove(new_name)
    file_num += 1
    
if __name__ == "__main__":
    main()


