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

    # x=[]
    # for i in data_reading.split(' '):
    #     x.append(i)
        

    # print(x)

    # for j in x:
    #     emoji=emj.emojize(j) 
    #     if emj.is_emoji(emoji)==True:
    #         pass

    obj=emoji_emotion.emj_emo #object for all emoji hash mapped
    list_emotion=[]
    for i in data_reading:
        if emj.is_emoji(i)==True:
            list_emotion.append(i)

    

    for j in list_emotion:
        str_emotion=""
        emoji=j
        str_emotion.join(obj.get(j))





    Engine=pyttsx3.init()
    print(data_reading)
    read=data.replace("_",' ')
    Engine.say(read) #should not say underscore bs WORKS :D 
   

    
    

    say_emotion=("Person is feeling "+random.choice(obj.get(emoji)))
    print(say_emotion)
    Engine.say(say_emotion)
    Engine.runAndWait()





