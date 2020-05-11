import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
# If you prefer to use environment variables, see Extra Credit for more info.
subscription_key = 'YOUR_TRANSLATOR_TEXT_SUBSCRIPTION_KEY'

# Don't forget to replace with your Cog Services location!
# Our Flask route will supply two arguments: text_input and language_output.
# When the translate text button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.
#instead of text_input -> get audio input
#no need of langauge output for now, but can keep it for later use

def get_translation(text_input, language_output):


    """
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'location',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    """

    # Here I add my code of STT and try to jsonify the transcribed text output
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something to Google STT')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print('Google thinks you said:\n' + r.recognize_google(audio))
        response = r.recognize_google(audio)


    ##return response.json()
    return response