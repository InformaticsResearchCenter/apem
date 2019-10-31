import speech_recognition as sr 
r=sr.Recognizer() 
with sr.Microphone() as source: #penyelesaian issues #8
    print("SPEAK ANYTHING")
    audio = r.listen(source)
    
    try:
        print("YOU SAY :" + r.recognize_google(audio, language = 'id-ID'))
    except Exception as e:
        print(e)

print("TIME OVER, THANK YOU")