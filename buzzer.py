"""
The method of editing musical notation in this program is based on numbered notation described.
For details, please refer to README.
https://github.com/Wind-stormger/micropython-uasycio-buzzer
"""
import time
import asyncio
from machine import PWM

# The dictionary contains 37 notes and their corresponding PWM frequencies.
Tone_Dict = {"L1": 131, "L1#": 139, "L2": 147, "L2#": 156, "L3": 165, "L4": 175, "L4#": 185, "L5": 196, "L5#": 208,
             "L6": 220, "L6#": 233, "L7": 247,
             "1": 262, "1#": 277, "2": 294, "2#": 311, "3": 330, "4": 349, "4#": 370, "5": 392, "5#": 415, "6": 440,
             "6#": 466, "7": 494,
             "H1": 523, "H1#": 554, "H2": 587, "H2#": 622, "H3": 659, "H4": 698, "H4#": 740, "H5": 784, "H5#": 831,
             "H6": 880, "H6#": 932, "H7": 988,
             "0": 0}


class Buzzer:
    # Initialize a PWM channel
    def __init__(self, pin):
        self.pwm = PWM(pin)
        self.pwm.duty(0)

    # Ordinary method
    def play(self, score, tempo=60, freq_multiple=1, output=0):
        one_beat_time = 1000 * 60 / tempo
        if output == 1:
            print("Tempo:%sbpm,one_beat_time:%sms,Freq_multiple:%s" %
                  (tempo, one_beat_time, freq_multiple))
        for (beat, tone1) in score:
            play_freq = round(Tone_Dict[tone1] * freq_multiple)
            play_time = round(beat * one_beat_time)
            if output == 1:
                print("Beat:%s,Tone:%s,Freq:%s" % (beat, tone1, play_freq))
            self.pwm.freq(play_freq)
            if play_freq == 0:
                self.pwm.duty(0)
            else:
                self.pwm.duty(512)
            time.sleep_ms(play_time)
            self.pwm.duty(0)
            time.sleep_ms(1)
        self.pwm.duty(0)

    # Async method
    async def async_play(self, score, tempo=60, freq_multiple=1, output=0, channel=0):
        one_beat_time = 1000 * 60 / tempo
        if output == 1:
            print("Channel:%s,Tempo:%sbpm,one_beat_time:%sms,Freq_multiple:%s" % (
                channel, tempo, one_beat_time, freq_multiple))
        await asyncio.sleep_ms(0)
        for (beat, tone1) in score:
            play_freq = round(Tone_Dict[tone1] * freq_multiple)
            play_time = round(beat * one_beat_time)
            if output == 1:
                print("Channel:%s,Beat:%s,Tone:%s,Freq:%s" %
                      (channel, beat, tone1, play_freq))
            self.pwm.freq(play_freq)
            if play_freq == 0:
                self.pwm.duty(0)
            else:
                self.pwm.duty(512)
            await asyncio.sleep_ms(play_time)
            self.pwm.duty(0)
