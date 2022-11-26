from winsound import Beep
from time import sleep
from win32com.client import Dispatch
from symbols import SYMBOLS

# ***   Text Properties   *** #
BOLD = "\x1b[1m"
TXT = "\x1b[38;2;0;0;210;48;2;212;175;55m"
NORMAL = "\x1b[m"

# ***   Morse Properties   *** #
DOT = 1
DASH = 3
SYMBOL_SPACE = 1
LETTER_SPACE = 3
WORD_SPACE = 7
WPM = 20                        # Words per minute (PARIS)
DOT_DURATION = 1200 / WPM      # Duration in milli seconds
FREQ = 400


def print_nato(text):
    print()
    nato_show = ""
    nato_word = ""
    nato_speak = []
    spaced = False
    for c in text.strip():
        if c.lower() in SYMBOLS:
            nato_show += BOLD + TXT + " " + SYMBOLS[c.lower()]["nato"] + " " + NORMAL
            nato_word += " " + SYMBOLS[c.lower()]["nato"] + " "
            spaced = False
        if c.isspace() and not spaced:
            nato_show += "   "
            nato_speak.append(nato_word.strip())
            nato_word = ""
            spaced = True
    if not spaced and nato_word != "":
        nato_speak.append(nato_word.strip())
    print(nato_show.strip())
    speak = Dispatch("SAPI.SpVoice")
    for word in nato_speak:
        speak.Speak(word)


def send_code(symbol):
    for sound in SYMBOLS[symbol.lower()]["morse"]:
        if sound == ".":
            Beep(FREQ, int(DOT * DOT_DURATION))
        else:
            Beep(FREQ, int(DASH * DOT_DURATION))
        sleep(SYMBOL_SPACE * DOT_DURATION / 1000.0)


def send_morse(text):
    print()
    spaced = False
    for c in text.strip():
        if c.lower() in SYMBOLS:
            print(f'{c}: {SYMBOLS[c.lower()]["morse"]}')
            send_code(c)
            sleep((LETTER_SPACE - SYMBOL_SPACE) * DOT_DURATION / 1000.0)
            spaced = False
        if c.isspace() and not spaced:
            print()
            sleep((WORD_SPACE - LETTER_SPACE) * DOT_DURATION / 1000.0)
            spaced = True


def main():
    text = input("Enter a word or a phrase: ")
    print_nato(text)
    send_morse(text)


if __name__ == "__main__":
    main()
