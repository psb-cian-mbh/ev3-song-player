#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

bases = [32.70320, 65.40639, 130.8128, 261.6256, 523.2511, 1046.502, 2093.005, 4186.009] # frequency bases for C1, C2, etc.

# calculating key frequencies
keys = {}
i = 0
for base in bases:
    i += 1
    keys[i] = {
        'C': base * 2**(0/12),
        'c': base * 2**(1/12),
        'D': base * 2**(2/12),
        'd': base * 2**(3/12),
        'E': base * 2**(4/12),
        'F': base * 2**(5/12),
        'f': base * 2**(6/12),
        'G': base * 2**(7/12),
        'g': base * 2**(8/12),
        'A': base * 2**(9/12),
        'a': base * 2**(10/12),
        'B': base * 2**(11/12),
    }

class Note:
    def __init__(self, key, octave):
        self.key = key
        self.octave = octave

    def __repr__(self):
        return self.key + str(self.octave)

    def play(self):
        """Plays note"""
        ev3.speaker.beep(keys[self.octave][self.key])

class Song:
    def __init__(self, text):
        """Initializes a Song object with the notes parsed from the param text"""
        self.notes = []
        i = 0
        while i < len(text):
            if text[i] in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                letter = text[i]
                i += 1
                if i < len(text) and text[i] in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    octave = text[i]
                    if i+1 < len(text) and text[i+1] == '#':
                        letter = letter.lower()
                        i += 2
                    self.notes.append(Note(letter, int(octave)))
                    i += 1
                else:
                    self.notes.append(Note(letter, 4))
            elif text[i] == ' ':
                self.notes.append('rest')
                i += 1
            else:
                print("expected a note, found", text[i])
                exit(1)
    def play(self):
        """Plays song"""
        for note in self.notes:
            if note == 'rest': wait(.2)
            else: note.play()

songs = {
    'twinkle': "C C G G A A G  F F E E D D C  G G F F E E D  G G F F E E D  C C G G A A G  F F E E D D C",
}

if __name__ == "__main__":
    twinkle = Song(songs['twinkle'])
    twinkle.play()
