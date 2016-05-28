from subprocess import PIPE, call
import urllib

class Speech(object):
	
  def text_to_speech(self , text):
      try:
          #text = text[:100] code for testing
          #print(text)
          #query = urllib.quote_plus(text)
          
          endpoint = "http://translate.google.com/translate_tts?tl=en&q="+text+"&client=tw-ob"
          print(endpoint)
          call(["mplayer",endpoint], shell=False, stdout=PIPE, stderr=PIPE)
    except:
          print("error translating text")
