from win32com.client import Dispatch
from mutagen.mp3 import MP3
from gtts import gTTS
from pygame import mixer
from time import sleep
from symbols import SYMBOLS


# ***   Text Properties   *** #
BOLD = "\x1b[1m"
TXT = "\x1b[38;2;0;0;210;48;2;212;175;55m"
NORMAL = "\x1b[m"

# ***   Speech Properties   *** #
SPEAK = True
MALE = False
LANG = "en"
DIALECT = "com"
LANG_CHECK = False
SPEED = False
PAUSE = ","
SPEECH_FILE = "speach_tmp.mp3"


def windows_voice(text):
    """
    Speaks the text with a male voice.

    The function uses the Windows Text To Speech Engine for converting the text string that is
    passed to the function.

    :param text: str :
        The text that is converted to speech.

    :return: Nothing is returned.
    """
    speak = Dispatch("SAPI.SpVoice")
    for word in text.split(PAUSE):
        speak.Speak(word)


def google_voice(text):
    """
    Speaks the text with a female voice.

    The function uses the Google Text To Speech Engine for converting the text string that is
    passed to the function.

    :param text: str :
        The text that is converted to speech.

    :return: Nothing is returned.
    """
    gTTS(text, lang=LANG, tld=DIALECT, lang_check=LANG_CHECK, slow=SPEED).save(SPEECH_FILE)
    mixer.init()
    mixer.music.load(SPEECH_FILE)
    mixer.music.play()
    sleep(MP3(SPEECH_FILE).info.length)


def print_nato(text):
    """
    Prints and speaks the NATO Phonetics of the text.

    The function converts the text string that is passed to the function into NATO Phonetics.
    The Nato Phonetics is then printed on the screen and converted to speech sent to the speakers.

    When the NATO Phonetics is printed on the screen, colors and formatting of the text and background
    can be configured by the BOLD and TEXT global parameters.
    The speech can be turned off by setting the global parameter SPEAK to False. It is also possible to
    choose between a male or a female voice by setting the global parameter MALE to True or False.

    :param text: str :
        The text that is converted into NATO Phonetics.

    :return: Nothing is returned.
    """
    print()
    nato_show = ""
    nato_speak = ""
    spaced = False
    for c in text.strip():
        if c.lower() in SYMBOLS:
            nato_show += BOLD + TXT + " " + SYMBOLS[c.lower()]["nato"] + " " + NORMAL
            nato_speak += " " + SYMBOLS[c.lower()]["nato"] + " "
            spaced = False
        if c.isspace() and not spaced:
            nato_show += "   "
            nato_speak += PAUSE
            spaced = True
    print(nato_show.strip())
    if SPEAK:
        if MALE:
            windows_voice(nato_speak)
        elif nato_speak:
            try:
                google_voice(nato_speak)
            except (ValueError, RuntimeError):
                windows_voice(nato_speak)


def main():
    """
    Asks for a word or phrase, converts it to NATO Phonetics, displays the result on the screen and
    plays it in the speakers.

    :return: Nothing is returned.
    """
    text = input("Enter a word or a phrase: ")
    print_nato(text)


if __name__ == "__main__":
    main()
