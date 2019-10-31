import speech_recognition as sr 
r=sr.Recognizer() 
with sr.Microphone() as source: 
    print("SPEAK ANYTHING")
    audio = r.listen(source)
    
    try:
        print("YOU SAY :" + r.recognize_google(audio, language = 'id-ID')) 
    except Exception as e: #penyelesaian issues #10
        print(e) #penyelesaian issues #10

print("TIME OVER, THANK YOU") #penyelesaian issues #10