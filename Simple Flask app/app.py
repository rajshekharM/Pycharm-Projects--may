from flask import Flask, render_template, url_for, jsonify, request
import translate
import speech_recognition as sr

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something to Google STT')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        if(audio):
            text = r.recognize_google(audio)
            if(text):
                print('Google thinks you said:\n' + text)
                return render_template('template1.html', foobar=text)
            else:
                return render_template('template1.html', foobar="Please Press Button & Speak Again")
        else:
            return render_template('template1.html', foobar="Please Press Button & Speak Again")

if __name__ == '__main__':
    app.run(debug=True)

    ##response = translate.get_translation()





