from itertools import permutations , combinations
import pyautogui as pg
import emoji as emj
import sys 
import pyttsx3
import random

with open('text.txt','w',encoding="utf-8") as f:
    w=input('Say ur msg- ')
    sys.stdout.reconfigure(encoding='utf-8')
    #w=pg.prompt("Say your msg",title="MSG")

    w=emj.demojize(w)


    f.writelines(w)
    f.close()


with open('text.txt') as r:
    data=r.read()
    data_reading=emj.emojize(data)
    Engine=pyttsx3.init()
    print(data_reading)

    data

    Engine.say(data)

    Engine.runAndWait()

    
    






