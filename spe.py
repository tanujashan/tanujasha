import speech_recongnition as sr 

AUDIO_FILE = ("example2.wav")
# use the audio file as the audio source

r = sr.Recongizer()

with sr.AudioFile(AUDIO_FILE) as source:
    #reads the audio file. here we use record instead of 
    #listen 
	audio = r.record(source)

try:
	print("The audio file contains: " + r.recongize_google(audio))

except sr.UnKnownValueError:
	print("Google Speech Recongition could not understand audio")

except sr.RequestError as e:
	print("Could not request results from Google Speech Regonition service; {0}".format(e))
