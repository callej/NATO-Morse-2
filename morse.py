from winsound import Beep
from time import sleep
from symbols import SYMBOLS


# ***   Morse Properties   *** #
PLAY_MORSE = True
DOT = 1
DASH = 3
SYMBOL_SPACE = 1
LETTER_SPACE = 3
WORD_SPACE = 7
WPM = 20                    # Words per minute (PARIS)
DOT_DURATION = 1200 / WPM   # Duration in milli seconds
FREQ = 400
VISUAL = True
AUDIO = True


def send_code(symbol):
    """
    Converts the symbol string passed to sound sent to the speakers.

    The parameter symbol is a string that consists only of dots and dashes. If the character is a dot it is converted
    to s short beep. Otherwise, the character is converted to a long beep. The lengths of the beeps are configured by
    the global parameters DOT, DASH, and DOT_DURATION.

    :param symbol: str :
            The text string of dots and dashes that is converted to short and long beeps.

    :return: Nothing is returned.
    """
    for sound in SYMBOLS[symbol.lower()]["morse"]:
        if sound == ".":
            Beep(FREQ, int(DOT * DOT_DURATION))
        else:
            Beep(FREQ, int(DASH * DOT_DURATION))
        sleep(SYMBOL_SPACE * DOT_DURATION / 1000.0)


def send_morse(text):
    """
    Converts the text to Morse code and plays it in the speakers.

    :param text: str,
        The text string that is being converted to Morse code.

    :return: Nothing is returned.
    """
    if PLAY_MORSE:
        if VISUAL:
            print()
        spaced = False
        for c in text.strip():
            if c.lower() in SYMBOLS:
                if VISUAL:
                    print(f'{c}: {SYMBOLS[c.lower()]["morse"]}')
                if AUDIO:
                    send_code(c)
                    sleep((LETTER_SPACE - SYMBOL_SPACE) * DOT_DURATION / 1000.0)
                spaced = False
            if c.isspace() and not spaced:
                if VISUAL:
                    print()
                if AUDIO:
                    sleep((WORD_SPACE - LETTER_SPACE) * DOT_DURATION / 1000.0)
                spaced = True


def main():
    """
    Asks for a word or phrase, converts it to Morse Code, displays the result on the screen and
    plays it in the speakers.
    :return: Nothing is returned.
    """
    text = input("Enter a word or a phrase: ")
    send_morse(text)


if __name__ == "__main__":
    main()
