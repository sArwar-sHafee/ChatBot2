print("\n\nPLEASE BE PATIENT. IT WOULD TAKE MORE THAN FEW SECONDS\n\n\n\n")

#..........................................................................................

import pygame
import pygame as pg
from pygame import mixer
import pyttsx3
import time
clock = pg.time.Clock()
pygame.init()
pg.init()
mixer.init()
friend = pyttsx3.init()
sound = friend.getProperty("voices")
friend.setProperty('voice', sound[1].id)


icon = pg.image.load("chatbotlogo2.png")
pg.display.set_icon(icon)

bg = pg.image.load("botbg2.jpg")

botimg = pg.image.load("chatbotlogo.png")
userimg = pg.image.load("userlogo.png")
userimg2 = pg.image.load("userlogo2.png")


botimage = pg.image.load("chatbot.jpeg")
chatimg = pg.image.load("chatbox.png")


#text = ''
#color = pg.Color('lightskyblue3')
#font = pg.font.Font(None, 32)

pg.display.set_caption('ChatBot')
scr = pg.display.set_mode([800, 670]) 


y_next = 0
then = 3
'''
font = pg.font.Font(None, 28)
input_box = pg.Rect(120, 600, 140, 32)
color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('dodgerblue2')
color = color_active
active = True
done = False
'''
text = ''

question = pg.font.SysFont('comicsansms', 20)
reply = pg.font.SysFont('comicsansms', 20)

your_text = ""
bot_reply = ""
flag = 0


myquestion = []
botanswer = []

def m_question():
    #for i in range(flag):
        myquestion.append(question.render(your_text, True, (0, 0, 0)))
        botanswer.append(reply.render(bot_reply, True, (0, 0, 0)))

text_ren = pg.font.SysFont('arial', 25)


#tx = []
#txs = ""
#def text_render():
#    tx.append(text_ren.render(text, True, (0, 0, 0)))
#.......................................................................................

        
#import view2
import tensorflow
import tflearn
import nltk
#from math import *

from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer() #makes word like running to run. Means take the root of the work 

import numpy
import json
import random

with open("all.json") as file:
    data = json.load(file)
    
import pickle
#print(data["intents"])
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
        if intent["tag"] not in labels:
            labels.append(intent["tag"])    

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x): # x is index number and doc is the item
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)
    
    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)


tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")
    
    
    
    
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)
answer = ""

def chat(req):
    #print("Say something!")
    #print("\n")
    #while True:
        #inp = input("You:   ")
        inp = req
        #if inp.lower() == "quit" or inp.lower() == "exit":
            #break

        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    answer = random.choice(responses)
                    #print("Robot:", answer)
        else:
            answer = "Sorry I did not get that!"
            #print("Robot: Sorry I did not get that! Please ask different question or same question in different way.")
            return answer
        #print("\n")
        return answer
#print("\n\n\n")        
#chat()    
    
    
    
#.....................................................................    
    
    
    

j = 1    
now = 1


run = True
while run:
    clock.tick(30)
    scr.blit(bg, (0, 70))
    scr.blit(botimage, (0 , 0)) 
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
                      
            
        #if event.type == pg.MOUSEBUTTONDOWN:
        if event.type == pg.KEYDOWN:
                #if active:
                if event.key == pg.K_RETURN:
                    '''try:
                        mixer.music.stop()
                    except:
                        pass'''
                    b_sound = mixer.Sound('swiftly2.wav')
                    b_sound.play()
                    your_text = text
                    #print(your_text)
                    bot_reply =chat(text)
                    
                    #print(":"+ bot_reply)
                    text = ''
                    s = text_ren.render(text, True, (0, 0, 0))
                    flag += 1
                    if flag > 10:
                        j += 1
                    m_question()
                    now = 1
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                    #text_render()
                    s = text_ren.render(text, True, (0, 0, 0))
                else:
                    text += event.unicode
                    #print(text)
                    #text_render()
                    s = text_ren.render(text, True, (0, 0, 0))
    try:            
        scr.blit(s, (130, 590))
    except:
        pass
    
    
    if flag < 10:
        y_next = 0
        for i in range(flag):
            scr.blit(userimg, (15, 85 + y_next))
            scr.blit(myquestion[i], (55, 85 + y_next))
            y_next += 55
        y_next = 0
        try:
            for i in range(flag-1):
                scr.blit(botimg, (15, 103 + y_next))
                scr.blit(botanswer[i], (55, 107 + y_next))
                y_next += 55
        except:
            pass
        if now == 1:
            pg.display.update()
            time.sleep(1)
        y_next = 0
        for i in range(flag):
                scr.blit(botimg, (15, 103 + y_next))
                scr.blit(botanswer[i], (55, 107 + y_next))
                y_next += 55
        if now == 1:
            pg.display.update()
            friend.say(bot_reply)
            friend.runAndWait()
            if bot_reply == "Ok. I'm playing my favourite band Imagine dragons song covered by j fla.":
                time.sleep(1)
                bs = mixer.Sound('botsong.wav')
                bs.play()
                #print("ok")
            if bot_reply == "stopping":
                try:
                    mixer.stop()
                except:
                    pass
            now = 0
            
            
            
    if flag >= 10:
        y_next = 0
        for i in range(flag-j):
            scr.blit(userimg, (15, 85 + y_next))
            scr.blit(myquestion[i+j], (55, 85 + y_next))
            y_next += 55
        y_next = 0
        try:
            for i in range(flag-j-1):
                scr.blit(botimg, (15, 103 + y_next))
                scr.blit(botanswer[i+j], (55, 107 + y_next))
                y_next += 55
        except:
            pass
        if now == 1:
            pg.display.update()
            time.sleep(1)
        y_next = 0
        for i in range(flag-j):
            scr.blit(botimg, (15, 103 + y_next))
            scr.blit(botanswer[i+j], (55, 107 + y_next))
            y_next += 55
        if now == 1:
            pg.display.update()
            friend.say(bot_reply)
            friend.runAndWait()
            if bot_reply == "Ok. I'm playing my favourite band Imagine dragons song covered by j fla.":
                time.sleep(1)
                bs = mixer.Sound('botsong.wav')
                bs.play()
                #print('ok')
            if bot_reply == "stopping":
                try:
                    mixer.stop()
                except:
                    pass
            now = 0
                
    

    
    scr.blit(userimg2, (75, 590))
    scr.blit(chatimg, (110, 590))                            
    #txt_surface = font.render(text, True, color)
    #width = max(600, txt_surface.get_width()+10)
    #input_box.w = width
    #scr.blit(txt_surface, (input_box.x+5, input_box.y+5))
    #pg.draw.rect(scr, color, input_box, 2)   
    pg.display.flip()
    
if run == False:
    pg.quit()


#..........................................................................
