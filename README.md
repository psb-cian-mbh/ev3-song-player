# ev3-song-player

Parses notes from a string of notes (spaces as rests).

## Docs

### ```Song``` member functions:

```__init__(self, text)```

Generates a ```Song``` object from ```text```.


```play(self)```

Plays the song.


### ```Note``` member functions:

```__init__(self, note, octave)```

Initializes object with note information


```__repr__(self)```

Formats ```Note``` object for printing.


```play(self)```

Plays the note using ```ev3.speaker.beep()```

### Other

```keys```

3 Dimensional dictionary object. Frequencies for a note are found through their octave, e.g. ```Middle C = C4 = key[4]['C']```


```songs```

Dictionary of premade songs
