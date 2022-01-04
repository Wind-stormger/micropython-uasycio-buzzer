# what is it

This project is a simple micropython pwm buzzer driver, which supports the application of uasycio to achieve multi-channel music playback, or multi-channels merged into one to achieve chord sound playback.

The method of composing music is more in line with the editing method of numbered musical notation. 

Composers can compose music in python code in this way. 

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

Note:   	C	D	E	F	G	A	B

Solfège:	do	re	mi	fa	so	la	ti

Notation:	1	2	3	4	5	6	7

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

A board with micropython firmware already. 

Upload the `buzzer.py` file to the board.

A buzzer and its matching circuit,or just Some connecting lines with a loudspeaker,need to pay attention to the use of voltage and power to avoid failure to work or accidental damage. 

Use one wire to share the ground, namely GND to GND. 

Use another wire to connect the pin that will output the PWM signal from the board to the signal receiving end of the buzzer or loudspeaker .

## Demo program
### Ordinary method
```python
from machine import Pin,PWM
import time
import buzzer
Musical_Score=[(1/2,"L1"),(1/4,"L2"),(1/2,"L3"),(1,"L4"),(2,"L5"),
               (1/2,"1#"),(1/4,"2#"),(1/2,"3"),(1,"4#"),(2,"5#"),
               (1/2,"H1#"),(1/4,"H2#"),(1/2,"H3"),(1,"H4#"),(2,"H5#"),(1,"0")]
pwm=PWM(Pin(1,Pin.OUT)
buzzer=buzzer.Buzzer(pwm))
buzzer.play(score=Musical_Score,tempo=60,freq_multiple=1,output=0)
```
