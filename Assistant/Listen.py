import speech_recognition

bot_ear = speech_recognition.Recognizer();
with speech_recognition.Microphone() as mic:
    print("Bot: Hey, I'm Listening")
    audio = bot_ear.listen(mic)

try:
    you = bot_ear.recognize_google(audio)
except:
    you == ""
print("You:"+you)