import pyautogui as pg
import emoji as emj
import sys 
from colorama import Fore 
import pyttsx3
from emotion import emoji_emotion
import random
from ordered_set import OrderedSet

with open('text.txt','w',encoding="utf-8") as f:
    w=input('Enter your message-')

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

    ###print(list_emotion) #all emoji list in a txt file 
    #NOTE- Maybe i should use {} sets so that no repetition ^^^
    
    str_emotion=["The person is feeling-"]
    for j in OrderedSet(list_emotion): #unique orderset of emojies from list 
        emo_val=random.choice(obj.get(j)) #emoji feelings from the list
        str_emotion.append(emo_val+",")


    print(Fore.LIGHTRED_EX+data_reading+Fore.RESET)
    
    for emo in str_emotion:
        print(Fore.LIGHTBLACK_EX+emo,end=" "+Fore.RESET)


    read=data.replace("_",' ')

    
    Engine=pyttsx3.init() #init for module pyttsx3
    Engine.say(read) #avoid saying underscore. NOTE- If user meant to put underscore? email_id: etc.
    Engine.say(str_emotion)
    Engine.runAndWait()





