import requests, re
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

url = "http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/sphinxdict/cmudict.0.7a_SPHINX_40"
rq = requests.get(url)
r1 = rq.text

phonemes = {
    "AA" : "ɑ",
    "AE" : "æ",
    "AH" : "ʌ",
    "AW" : "aʊ",
    "AY" : "aɪ",
    "B"  : "b",
    "CH" : "tʃ",
    "D"  : "d",
    "DH" : "ð",
    "EH" : "ɛ",
    "ER" : "ɝ",
    "EY" : "eɪ",
    "F"  : "f",
    "G"  : "ɡ",
    "HH" : "h",
    "IH" : "ɪ",
    "IY" : "i",
    "JH" : "dʒ",
    "K"  : "k",
    "L"  : "l",
    "M"  : "m",
    "N"  : "n",
    "NG" : "ŋ",
    "OW" : "oʊ",
    "OY" : "ɔɪ",
    "P"  : "p",
    "R"  : "ɹ",
    "S"  : "s",
    "SH" : "ʃ",
    "T"  : "t",
    "TH" : "θ",
    "UH" : "ʊ",
    "UW" : "u",
    "V"  : "v",
    "W"  : "w",
    "Y"  : "j",
    "Z"  : "z",
    "ZH" : "ʒ",}

print("speak")

with mic as source:
    #r.adjust_for_ambient_noise(source, duration = 0.5)
    audio = r.listen(source)

print("recognizing")

query = r.recognize_google(audio)
print(query)

##DO NOT DELETE ANYTHING ABOVE THIS LINE##

word = re.search(query.upper(), r1)
word2 = word.split()
word3 = [phonemes[p] for p in word2]
print(word)
