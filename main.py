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


    obj=emoji_emotion.emj_emo #object for all emoji hash mapped
    list_emotion=[]
    for i in data_reading:
        if emj.is_emoji(i)==True:
            list_emotion.append(i)

    print(list_emotion) #all emoji list in a txt file 
    #NOTE- Maybe i should use {} sets so that no repetition ^^^
    
    str_emotion=[]
    for j in list_emotion:
        emo_val=random.choice(obj.get(j))
        str_emotion.append(emo_val)
    






        
    








    Engine=pyttsx3.init()
    print(data_reading)
    read=data.replace("_",' ')
    Engine.say(read) #should not say underscore bs WORKS :D 
   

    
    

    say_emotion=("Person is feeling ",str_emotion)
    print(say_emotion)
    Engine.say(say_emotion)
    Engine.runAndWait()





