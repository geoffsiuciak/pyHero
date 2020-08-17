# pyHero
2-D rhythm game with custom charting solution
2 songs included:
- "Exposed" by Old Sol (demo)
- "Rosalyn" by Better Love (cover)

# MAKE A CHART:
- creating custom songs is easy. using the MIDI editor inside any DAW, line up your audio and midi start point at 0:00
- note: if a note occurs within the first 1200 ms of the song, add 2 bars of silence before the audio begins
- use MIDI values 64-60 for orange-green notes respectively (default key controls are S-D-F-G-H)
- export MIDI, and convert to JSON using https://tonejs.github.io/Midi/ (thank you!)
- copy and save the output into a .txt file and save into the JSON_FILES folder
- the parseJson() method in actions.py will grab data from the tree and write to a new excel file in the LOADED_SONGS folder 

# project goals
- build an original, end-to-end solution for creating and playing rhythm charts
- maintain good design practice and focus on customizability

# to-do, features to add
- sustain bars: complete .blit() animation using note.SUSTAIN_LENGTH attribute
- debug input comparisons on chords 
- fix up excel formatting in actions.parseMidi()
- add guitar controller support (wii w/ usb dongle), this was my initial vision for the project
