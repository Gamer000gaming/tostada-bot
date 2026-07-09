import random
import requests
import urllib.parse
from time import sleep
import json

supportedLangs = ["af","sq","am","ar","hy","az","eu","bn","bs","bg","ca","ceb","zh-CN","zh-TW","co","hr","cs","da","nl","en","eo","et","fi","fr","fy","gl","ka","de","el","gu","ht","ha","haw","iw","hi","hmn","hu","is","id","ga","ja","jw","kn","kk","km","ko","ku","lo","lv","lt","lb","mk","mg","ms","ml","mt","mi","mr","mn","ne","no","ny","ps","fa","pl","pt","pa","ro","ru","sm","gd","sr","st","sn","sd","si","sk","sl","so","es","sw","sv","tl","tg","ta","te","th","tr","uk","ur","uz","vi","cy","xh","yi","yo","zu"]

def translate(text, sourceLang, targetLang):
   try:
      url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl={targetLang}&dt=t&q={urllib.parse.quote(text)}"
      r = requests.get(url)
      formatted = r.json()[0]
      realText = ""
      for line in formatted:
         realText += line[0]
      return realText
   except Exception:
      # something happened, try again (likely a ratelimit)
      sleep(5)
      return translate(text, sourceLang, targetLang)

def hypertranslate(text, startLang, endLang, count):
   path = []
   oldLang = startLang
   for i in range(count - 1):
      newLang = random.choice(supportedLangs)
      text = translate(text, oldLang, newLang)
      oldLang = newLang
      path.append(newLang)
   text = translate(text, oldLang, endLang)
   path.append(endLang)
   return {"text": text, "path": path}
