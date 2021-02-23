import requests, re, json           #Built in Python modules
import speech_recognition as sr     #Module SpeechRecognizer
recognize = sr.Recognizer()
mic = sr.Microphone()

phonemes = {
    "AA0": "ɑ",
    "AA1": "ˈɑ",
    "AA2": "ˌɑ",
    "AE0" : "æ",
    "AE1" : "ˈæ",
    "AE2" : "ˌæ",
    "AH0" : "ʌ",
    "AH1" : "ˈʌ",
    "AH2" : "ˌʌ",
    "AW0" : "aʊ",
    "AW1" : "ˈaʊ",
    "AW2" : "ˌaʊ",
    "AY0" : "aɪ",
    "AY1" : "ˈaɪ",
    "AY2" : "ˌaɪ",
    "B"  : "b",
    "CH" : "tʃ",
    "D"  : "d",
    "DH" : "ð",
    "EH" : "ɛ",
    "EH1" : "ˈɛ",
    "EH2" : "ˌɛ",
    "ER0" : "ɝ",
    "ER1" : "ˈɝ",
    "ER2" : "ˌɝ",
    "EY" : "eɪ",
    "EY1" : "ˈeɪ",
    "EY2" : "ˌeɪ",
    "F"  : "f",
    "G"  : "ɡ",
    "HH" : "h",
    "IH0" : "ɪ",
    "IH1" : "ˈɪ",
    "IH2" : "ˌɪ",
    "IY0" : "i",
    "IY1" : "ˈi",
    "IY2" : "ˌi",
    "JH" : "dʒ",
    "K"  : "k",
    "L"  : "l",
    "M"  : "m",
    "N"  : "n",
    "NG" : "ŋ",
    "OW0" : "oʊ",
    "OW1" : "ˈoʊ",
    "OW2" : "ˌoʊ",
    "OY0" : "ɔɪ",
    "OY1" : "ˈɔɪ",
    "OY2" : "ˌɔɪ",
    "P"  : "p",
    "R"  : "ɹ",
    "S"  : "s",
    "SH" : "ʃ",
    "T"  : "t",
    "TH" : "θ",
    "UH0" : "ʊ",
    "UH1" : "ˈʊ",
    "UH2" : "ˌʊ",
    "UW0" : "u",
    "UW1" : "ˈu",
    "UW2" : "ˌu",
    "V"  : "v",
    "W"  : "w",
    "Y"  : "j",
    "Z"  : "z",
    "ZH" : "ʒ",}

def encode(word):
    word2 = word.split()
    word3 = [phonemes[p] for p in word2]
    word4 = ''.join(word3)
    print(f"\n{word4}")

url = 'https://raw.githubusercontent.com/bschapp/English-Speech-to-IPA/main/CMU_DICT.json'
r = requests.get(url)

response_dict = r.json()

with open("CMU_DICT.json",'w') as f:
    json.dump(response_dict, f, indent = 4)

filename = 'CMU_DICT.json'

with open(filename) as f:
    cmu_dict_data = json.load(f)

print("speak")

with mic as source:
    #r.adjust_for_ambient_noise(source, duration = 0.5)
    audio = recognize.listen(source)

print("recognizing")

query = recognize.recognize_google(audio)
print(query)
rabbit = cmu_dict_data[query.upper()]
translation = encode(rabbit)
