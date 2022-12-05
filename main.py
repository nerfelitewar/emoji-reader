from itertools import permutations , combinations
import pyautogui as pg
import emoji as emj
import sys 
import pyttsx3
from emotion import emoji_emotion
import random
from ordered_set import OrderedSet

with open('text.txt','w',encoding="utf-8") as f:
    w=input('Say ur msg- ')

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
    
    str_emotion=["The person is feeling "]
    for j in OrderedSet(list_emotion): #unique orderset of emojies from list 
        emo_val=random.choice(obj.get(j)) #emoji feelings from the list
        str_emotion.append(emo_val+" ")
    



    Engine=pyttsx3.init()
    print(data_reading)
    read=data.replace("_",' ')
    Engine.say(read) #avoid saying underscore. NOTE- If user meant to put underscore? email_id: etc.

    print(str_emotion)
    Engine.say(str_emotion)
    Engine.runAndWait()





