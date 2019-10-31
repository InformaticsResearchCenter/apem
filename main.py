import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK ANYTHING")
    audio = r.listen(source)
    
    try:
        print("YOU SAY :" + r.recognize_google(audio, language = 'id-ID'))#3
    except Exception as e:
        print(e)

print("TIME OVER, THANK YOU")