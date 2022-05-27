import pprint
import wikipedia
from gtts import gTTS
from bs4 import BeautifulSoup
from playsound import playsound

try:
    while True:
        q = wikipedia.search(str(input("Search: ")))
        r = wikipedia.summary(q[0], sentences=0, chars=0, auto_suggest=False, redirect=False)
        s = BeautifulSoup(r, 'html.parser')
        pprint.pprint(q[0])
        pprint.pprint(s.prettify().replace('\n', ''))
        v = gTTS(str(s))
        v.save('temp.mp3')
        playsound('temp.mp3')

except wikipedia.exceptions.DisambiguationError as error:
    print(error.options)
    pass
