from itertools import permutations , combinations
import pyautogui as pg
import emoji as emj
import sys 
import pyttsx3
from emotion import emoji_emotion
import random

with open('text.txt','w',encoding="utf-8") as f:
    w=input('Say ur msg- ')
    #sys.stdout.reconfigure(encoding='utf-8')
    #w=pg.prompt("Say your msg",title="MSG")

    w=emj.demojize(w)


    f.writelines(w)
    f.close()


with open('text.txt') as r:
    data=r.read()
    data_reading=emj.emojize(data)

    x=[]
    for i in data_reading.split(' '):
        x.append(i)
        

    print(x)

    for j in x:
        emoji=emj.emojize(j) 
        # list_emoji=[]   
        # for emoji in emoji: 
        #     e=emj.is_emoji(emoji)
        #     if e==True:
        #         list_emoji.append(e)
        # print(list_emoji)



    Engine=pyttsx3.init()
    print(data_reading)
    read=data.replace("_",' ')
    Engine.say(read) #should not say underscore bs WORKS :D 
   

    
    obj=emoji_emotion.emj_emo

    say_emotion=("Person is feeling "+random.choice(obj.get(emoji)))
    print(say_emotion)
    Engine.say(say_emotion)
    Engine.runAndWait()





