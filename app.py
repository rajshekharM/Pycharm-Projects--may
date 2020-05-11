"""
A barebones Flask application to demonstrate the Google Speech API usage.
Install the requirements first:
`pip install SpeechRecognition flask`
Then just run this file, go to http://127.0.0.1:5000/
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)