import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

bot_ear = speech_recognition.Recognizer();
bot_mouth = pyttsx3.init()
bot_brain =""

while True:
    with speech_recognition.Microphone() as mic:
        print("Bot: Hey, I'm Listening")
        audio = bot_ear.listen(mic)
    print("Bot ...")
    try:
        you = bot_ear.recognize_google(audio)
    except:
        you == ""
    print("You:"+you)


    if you == "":
        bot_brain = "Sorry, I can't here you."
    elif  "hello" in you:
        bot_brain = "Hello Bro!! Long time no see"
    elif "today" in you:
        today = date.today()
        bot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        bot_brain = now.strftime("%H:%M:%S")
    elif "bye" in you:
        bot_brain = " Bye, see you next time"
        print("Bot:"+ bot_brain)
        bot_mouth.say(bot_brain)
        bot_mouth.runAndWait()
        break
    else: 
        bot_brain = "I'm fine thanks"
    print("Bot:"+ bot_brain)
    bot_mouth.say(bot_brain)
    bot_mouth.runAndWait()