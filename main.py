# Start

# Dependencies
from asyncio import SendfileNotAvailableError
import speech_recognition as sr 
import yagmail 

# Encrypting the email address and password
from decouple import config
EMAIL_ADDRESS = config('emailAddress')
EMAIL_PASSWORD = config('emailPassword')

# creating an instance for speechRecognition 
recognizer = sr.Recognizer() 

# Setting source for real time input > Microphone 
with sr.Microphone() as source: 
    print('Clearing the background noise for clear recognition !')
    
    # Clearing background noise in input sound
    recognizer.adjust_for_ambient_noise(source, duration=5)
    print('Waiting for your message >>> ')
    
    # Recording your audio
    recordedAudio = recognizer.listen(source)
    print('Recording is done !')
    print('Your recording is done !')
    
    # Try Block
    try: 
        print('Printing your recorded message >>> ')
        text = recognizer.recognize_google(recordedAudio, language='en-US')
        
        # Converting recorded audio into text > Language = English 
        print('Your recorded message is > {}'.format(text))
        
    except Exception as ex: 
        print(ex)
        

# Sending email        

# Setting RECIEVER's email address
reciever = EMAIL_ADDRESS

#Setting the recorded text as email body
message = text

# Setting SENDER's email address
sender = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Sending the email now
sender.send(to=reciever, subject='Voice assisted message !', contents=message)

# End