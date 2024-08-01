from gtts import gTTS
import os   #we are importing the os module in order to open the program which will help to play the audio

'''
Conversion of the text to speech code
text = "Today is a very good day"
output = gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')

os.system("start output.mp3")

'''
text = open('demo.txt','r').read()

language = 'en'   #we can also use any other languages as well whose codes we can get from the google speech language code by doing google search
output = gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp3')
os.system("start fileoutput.mp3")