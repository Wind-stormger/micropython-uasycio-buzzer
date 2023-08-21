# What is it

This project is a simple micropython pwm buzzer driver, which supports the application of uasycio to achieve multi-channel music playback, or multi-channels merged into one to achieve chord sound playback.

The method of composing music is more in line with the editing method of numbered musical notation. 

Composers can compose music in python code in this way. 

Currently only tested ESP32S2 chip.

After confirming the relevant documents, it has been determined that it should be compatible with all chips launched by Espressif that already support the micropython firmware , such as ESP8266,ESP32,ESP32S2,ESP32S3,ESP32C3.

# How to edit your own musical score

A musical score is a list, and each element in the list contains two values,first value is beat,second value is tone.

Example:

```python
Musical_Score=[(1/2,"L1"),(1/4,"L2"),(1/2,"L3"),(1,"L4"),(2,"L5"),
               (1/2,"1#"),(1/4,"2#"),(1/2,"3"),(1,"4#"),(2,"5#"),
               (1/2,"H1#"),(1/4,"H2#"),(1/2,"H3"),(1,"H4#"),(2,"H5#"),(1,"0")]
```

Numbers 1 to 7 represent the musical notes (more accurately the scale degrees). 

They always correspond to the diatonic major scale.

For example, in the key of C, their relationship with the notes and the solfège is as follows:

|Note|Solfège|Notation|
|---|---|---|
| C | do | 1 |
| D | re | 2 |
| E | mi | 3 |
| F | fa | 4 |
| G | so | 5 |
| A | la | 6 |
| B | ti | 7 |

In the numbered notation described,dots above or below a musical note raise or lower it to other octaves. 

The number of dots equals the number of octaves.

Here,the dots above a musical note change to "L",such as "L1".

The dots below a musical note change to "H",such as "H1".

If it is sharp (higher in pitch by one semitone (half step)), its notation is "#", such as "1#". 

The number "0" represents the musical rest.

With these rules, you can edit the musical score, it is recommended to try the simple music that you are most familiar with and love first, and search for its numbered musical notation on the Internet and edit it into code accordingly. 

More knowledge about numbered musical notation please refer to [Wikipedia](https://en.wikipedia.org/wiki/Numbered_musical_notation) or other more professional music theory articles or videos.

# How to play music on the buzzer or loudspeaker

## Necessary software and hardware conditions

A board with micropython firmware already. (Currently only tested ESP32S2)

Upload the `buzzer.py` file to the board.

A buzzer and its matching circuit,or just Some connecting lines with a loudspeaker,need to pay attention to the use of voltage and power to avoid failure to work or accidental damage. 

Use one wire to share the ground, namely GND to GND. 

Use another wire to connect the pin that will output the PWM signal from the board to the signal receiving end of the buzzer or loudspeaker .

## Examples

Currently only tested ESP32S2.

### Ordinary method

```python
from machine import Pin,PWM
import time
import buzzer
Musical_Score=[(1/2,"L1"),(1/4,"L2"),(1/2,"L3"),(1,"L4"),(2,"L5"),
               (1/2,"1#"),(1/4,"2#"),(1/2,"3"),(1,"4#"),(2,"5#"),
               (1/2,"H1#"),(1/4,"H2#"),(1/2,"H3"),(1,"H4#"),(2,"H5#"),(1,"0")]
buzzer=buzzer.Buzzer(Pin(1))
buzzer.play(score=Musical_Score,tempo=60,freq_multiple=1,output=0)
```

- `buzzer.Buzzer(pwm)`
    - `pwm`: A necessary PWM channel, such as `machine.PWM(Pin(1))`.

- `play(score,tempo,freq_multiple,output)`
    - `score`: A list include musical score , it is necessary.
    - `tempo`: The speed at which a passage of music is or should be played, unit is **bpm**(Beat Per Minute), Default value is `tempo=60`, means 60 beats per minute.
    - `freq_multiple`: Each tone has its corresponding PWM frequency, setting this value will make the frequency multiply by this value. Default value is `freq_multiple=1`.
    - `output`: Default value is `output=0`.If the value is `output=1`, detailed information will be printed when each tone is played.

### Async method

```python
from machine import Pin,PWM
import uasyncio as asyncio
import buzzer
Musical_Score1=[(1/2,"L1"),(1/4,"L2"),(1/2,"L3"),(1,"L4"),(2,"L5")]
Musical_Score2=[(1/2,"1#"),(1/4,"2#"),(1/2,"3"),(1,"4#"),(2,"5#")]
async def main():
    buzzer1=buzzer.Buzzer(1)
    buzzer2=buzzer.Buzzer(2)
    tasks=[asyncio.create_task(
        buzzer1.async_play(Musical_Score1,tempo=60,freq_multiple=1,output=1,channel=0))]
    tasks.append(asyncio.create_task(
        buzzer2.async_play(Musical_Score2,tempo=60,freq_multiple=1,output=1,channel=1)))
    await asyncio.gather(*tasks)
asyncio.run(main())
```

- `buzzer.Buzzer(pwm)` same as ordinary method

- `async_play(score,tempo,freq_multiple,output,channel))` mostly same as ordinary method
    - `channel`: Only valid when `output=1`.This channel value will be output when printing detailed information, in order to distinguish the channel corresponding to the specific information.

The application method of `uasyncio` is detailed in[peterhinch's Github project ：micropython-async](https://github.com/peterhinch/micropython-async)

For general applications, please refer to the code in the example. 

1. Create an async function , `async def main():` 

2. Create a tasks list ,  `tasks=[]`

3. Create async tasks to the list , such as `tasks=[asyncio.create_task()]` or `tasks.append(asyncio.create_task())`

4. Use the `gather` method to gather all tasks, `await asyncio.gather(*tasks)`

5. Use the `run` method to run the async function created in step 1. When the execution reaches `await asyncio.gather(*tasks)`, the corresponding music score will be played on each channel.

# Issues or Pull requests

If you have any questions or good ideas, please submit your issue, and specify your hardware and software conditions and specific questions in detail.

The code of this program is relatively simple, I think it will not be difficult to transplant and adapt, but there is no other platform available in my hand, and those who are interested are welcome to pull requests. 

# Enjoy it :)
