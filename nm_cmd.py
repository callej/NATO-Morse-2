from nato import convert_to_nato, speak_nato
from morse import send_morse


def main():
    """
    Asks for a word or phrase, converts it to NATO Phonetics and Morse Code, displays the result on the screen and
    plays it in the speakers.
    :return: Nothing is returned.
    """
    text = input("Enter a word or a phrase: ")
    print(convert_to_nato(text, "formatted"))
    speak_nato(text)
    send_morse(text)


if __name__ == "__main__":
    main()
