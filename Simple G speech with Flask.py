#!/usr/bin/env python
"""
Simple Flask application to demonstrate the Google Speech API usage.
Install the requirements first:
`pip install SpeechRecognition flask`
Then just run this file, go to http://127.0.0.1:5000/
and upload an audio (or may be even video) file there, using the html form.
(I've tested it with a .wav file only - relying on Google here).
"""

import os
from flask import Flask, request, redirect, flash
from werkzeug.utils import secure_filename

import speech_recognition as sr

app = Flask(__name__)
##UPLOAD_FOLDER = "./"
##app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# You have 50 free calls per day, after that you have to register somewhere
# around here probably https://cloud.google.com/speech-to-text/
GOOGLE_SPEECH_API_KEY = None


@app.route("/", methods=["GET", "POST"])
def index():
    extra_line = ''
    if request.method == "POST":
        # Check if the post request has the file part.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say something to Google STT')
            r.listen(source)
            audio_file = r.adjust_for_ambient_noise(source)

        if audio_file:
            # Speech Recognition stuff.
            text = r.recognize_google(audio_file)
            extra_line = f'Speech to Text engine thinks you said: "{text}"'



    return f"""
    <!doctype html>
    <title>Upload new File</title>
    {extra_line}
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <p/>
      <input type=submit value=Upload>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True, threaded=True)