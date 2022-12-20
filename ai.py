# imports
import speech_recognition as speech
import pyttsx3
from chatgpt_wrapper import ChatGPT

# apis
bot = ChatGPT()
speech_engine = pyttsx3.init()
RECOGNIZER = speech.Recognizer()

KEYWORD = "jarvis"

def main():
    
    result = listen().lower()
    
    # go until stopped
    while "stop" not in result:
        
        # if in result, we run the bot
        if KEYWORD in result:
            print("You said \"" + result + "\"")
            print("Thinking...")
            
            result = result.replace(KEYWORD, '')
            say = bot.ask(result) # get from chatGPT
            print(say)
            speak(say) # speak it
            
        # keep looping
        result = listen().lower()
    
    # stop or an error
    print("Stopping...")    
        
def listen():
    
    result = "stop"
    
    # Get from mic source
    with speech.Microphone() as source:
        RECOGNIZER.adjust_for_ambient_noise(source)
        
        # let user know
        print("Listening!")
        audio = RECOGNIZER.listen(source)
        
        # catch unrecognized input
        try:
            result = RECOGNIZER.recognize_google(audio)
        except speech.UnknownValueError:
            print("Error: Unknown value")
            
        return result
    
def speak(phrase):
    
    # simply just say and continue
    speech_engine.say(phrase)
    speech_engine.runAndWait()
    
if __name__ == "__main__":
    main()


