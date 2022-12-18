import string

from win32com.client import Dispatch
from mutagen.mp3 import MP3
from gtts import gTTS
from pygame import mixer
from time import sleep
from symbols import SYMBOLS

# ***   Text Properties   *** #
SHOW = True
EMPHASIS = "\x1b[1m"
COLOR = "\x1b[38;2;0;0;210;48;2;212;175;55m"
NORMAL = "\x1b[m"
CHAR_SEP = " "
WORD_SEP = "   "

# ***   Speech Properties   *** #
SPEAK = True
MALE = False
LANG = "en"
DIALECT = "com"
LANG_CHECK = False
SPEED = False
PAUSE = ","
SPEECH_FILE = "speach_tmp.mp3"

# ***   Configuration Dictionaries   *** #
nato_text_config = {
    "show": {
        "default": SHOW,
        "current": SHOW
    },
    "emphasis": {
        "default": EMPHASIS,
        "current": EMPHASIS
    },
    "color": {
        "default": COLOR,
        "current": COLOR
    },
    "normal": {
        "default": NORMAL,
        "current": NORMAL
    },
    "char_sep": {
        "default": CHAR_SEP,
        "current": CHAR_SEP
    },
    "word_sep": {
        "default": WORD_SEP,
        "current": WORD_SEP
    }
}

nato_speech_config = {
    "speak": {
        "default": SPEAK,
        "current": SPEAK
    },
    "male": {
        "default": MALE,
        "current": MALE
    },
    "lang": {
        "default": LANG,
        "current": LANG
    },
    "dialect": {
        "default": DIALECT,
        "current": DIALECT
    },
    "lang_check": {
        "default": LANG_CHECK,
        "current": LANG_CHECK
    },
    "speed": {
        "default": SPEED,
        "current": SPEED
    },
    "pause": {
        "default": PAUSE,
        "current": PAUSE
    },
    "speech_file": {
        "default": SPEECH_FILE,
        "current": SPEECH_FILE
    }
}


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
    for word in text.split(nato_speech_config["pause"]["current"]):
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
    if text:
        gTTS(text,
             lang=nato_speech_config["lang"]["current"],
             tld=nato_speech_config["dialect"]["current"],
             lang_check=nato_speech_config["lang_check"]["current"],
             slow=nato_speech_config["speed"]["current"]).save(nato_speech_config["speech_file"]["current"])
        with open(nato_speech_config["speech_file"]["current"]) as tts_file:
            mixer.init()
            mixer.music.load(nato_speech_config["speech_file"]["current"])
            mixer.music.play()
            sleep(MP3(nato_speech_config["speech_file"]["current"]).info.length)
            mixer.music.stop()
            mixer.stop()
            mixer.quit()


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
            nato_show += nato_text_config["emphasis"]["current"] + nato_text_config["color"]["current"] + " " + \
                         SYMBOLS[c.lower()]["nato"] + " " + nato_text_config["normal"]["current"]
            nato_speak += " " + SYMBOLS[c.lower()]["nato"] + " "
            spaced = False
        if c.isspace() and not spaced:
            nato_show += "   "
            nato_speak += nato_speech_config["pause"]["current"]
            spaced = True
    print(nato_show.strip())
    if nato_speech_config["speak"]["current"]:
        if nato_speech_config["male"]["current"]:
            windows_voice(nato_speak)
        elif nato_speak:
            try:
                google_voice(nato_speak)
            except (ValueError, RuntimeError):
                windows_voice(nato_speak)


def convert_to_nato(text, option="plain"):
    """
    Converts the text into NATO Phonetics and returns a string with the correct format depending on the option.

    The possible options are "plain", "formatted", and "speech"
    "plain" is the default option and is not required to specify. If any other option is provided it will be
    treated as "plain".

    If the option is "formatted" then the NATO Phonetics string returned is formatted with the ANSI Escape codes for
    emphasis, text colors, and background colors configured by the text_config["emphasis"]["current"] and
    text_config["color"]["current"] configuration parameters.
    If the option is "speech" then the NATO Phonetics string returned is formatted with the correct characters
    to be used in a text to speech engine.

    :param text: str :
        The text that is converted into NATO Phonetics.
    :param option: str :
        The options available are "plain" (default), "formatted", or "speech"

    :return: str :
        The NATO Phonetics string with the correct format depending on the option parameter.
    """
    nato_str = ""
    spaced = False
    for c in text.strip():
        if c.lower() in SYMBOLS:
            if option == "formatted":
                nato_str += nato_text_config["emphasis"]["current"] + nato_text_config["color"]["current"] + \
                            nato_text_config["char_sep"]["current"] + \
                            SYMBOLS[c.lower()]["nato"] + \
                            nato_text_config["char_sep"]["current"] + nato_text_config["normal"]["current"]
            else:
                nato_str += nato_text_config["char_sep"]["current"] + \
                            SYMBOLS[c.lower()]["nato"] + \
                            nato_text_config["char_sep"]["current"]
            spaced = False
        if c.isspace() and not spaced:
            if option == "speech":
                nato_str += nato_speech_config["pause"]["current"]
            else:
                nato_str += nato_text_config["word_sep"]["current"]
            spaced = True
    return nato_str.strip()


def speak_nato(text):
    """
    Speaks the NATO Phonetics of the text.

    The function converts the text string that is passed to the function into NATO Phonetics and speaks it.

    It is possible to choose between a male or a female voice by setting the configuration parameter
    speech_config["male"]["current"] to True or False.

    :param text: str :
        The text that is to be converted into NATO Phonetics and spoken.

    :return:
    """
    if nato_speech_config["male"]["current"]:
        windows_voice(convert_to_nato(text, "speech"))
    else:
        try:
            google_voice(convert_to_nato(text, "speech"))
        except (ValueError, RuntimeError):
            windows_voice(convert_to_nato(text, "speech"))


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
