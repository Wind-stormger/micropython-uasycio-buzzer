'''
The method of editing musical notation in this program is based on the numbered notation described.
Numbers 1 to 7 represent the musical notes (more accurately the scale degrees). 
They always correspond to the diatonic major scale.
For example, in the key of C, their relationship with the notes and the solfège is as follows:

Note:   	C	D	E	F	G	A	B
Solfège:	do	re	mi	fa	so	la	ti
Notation:	1	2	3	4	5	6	7

In the numbered notation described,dots above or below a musical note raise or lower it to other octaves. 
The number of dots equals the number of octaves.
Here,the dots above a musical note change to "L",such as "L1".
The dots below a musical note change to "H",such as "H1".
If it is sharp (higher in pitch by one semitone (half step)), its notation is "#", such as "1#". 
The number "0" represents the musical rest.
'''
from machine import Pin,PWM
import time
import uasyncio as asyncio

#The dictionary contains 37 notes and their corresponding PWM frequencies.
Tone_Dict={"L1":131,"L1#":139,"L2":147,"L2#":156,"L3":165,"L4":175,"L4#":185,"L5":196,"L5#":208,"L6":220,"L6#":233,"L7":247,
            "1":262, "1#":277, "2":294, "2#":311, "3":330, "4":349, "4#":370, "5":392, "5#":415, "6":440, "6#":466, "7":494,
           "H1":523,"H1#":554,"H2":587,"H2#":622,"H3":659,"H4":698,"H4#":740,"H5":784,"H5#":831,"H6":880,"H6#":932,"H7":988,
            "0":0}

class Buzzer:
    def __init__(self,pwm=None):
        self.pwm=pwm
        if self.pwm==None:
            self.pwm=PWM(Pin(0,Pin.OUT))
        self.pwm.duty(0)


    def play(self,score,tempo=60,freq_multiple=1,output=0):
        One_Beat_Time=1000*60/tempo
        if output==1:
            print("Tempo:%sbpm,One_Beat_Time:%sms,Freq_multiple:%s" % (tempo,One_Beat_Time,freq_multiple))
        for (beat,tone1) in score:
            play_freq=round(Tone_Dict[tone1]*freq_multiple)
            play_time=round(beat * One_Beat_Time)
            if output==1:
                print("Beat:%s,Tone:%s,Freq:%s" % (beat,tone1,play_freq))
            if play_freq==0:
                self.pwm.duty(0)
            else:
                if not self.pwm.freq() == play_freq:
                    self.pwm.freq(play_freq)
                self.pwm.duty(512)
            time.sleep_ms(play_time)
            self.pwm.duty(0)
            time.sleep_ms(1)
        self.pwm.duty(0)

    async def async_play(self,score,tempo=60,freq_multiple=1,output=0,channel=0):
        One_Beat_Time=1000*60/tempo
        if output==1:
            print("Channel:%s,Tempo:%sbpm,One_Beat_Time:%sms,Freq_multiple:%s" % (channel,tempo,One_Beat_Time,freq_multiple))
        for (beat,tone1) in score:
            play_freq=round(Tone_Dict[tone1]*freq_multiple)
            play_time=round(beat * One_Beat_Time)
            if output==1:
                print("Channel:%s,Beat:%s,Tone:%s,Freq:%s" % (channel,beat,tone1,play_freq))
            for i in range(0,play_time+10,10):
                if play_freq==0:
                    self.pwm.duty(0)
                else:
                    if not self.pwm.freq() == play_freq:
                        self.pwm.freq(play_freq)
                    self.pwm.duty(512)
                await asyncio.sleep_ms(10)
            self.pwm.duty(0)
            await asyncio.sleep_ms(1)
        self.pwm.duty(0)

if __name__ == '__main__':
    Music_Score1=[(1/4,"3"),(1/4,"3"),(1/4,"4"),(1/4,"5"),
                  (1/4,"5"),(1/4,"4"),(1/4,"3"),(1/4,"2"),
                  (1/4,"1"),(1/4,"1"),(1/4,"2"),(1/4,"3"),
                  (1/4,"3"),(1/4,"2"),(1/4,"2")]
    Music_Score2=[(1,"1"),(1,"2"),(1,"3"),(1,"4"),(1,"5"),]
    Music_Score3=[(1,"1"),(1,"1"),(1,"1"),(1,"1"),(1,"1"),]

#     buzzer=Buzzer(PWM(Pin(1,Pin.OUT)))
#     buzzer.play(Music_Score1,tempo=30,freq_multiple=1,output=0)

    async def main():
        pwm1=PWM(Pin(1,Pin.OUT))
        pwm2=PWM(Pin(2,Pin.OUT))
        buzzer1=Buzzer(pwm1)
        buzzer2=Buzzer(pwm2)
        tasks=[asyncio.create_task(
            buzzer1.async_play(Music_Score1,tempo=60,freq_multiple=1,output=1,channel=0))]
        tasks.append(asyncio.create_task(
            buzzer2.async_play(Music_Score2,tempo=60,freq_multiple=1,output=1,channel=1)))
        await asyncio.gather(*tasks)
    
    asyncio.run(main())

