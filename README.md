# NATO Alphabet and Morse Code

A short Python program that translates text both to the NATO Phonetic Alphabet and to Morse code. The Morse code is shown both visually as well as played in the speakers. The NATO Phonetics of the text will aslo be spoken. 

It is possible to choose the spoken voice to be either a male voice or a female voice. The male voice is using Windows Speach To Text Engine. The female voice is using Google Speech To Text Engine. Which voice to use is configured in the Speech Properties section near the top of the main.py file. 

Most of the look and behavior of this program can be configured by changing the values of some configuration constants at the top of the nato.py and morse.py files. They are organized in the following sections:

* Text Properties <br/>
Properties for changing the color and the look of the NATO Phonetic text shown on the screen

* Speech Properties <br/>
Properties that decide if the phonetics should be played, which voice to use, which language to use, speed, and the name of the temporary resulting speech file (an mp3-file is required when using the Google Speech Engine for the female voice).

* Morse Properties <br/>
Properties that decide if the Morse code of the text should be shown and played, as well as the speed, tone frequencey and all the relations between the durations of dots, dashes, and spaces between symbols, letters, words, etc.

<br/>

### Example:

<img width="602" alt="image" src="https://user-images.githubusercontent.com/1498298/204062001-c11fda2c-866a-4866-b2f6-6d66f2669298.png">

<br/>

### Architecture

The program is split into several parts. 
* All the logic and functionality for the NATO Phonetics part is in the nato.py file.
* All the logic and functionality for the Morse part is in the morse.py file.
* All the data that is used to produce the correct phonetics and the correct Morse letters is stored in a dictionary in the symbols.py file. Add new characters or removing characters only requires to enter or remove entries in the dictionary. No logic need to be changed.
* The app itlsef can then use the resources from the other modules.
* There is a fully functional command-line app using this architecture in the file nm_cmd.py
* A GUI app is being developed, using this architecture, with the core GUI functionality in nm_win.py

<br/>

### Graphical User Interface

Below is the first draft of a possible GUI for this app:

<img width="977" alt="image" src="https://user-images.githubusercontent.com/1498298/205522157-33ff7069-ff1c-46d1-9cae-e0d6e2e87ca5.png">
