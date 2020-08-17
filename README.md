# pyHero
2-D rhythm game with custom charting solution. Includes 2 songs:
- "Exposed" by Old Sol (demo)
- "Rosalyn" by Better Love (cover)

[![](http://img.youtube.com/vi/Wosj12coIN4/0.jpg)](http://www.youtube.com/watch?v=Wosj12coIN4 "pyHero")


# MAKE A CHART:
- creating custom songs is easy. open the song and MIDI editor inside any DAW, ensuring your audio starts at 0:00
- if a note occurs within the first 1200 ms of the song, add 2 bars of silence before the audio begins
- use MIDI values 64-60 for green-orange notes respectively (default key controls are S-D-F-G-H)
- export MIDI, and convert to JSON using https://tonejs.github.io/Midi/ (thank you!)
- copy and save the output into a .txt file and save into the JSON_FILES folder
- the parseJson() method in actions.py will grab data from the tree and write to a new excel file in the LOADED_SONGS folder 
- append song metadata to data.py

# project goals
- build an original, end-to-end solution for creating and playing rhythm charts
- maintain good design practice and focus on customizability
- learn stuff

# to-do, features to add
- sustain bars: complete .blit() animation using note.SUSTAIN_LENGTH attribute
- debug input comparisons on chords 
- clean up excel formatting in actions.parseMidi()
- add guitar controller support (wii w/ usb dongle), this was my initial vision for the project
