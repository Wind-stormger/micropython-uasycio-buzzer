'''
Licence
The music score used in this code comes from https://www.qupu123.com/puyou/jipu/p289352.html
Comply with the CC BY-NC-SA 3.0 license
'''
from machine import Pin,PWM
import time
import buzzer
import uasyncio as asyncio

Weight_of_the_World=[
    (1/2,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"2"),(1/2,"5"),
    (1/4,"L6"),(1/4,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"5"),
    (1/1,"5"),
    
    (1/2,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"2"),(1/2,"6"),
    (1/4,"2"),(1/4,"2"),(1/4,"3"),(1/4,"2"),(1/4,"6"),
    (1/1,"6"),
    
    (1/2,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"2"),(1/2,"5"),
    (1/4,"L6"),(1/4,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"5"),
    (1/1,"5"),
    
    (1/2,"L6"),(1/4,"3"),(1/4,"2"),(1/4,"2"),(1/2,"6"),
    (1/4,"2"),(1/4,"2"),(1/4,"3"),(1/4,"2"),(1/4,"6"),
    (1/1,"6"),
    ]

buzzer=buzzer.Buzzer(PWM(Pin(1)))
buzzer.play(Weight_of_the_World,tempo=90,freq_multiple=1,output=0)
