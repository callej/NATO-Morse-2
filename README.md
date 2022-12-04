# NATO Alphabet and Morse Code

A short Python program that translates text both to the NATO Phonetic Alphabet and to Morse code. The Morse code is shown both visually as well as played in the speakers. The NATO Phonetics of the text will aslo be spoken. 

It is possible to choose the spoken voice to be either a male voice or a female voice. The male voice is using Windows Speach To Text Engine. The female voice is using Google Speech To Text Engine. Which voice to use is configured in the Speech Properties section near the top of the main.py file. 

Most of the look and behavior of this program can be configured by changing the values of some confiuration constants at the top of the main.py file. They are organized in the following sections:

* Text Properties <br/>
Properties for changing the color and the look of the NATO Phonetic text shown on the screen

* Morse Properties <br/>
Properties that decide if the Morse code of the text should be shown and played, as well as the speed, tone frequencey and all the relations between the durations of dots, dashes, and spaces between symbols, letters, words, etc.

* Speech Properties <br/>
Properties that decide if the phonetics should be played, which voice to use, which language to use, speed, and the name of the temporary resulting speech file (an mp3-file is required when using the Google Speech Engine for the female voice).

<br/>

### Example:

<img width="602" alt="image" src="https://user-images.githubusercontent.com/1498298/204062001-c11fda2c-866a-4866-b2f6-6d66f2669298.png">

<br/>

### Architecture

The program is split into two parts. All the logic is in the main.py file. All the data that is used to produce the correct phonetics and the correct Morse letters is stored in a dictionary in the symbols.py file. Add new characters or removing characters only requires to enter or remove entries in the dictionary. No logic need to be changed, meaning no change is required in the main.py file. 

<br/>

### Graphical User Interface

Below is the first draft of a possible GUI for this app:

<img width="977" alt="image" src="https://user-images.githubusercontent.com/1498298/205520936-72dcb22b-87ea-457f-8184-ce306ad55c72.png">

