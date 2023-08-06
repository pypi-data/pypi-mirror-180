#vaaninlp
#developed by neechalkaran@gmail.com

import regex
import requests 
import os
import dateutil.parser
import xml.etree.ElementTree as ET

def char_tokenize(text):
  chars = regex.findall(r"\p{L}\p{M}*",text)
  return chars

def word_tokenize(text):
  words = regex.findall("[ஂ-௺]+",text)
  return words

#get APIkey from https://vaanieditor.com for advance results.
def spellcheck(words, Vaani_api=""):
  URL = "http://vaani.neechalkaran.com/spellcheck"
  if(Vaani_api!=""):
    URL = "https://vaanieditor.com/SpellCheck.asmx/TamilSpellCheck"
    r = requests.post(url = URL, data={"tamilwords":"|".join(words),"sandhi":"true","translated":"true","unicode_error":"true","colloquial":"true","apikey":Vaani_api})   
    #print(r.text)
    data = __parseXmlToJson(ET.fromstring(r.text))
  else:
    r = requests.post(url = URL, data={"tamilwords":"|".join(words),"sandhi":"true","translated":"true","unicode_error":"true","colloquial":"true","apikey":Vaani_api})   
    data=r.json()
  return(data)

def lemmatize(words):
  URL = "http://vaani.neechalkaran.com/v2/parse"
  r = requests.post(url = URL, data={"tamilwords":"|".join(words)})
  data = r.json() 
  for i in range(len(data)):
    for j in range(len(data[i]["RootWords"])):
      data[i]["RootWords"][j]=data[i]["RootWords"][j].split("+")[0]
  return(data)

def delemmatize(word,suffix):
  URL = "http://vaani.neechalkaran.com/v2/build"
  r = requests.post(url = URL, data={"tamilwords":word+"|"+suffix})
  data = r.json() 
  return(data)

def sort(words):  
  words.sort(key=lambda b: __weight(b))
  return (words)
def __weight(a):
  map="அஆஇஈஉஊஎஏஐஒஓஔஔஃகஙசஞடணதநபமயரலவழளறனஜஶஷஸஹௐ"
  result=0
  for i in range(len(a)):
    index=map.find(a[i])
    if(index<0):
      index=ord(a[i])-2946
      if(index>99):index=0 
    result=result+(index/(100**i))
  return result

def remove_stopwords(words):
  stop_words_list = open(os.path.dirname(os.path.abspath(__file__))+"/stop_words.txt", "r").read().split("\n")
  new_words =[]
  for i in words:
    if i not in stop_words_list:
        new_words.append(i)
  return(new_words)


def get_entities(words):
  URL = "http://vaani.neechalkaran.com/v2/ner"
  r = requests.post(url = URL, data={"tamilwords":"|".join(words)})
  data = r.json() 
  entity=[]
  for i in data:
    for j in range(len(i["NERWords"])):
      if(i["Solspan"]>0):
        entity.append(i["NERWords"][j].split("+")[0])
    #print(i)
  return(entity)

def get_roots(words):
  URL = "http://vaani.neechalkaran.com/v2/parse"
  r = requests.post(url = URL, data={"tamilwords":"|".join(words)})
  data = r.json() 
  roots=[]
  for i in data:
    for j in range(len(i["RootWords"])):
      if(i["Flag"]==True):
        roots.append(i["RootWords"][j].split("+")[0])
  return(roots)
  
def date_string(dvalue):
  if (isfloat(dvalue)): return dvalue
  tmonth="ஜனவரி,பிப்ரவரி,மார்ச்,ஏப்ரல்,மே,ஜூன்,ஜூலை,ஆகஸ்ட்,செப்டம்பர்,அக்டோபர்,நவம்பர்,டிசம்பர்".split(',')
  tvalue=dvalue

  try:
    frame = dateutil.parser.parse(dvalue)
  except :
    return dvalue
  tvalue = str(frame.year) +" "+ tmonth[int(frame.month)-1] +" "+ str(frame.day)   
  return tvalue

def char_ngram(text, size): 
  ngrams = [];
  words = regex.findall("[ஂ-௺]+",text)
  for a in range(len(words)):
    chars = regex.findall(r"\p{L}\p{M}*",words[a])   
  
    for b in range(len(chars)-(size-1)):
      gram=""
      for c in range(size):
        gram=gram+chars[b+c]
      ngrams.append(gram);
  return ngrams

def isfloat(str):
  try: 
    float(str)
  except ValueError: 
    return False
  return True


def unicode_clean(c):
  c=regex.sub("([ா-்])([ ]+|)([ா-்])", lambda x: x.group(1)+x.group(3) ,c)#to remove space
  c=regex.sub("ொ([ா-்])", lambda x: "ெர" + x.group(1) ,c)
  c=regex.sub("ோ([ா-்])", lambda x: "ேர" + x.group(1) ,c)
  c=regex.sub("ரா([ா-்])", lambda x: "ார" + x.group(1) ,c)
  c=regex.sub("ா([ா-்])", lambda x: "ர" + x.group(1) ,c)
  c=regex.sub("ௌ([ா-்])", lambda x: "ெள" + x.group(1) ,c)
  c=regex.sub("ஔ([ா-்])", lambda x: "ஒள" + x.group(1) ,c)
  c=regex.sub(" ([ா-்])", lambda x: x.group(1) ,c)#a=a.replace(/ ீ/gi,"ீ")
  c=c.replace("்்","்")
  c=c.replace("ைை","ை")
  c=c.replace("ெெ","ெ")
  c=c.replace("ேே","ே")
  c=c.replace("ெ"+"ா", "ொ")
  c=c.replace("ே"+"ா", "ோ")
  c=regex.sub("([நறலதணஞன])ுா", lambda x: x.group(1)+"ூ" ,c)
  return c


def convert_prosody(c):
  #https://en.wikipedia.org/wiki/Prosodic_unit
    #return நேர் | /நிரை ‖
  c=unicode_clean(c)
  c=regex.sub("([க-ஹ]்|ஃ)", "0" ,c) #removing all ottru prior to avoid regexp issue
  c=regex.sub("([ஂ-௺])([க-ஹ])ை", lambda x: x.group(1)+x.group(2) ,c) 
  c=regex.sub("([ஂ-௺])([க-ஹ])ௌ", lambda x: x.group(1)+x.group(2) ,c)
  c=regex.sub("[அஇஉஎஒக-ஹ]([ிுெொ]|)[க-ஹ]([ா-ௌ]|)", "‖" ,c)
  c=regex.sub("[அ-ஔக-ஹ]([ா-ௌ]|)", "|" ,c)
  c=c.replace("0","")
  c=regex.sub("\s"," ",c)
  c=regex.sub("[ ]+", " ",c)
  return c  


def __parseXmlToJson(xml):
  response = []  
  for child in list(xml):
    sol={}
    for children in list(child):
      tag= (children.tag).replace("{https://vaanieditor.com/}","")
      sol[tag]=children.text
    response.append(sol)
  return response
