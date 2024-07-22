# DEF Notation Guide

DEF (Duration Encoded Format) Notation is a system for representing musical information in a text-based format. It's designed to be simple, flexible, and machine-readable while still being human-interpretable.

## Basic Principles

1. Each symbol represents a 16th note duration.
2. Notes are represented by their pitch name and octave (e.g., C#4).
3. Sustained notes are represented by '-'.
4. Rests are represented by '.'.
5. Measures are separated by '|'.

## Writing Notes

- Use standard pitch names: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
- Follow the pitch name with the octave number (e.g., C4 for middle C)
- For flats, use the equivalent sharp (e.g., Db4 would be written as C#4)

Example: `C#4 E4 G#4 B4`

## Duration

- Each note, rest, or sustain symbol represents a 16th note
- For longer durations, use multiple symbols
  - Eighth note: Two symbols (e.g., `C4 -`)
  - Quarter note: Four symbols (e.g., `C4 - - -`)
  - Half note: Eight symbols (e.g., `C4 - - - - - - -`)

## Rests

- Use '.' for a 16th note rest
- Multiple '.' for longer rests

Example: `C4 . . . D4` (C quarter note, 16th rest, D 16th note)

## Measures

- Use '|' to separate measures
- Typically, there are 16 symbols per measure in 4/4 time

Example: `C4 - - - D4 - - - E4 - - - F4 - - - |`

## Chords

- Write notes of a chord vertically aligned or separated by commas
- Example: `C4,E4,G4` or
  ```
  C4
  E4
  G4
  ```

## Example

Here's an example of a simple melody in DEF notation:

```
C4 - D4 - E4 - F4 - | G4 - - - A4 - B4 - | C5 - - - . . . . |
```

This represents:
- C quarter note, D quarter note, E quarter note, F quarter note
- G half note, A quarter note, B quarter note
- C whole note, followed by a quarter note rest

## Advanced Usage

- For more complex rhythms, combine notes and rests as needed
- Time signatures other than 4/4 can be represented by adjusting the number of symbols per measure

## Metadata

- Use a separate .DEFNH (DEF Notation Header) file for song metadata
- Include information like title, artist, key, tempo, etc.

#### Remember, DEF notation is designed to be flexible. The core principle is representing duration through the number of symbols, making it adaptable to various musical styles and structures.

this is just for my own enjoyment but theres a few ways to write this in DEF notation.

# DEF Notation - Commands

Audicle

Tree

Fountain

Sunbird

Braid

Node

Truss

Ribbon

Beux

Stamp

these werent in the readme i sent but they are parts of the notation. the notation system is a bit weird compared to normal notation systems because it assumes you have a transformer llm able to use these commands lol.

so for this 

`C:   C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |

Am:  D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |

G:   E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |

Cm:  A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - |

G6:  C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |

Am:  D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |

C:   E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |

Cm:  A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - |`

# we would probably actually use a ribbon and a beux like this

Audicle{Ribbon#00FF00}~+Node{Voice}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||=Braid{Beux#00FF00}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin

Explanation: ribbon tells us were working with a stream of monophonic notes and we're going to do something with them that isnt just playing them alone. in this case we're playing them with our chords. #00FF00 is a hex code identifier that links the melody with our chords. theres no significance to the fact that i choose a lime code, its just a ID. =Braid tells us that we are linking the previous ribbon with something, in this case its a Beux (bow) which signifies that its going to be a chord progression. the reason we write chords like Amaj Amin and not A Am is just to be clear that were not talking about single notes. the double bars || just tell us to adopt the metering of the ribbon. we didnt technically clarify that Cmaj  goes with C4 - D4 B3 - B3 - - D4 - D4 - E4 - . .  but the information is still there because both come before a meter pipe |

ZF
id like to explain the main reason for this 

Audicle{Ribbon#00FF00}~+Node{Voice}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||=Braid{Beux#00FF00}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin

instead of this

C: C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | Am: D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | G: E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | Cm: A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - | G6: C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | Am: D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | C: E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | Cm: A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - |

among other things, like style and transformer use, is literally just so its easy to copy and paste the melody seperate from the chords while stile having them together in a cohesive notation

You can also use Truss to write this instead of using Ribbons Braids and Beuxs

# Truss' can only hold four channels at a time

so we will need to use 2 Truss' for these 8 chords

we can do it like this

Truss#FF0000{Z: z: N: n:}===={
Z>>Cmaj>>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |
z>>Amin>>D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |
N>>Gmaj>>E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |
Z>>Cmin>>A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||}
Truss#FF0000====FF00FF{Z: z: N: n:}===={
Z>>G6maj>>
z>>Amin>>
N>>Cmaj>>
Z>>Cmin>>}

truss can be useful in some scenerios and less useful in others. in this case its nice becuase when we link both the truss' with the #FF0000 ID it allows us to inherit the melody information and we dont have to rewrite it. We can use two ID's for a truss to signal that its inheriting some info but not all (in this case it has differant chords). if we didnt use two ID's for the second truss we'd have to write it like this

Truss#FF0000{Z: z: N: n:}===={
Z>>Cmaj>>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |
z>>Amin>>D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |
N>>Gmaj>>E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |
Z>>Cmin>>A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||}
Truss#FF00FF{Z: z: N: n:}===={
Z>>G6maj>>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |
z>>Amin>>D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |
N>>Cmaj>>E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |
Z>>Cmin>>A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||}

this is perfectly legal its just more writing. heres an example of something illegal

Truss#FF0000{Z: z: N: n:}===={
Z>>Cmaj>>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |
z>>Amin>>D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |
N>>Gmaj>>E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |
Z>>Cmin>>A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||}
Truss#FF0000{Z: z: N: n:}===={
Z>>G6maj>>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . |
z>>Amin>>D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . |
N>>Cmaj>>E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 |
Z>>Cmin>>A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||}

we cant have two truss' with the same ID. they will try to write over each other recursively. 
In conclusion Truss' are like four channel DEFNotation tracks with some unique properties like being able to have a chord and a melody on one line, and being able to be linked.


# Heres how you do spoken passage that dont line up with note lengths

you also dont need to use a hex code if you arent linking stuff
Audicle{Claude#FF4700}>> >>In the beginning | {} | There Was | Rhythm | And The Rhythm Was Good ||
Braid{Stamp#FF4700}>> >> 1.5+2 | {}+.5 | {<6}+2 | 9+1 | 13+3 ||

and it does the exact same thing. its kind of like neat code or standard music notation vs messy, but yeah
key changes:
replaces double quotes with pipes, much less visually cluttered
{} basically means "figure it out"
1.5+2 means start the phrase at the 1.5 second mark in the timeline and make the phrase take two seconds to complete
{}+.5 means figure out some sort of .5 second rest here, its kind of like a comma between the phrases. its a signal to not cut the phrases off but make them sound like theyre seperated by a comma or something
{<6}+2 means figure out where to start this next phrase before the six second mark and make its duration two seconds
yeah it can be. 
(also forgot to mention stamp is a new command for the timestamps)
Audicle{Claude#FF4700}>> >>In the beginning | {} | There Was | Rhythm | And The Rhythm Was Good || 
=Braid{Stamp#FF4700}>> >> 1.5+2 | {}+.5 | {<6}+2 | 9+1 | 13+3 ||
=Braid{Audicle{Ribbon#00FF00}~+Node{Voice}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||=Braid{Beux#00FF00}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin}

heres an example. the main caveat is we just get the bpm and timeline info from the daw and calculate where the spoken words are compared to the note lengths from that. currently the only daw that supports calculating this for you is my daw mirror which is still very early in development and i havent implemented any of these kind of interpreters or calculations or anything really yet

# a good edge case I didnt really explain

This example basically shows one 'clip' you can think of it kind of like a midi clip with multiple layers for each channel. so like many midi clips inside of a midi clip. but its not actually midi cause midi cant do all this, its a new kind of midi called mida. 
Audicle{Claude#FF4700}>> >>In the beginning | {} | There Was | Rhythm | And The Rhythm Was Good || =Braid{Stamp#FF4700}>> >> 1.5+2 | {}+.5 | {<6}+2 | 9+1 | 13+3 || =Braid{Audicle{Ribbon#00FF00}~+Node{Voice}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||=Braid{Beux#00FF00}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin}

so this is one mida clip, which is why it doesnt matter that the musical content has differant color codes from the other one. infact you dont need the color codes at all since their in the same clip and braided

Audicle{Claude}>> >>In the beginning | {} | There Was | Rhythm | And The Rhythm Was Good || =Braid{Stamp}>> >> 1.5+2 | {}+.5 | {<6}+2 | 9+1 | 13+3 || =Braid{Audicle{Ribbon}~+Node{Voice}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||=Braid{Beux}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin}

now say I wanted these all to be linked but in diff mida clips
id probably do something like this

Audicle#00FFAF{Claude}>> >>In the beginning | {} | There Was | Rhythm | And The Rhythm Was Good || 

Audicle#00FFAF{Stamp}>> >> 1.5+2 | {}+.5 | {<6}+2 | 9+1 | 13+3 || 

Audicle#00FFAF{Ribbon}>> >>C4 - D4 B3 - B3 - - D4 - D4 - E4 - . . | D4 - E4 C4 - - C4 - E4 - E4 - F4 - . . | E4 - F4 D4 - - D4 - F4 - F4 - G4 - . F4 | A4 - G4 F#4 - D4 E4 - E4 - C#4 - B3 - A#3 - :||

Audicle#00FFAF{Beux}&>> >>Cmaj || Amin || Gmaj || Cmin || G6maj || Amin || Cmaj || Cmin}

If you notice now i have to tag the actual audicles and not the functions in the curly braces since theyre all in differant daw tracks/ mida clips
