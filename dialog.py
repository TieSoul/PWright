from __future__ import print_function
import re, os
from time import sleep
from colors import *
if os.name == 'nt':
    import msvcrt


if os.name == 'nt':
    import colorama
    colorama.init()

DELAY = 0.05
EXTRADELAY = 0.1
PERSON = ''

def changeSpeed(delay, extradelay):
    global DELAY, EXTRADELAY
    DELAY = delay
    EXTRADELAY = extradelay


def dialog(person, text, autoEnd=False, pauses=None, autoPause=True):
    if text[-1] == "}":
        text += " \b"
    text = text.replace("g{", "\033[32m\033[1m").replace("r{", "\033[31m\033[1m").replace("}", "\033[0m")\
               .replace("b{", "\033[36m").replace("B{", "\033[1m")
    global DELAY, EXTRADELAY, PERSON
    if person != PERSON:
        print("\n", end="")
    color = ''
    ps = pauses if pauses is not None else []
    pt = re.compile(r'[a-zA-Z]')
    print(person + ":", end=' ') if not person == '' else None
    i = 0
    if not os.name == 'nt':
        os.system('stty -echo')
    while i in range(len(text)):
        while text[i] == '\033':
            if text[i + 2] == '0':
                if len(color) > 0 and color[-2] == '1' and color[-3] == '[':
                    color = color[:color.rindex("\033")]
                color = color[:color.rindex("\033")]
            else:
                color += text[i:text[i:].index('m') + i + 1]
            l = text[i:].index('m')
            text = text[:i] + text[text[i:].index('m') + i + 1:]
            ps = [i-l for i in ps]
        print(color + text[i] + ENDC, end='')
        sleep(DELAY)
        if (text[i] in ['.', ',', '!', '?']
                and not i >= len(text) - 1
                and not text[i + 1] in ['.', ',', '!', '?']
                and re.findall(pt, text[i:])
                and autoPause) \
                or i in ps:
            sleep(EXTRADELAY)
        i += 1
    raw_input() if not autoEnd else None
    PERSON = person
    if autoEnd:
        print("\n", end="")