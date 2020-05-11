import speech_recognition as sr

r = sr.Recognizer()

try:
    while True:

        with sr.Microphone() as source:
            print('Say something to Google STT')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            print('Google thinks you said:\n' + r.recognize_google(audio))


except KeyboardInterrupt:
    pass