import tkinter as tk
import speech_recognition as sr
import requests, json

root = tk.Tk()
#root.geometry("250x500")

## MISC. DEFINITIONS ##########################################################
word_var = tk.StringVar()
recognize = sr.Recognizer()
mic = sr.Microphone()

phonemes = {
    ## VOWELS ##
    "AA0": "ɑ",     "AA1": "ˈɑ",    "AA2": "ˌɑ",
    "AE0" : "æ",    "AE1" : "ˈæ",   "AE2" : "ˌæ",
    "AH0" : "ʌ",    "AH1" : "ˈʌ",   "AH2" : "ˌʌ",
    "AO0" : "ɔ",    "AO1" : "ˈɔ",   "AO2" : "ˌɔ",
    "AW0" : "aʊ",   "AW1" : "ˈaʊ",  "AW2" : "ˌaʊ",
    "AY0" : "aɪ",   "AY1" : "ˈaɪ",  "AY2" : "ˌaɪ",
    "EH0" : "ɛ",    "EH1" : "ˈɛ",   "EH2" : "ˌɛ",
    "ER0" : "ɝ",    "ER1" : "ˈɝ",   "ER2" : "ˌɝ",
    "EY0" : "eɪ",   "EY1" : "ˈeɪ",  "EY2" : "ˌeɪ",
    "IH0" : "ɪ",    "IH1" : "ˈɪ",   "IH2" : "ˌɪ",
    "IY0" : "i",    "IY1" : "ˈi",   "IY2" : "ˌi",
    "OW0" : "oʊ",   "OW1" : "ˈoʊ",  "OW2" : "ˌoʊ",
    "OY0" : "ɔɪ",   "OY1" : "ˈɔɪ",  "OY2" : "ˌɔɪ",
    "UH0" : "ʊ",    "UH1" : "ˈʊ",   "UH2" : "ˌʊ",
    "UW0" : "u",    "UW1" : "ˈu",   "UW2" : "ˌu",
    ## CONSONANTS ##
    "B"  : "b",     "CH" : "tʃ",    "D"  : "d",
    "DH" : "ð",     "F"  : "f",     "G"  : "ɡ",
    "HH" : "h",     "JH" : "dʒ",    "K"  : "k",
    "L"  : "l",     "M"  : "m",     "N"  : "n",
    "NG" : "ŋ",     "P"  : "p",     "R"  : "ɹ",
    "S"  : "s",     "SH" : "ʃ",     "T"  : "t",
    "TH" : "θ",     "V"  : "v",     "W"  : "w",
    "Y"  : "j",     "Z"  : "z",     "ZH" : "ʒ",}
###############################################################################

## RETRIEVE CMU PRONOUNCIATION DICTIONARY DATA #################################
url = "https://raw.githubusercontent.com/bschapp/English-Speech-to-IPA/main/CMU_DICT.json"
r = requests.get(url)

response_dict = r.json()

with open("CMU_DICT.json",'w') as f:
    json.dump(response_dict, f, indent = 4)

filename = 'CMU_DICT.json'

with open(filename) as f:
    cmu_dict_data = json.load(f)
###############################################################################

## DEFINE FUNCTIONS ###########################################################
def translate():
    word = word_var.get()
    query = cmu_dict_data[word.upper()]
    wordSplit = query.split()
    wordPhone = [phonemes[p] for p in wordSplit]
    wordJoin  = f"/{''.join(wordPhone)}/"

    txt1.delete(1.0, float(len(word)))
    txt1.insert(1.0, word.lower())
    txt2.delete(1.0, float(len(word)))
    txt2.insert(1.0, wordJoin.lower())
    word_var.set("")

def Vtranslate():
    with mic as source:
        audio = recognize.listen(source)
        query = recognize.recognize_google(audio)
        word = query
        query = cmu_dict_data[query.upper()]
        wordSplit = query.split()
        wordPhone = [phonemes[p] for p in wordSplit]
        wordJoin  = f"/{''.join(wordPhone)}/"

        txt1.delete(1.0, float(len(word)))
        txt1.insert(1.0, word.lower())
        txt2.delete(1.0, float(len(query)))
        txt2.insert(1.0, wordJoin.lower())
        word_var.set("")

###############################################################################

## SET UP WIDGETS #############################################################
txt1 = tk.Text(root, height = 3, width = 20)
txt1.config(font = ("Verdana", 20))
txt2 = tk.Text(root, height = 3, width = 20)
txt2.config(font = ("Verdana", 20))

lbl1 = tk.Label(root, text = "English")
lbl1.config(font = ("Verdana", 14))
lbl2 = tk.Label(root, text = "IPA")
lbl2.config(font = ("Verdand", 14))

ent1 = tk.Entry(root, textvariable = word_var, width = 20, font = ("Verdana", 10))

btn1 = tk.Button(root, text = "Exit",       command = root.destroy,
    height = 2, width = 20)
btn2 = tk.Button(root, text = "Translate!", command = translate,
     height = 2, width = 20)
btn3 = tk.Button(root, text = "Speak!", command = Vtranslate,
    height = 2, width = 20)
###############################################################################

## PLACE WIDGETS ##############################################################
lbl1.grid(row = 0, column = 1, columnspan = 2, pady = 2)
txt1.grid(row = 1, column = 1, columnspan = 2, pady = 1)
lbl2.grid(row = 2, column = 1, columnspan = 2, pady = 1)
txt2.grid(row = 3, column = 1, columnspan = 2, pady = 1)
ent1.grid(row = 4, column = 1, columnspan = 2, pady = 1)
btn3.grid(row = 5, column = 1, pady = 1)
btn2.grid(row = 5, column = 2, pady = 1)
btn1.grid(row = 6, column = 1, columnspan = 2, pady = 1)
###############################################################################

root.mainloop()
