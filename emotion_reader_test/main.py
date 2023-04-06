#import pyautogui as pg
import emoji as emj
#import sys 
from colorama import Fore 
import pyttsx3
from emotion import emoji_emotion
import random
from ordered_set import OrderedSet

with open('emotion_reader_test/text.txt','w',encoding="utf-8") as f:
    w=input('Enter your message-')
    emj_cnt=emj.emoji_count(w)
    w=emj.demojize(w)


    f.writelines(w)
    f.close()


with open('emotion_reader_test/text.txt') as r:
    data=r.read()
    data_reading=emj.emojize(data)


    obj=emoji_emotion.emj_emo #object for all emoji hash mapped
    list_emotion=[]
    for i in data_reading: 
        if emj.is_emoji(i)==True:
            list_emotion.append(i)



    
    str_emotion=["The person is feeling- "]
    for j in OrderedSet(list_emotion): #unique orderset of emojies from list 
        emo_val=random.choice(obj.get(j)) #emoji feelings from the list
        str_emotion.append(emo_val+",")


    print(Fore.LIGHTGREEN_EX+data_reading+Fore.RESET)
    
    for emo in str_emotion:
        print(Fore.LIGHTBLACK_EX+emo,end=" "+Fore.RESET)


    read=data.replace("_",' ')

    
    Engine=pyttsx3.init() #init for module pyttsx3
    Engine.say(read) #avoid saying underscore. NOTE- If user meant to put underscore? email_id: etc.
    if emj_cnt!=0:
        Engine.say(str_emotion)
    else:
        Engine.say("The person is feeling nothing, try reading text messages ")
    Engine.runAndWait()





