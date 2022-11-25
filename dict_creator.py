

NATO = [
        "Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
        "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
        "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo",
        "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
        "Xray", "Yankee", "Zulu"
    ]

NDIG = [
        "Zero", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"
    ]

MORSE = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
        "..", ".---", "-.-.", ".-..", "--", "-.", "---", ".--.",
        "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
        "-.--", "--.."
    ]

MDIG = [
        "-----", ".----", "..---", "...--", "....-",
        ".....", "-....", "--...", "---..", "----."
    ]


def main():
    symbols = '{\n'
    for c in range(ord('a'), ord('z') + 1):
        symbols += f'    "{chr(c)}": {{\n'
        symbols += f'        "nato": "{NATO[c - ord("a")]}",\n'
        symbols += f'        "morse": "{MORSE[c - ord("a")]}"\n'
        symbols += f'    }},\n'
    for n in range(0, 10):
        symbols += f'    "{n}": {{\n'
        symbols += f'        "nato": "{NDIG[n]}",\n'
        symbols += f'        "morse": "{MDIG[n]}"\n'
        symbols += f'    }},\n'
    symbols = symbols[:-2] + '\n}'
    print(symbols)


if __name__ == "__main__":
    main()
