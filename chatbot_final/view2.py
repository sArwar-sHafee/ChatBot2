#import try2

import pygame as pg
#import math
#import random
from pygame import mixer
clock = pg.time.Clock()
pg.init()
mixer.init()


icon = pg.image.load("chatbotlogo2.png")
pg.display.set_icon(icon)

pg.display.set_caption('ChatBot')


bg = pg.image.load("botbg2.jpg")

botimg = pg.image.load("chatbotlogo.png")
userimg = pg.image.load("userlogo.png")
userimg2 = pg.image.load("userlogo2.png")


botimage = pg.image.load("chatbotbg.jpeg")

#text = ''
#color = pg.Color('lightskyblue3')
#font = pg.font.Font(None, 32)

scr = pg.display.set_mode([800, 670]) 

y_next = 0
then = 3

font = pg.font.Font(None, 28)
input_box = pg.Rect(120, 600, 140, 32)
color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('dodgerblue2')
color = color_active
active = True
text = ''
done = False

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

 
    
j = 1    
    
run_ing = True
while run_ing:
    #clock.tick(30)
    scr.blit(bg, (0, 70))
    #scr.fill([0,0,0])
    scr.blit(botimage, (0 , 0))
    pg.display.update()
    #for i in range(flag):    
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_ing = False
            
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                your_text = text
                #print(your_text)
                #bot_reply =try2.chat(text)
                bot_reply = ":)"
                #print(":"+ bot_reply)
                text = ''
                flag += 1
                if flag > 10:
                    j += 1
                m_question()
                b_sound = mixer.Sound('swiftly2.wav')
                b_sound.play()
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            else:
                #text += event.unicode
                text = 'a'
    
    y_next = 0
    if flag < 10:
        for i in range(flag):
            scr.blit(userimg, (15, 85 + y_next))
            scr.blit(myquestion[i], (55, 85 + y_next))
            scr.blit(botimg, (15, 103 + y_next))
            scr.blit(botanswer[i], (55, 107 + y_next))
            y_next += 55
    if flag >= 10:
        for i in range(flag-j):
            scr.blit(userimg, (15, 85 + y_next))
            scr.blit(myquestion[i+j], (55, 85 + y_next))
            scr.blit(botimg, (15, 103 + y_next))
            scr.blit(botanswer[i+j], (55, 107 + y_next))
            y_next += 55
  
    scr.blit(userimg2, (75, 600))                            
    txt_surface = font.render(text, True, color)
    width = max(600, txt_surface.get_width()+10)
    input_box.w = width
    scr.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pg.draw.rect(scr, color, input_box, 2)   
    #pg.display.flip()
    
    

#pg.quit()






