import sys, os
from dialog import *
from part import *

if sys.version_info[0] > 2:
    print("Your version of Python is not supported by this game. Please use a Python version lower than 3.0.")
    raw_input()
    exit()

sys.stderr = open('error.log', 'w')
if __name__ == '__main__':
    if len(sys.argv) > 1:
        x = parse(open(sys.argv[1]).read())
        interp_stmts(x, filename=sys.argv[1])
        exit()
    settings = shelve.open('settings.shelf')
    if 'delay' in settings and 'extradelay' in settings:
        changeSpeed(settings['delay'], settings['extradelay'])
    filename = ''
    print "Choose an option: "
    print "0) Settings"
    print "1) Phoenix Wright: Ace Attorney"
    print "2) Phoenix Wright: Ace Attorney: Justice For All"
    print "3) Phoenix Wright: Ace Attorney: Trials & Tribulations"
    print "4) Apollo Justice: Ace Attorney"
    print "5) Phoenix Wright: Ace Attorney: Dual Destinies"
    print "6) Ace Attorney Investigations: Miles Edgeworth"
    print "7) Ace Attorney Investigations: Miles Edgeworth: Prosecutor's Path (Gyakuten Kenji 2)"
    i = ''
    while not (i.isdigit() and 0 < int(i) <= 7):
        i = raw_input('> ')
        if i == '0':
            print "Change Text Speed: "
            print "0) Slow"
            print "1) Default"
            print "2) Fast"
            print "3) Instant"
            j = ''
            while not (j.isdigit() and 0 <= int(j) <= 3):
                j = raw_input('> ')
            if int(j) == 0:
                changeSpeed(0.075, 0.15)
                settings['delay'] = 0.075
                settings['extradelay'] = 0.15
            elif int(j) == 1:
                changeSpeed(0.05, 0.1)
                settings['delay'] = 0.05
                settings['extradelay'] = 0.1
            elif int(j) == 2:
                changeSpeed(0.025, 0.05)
                settings['delay'] = 0.025
                settings['extradelay'] = 0.05
            elif int(j) == 3:
                changeSpeed(0, 0)
                settings['delay'] = 0
                settings['extradelay'] = 0
            print "Choose an option: "
            print "0) Settings"
            print "1) Phoenix Wright: Ace Attorney"
            print "2) Phoenix Wright: Ace Attorney: Justice For All"
            print "3) Phoenix Wright: Ace Attorney: Trials & Tribulations"
            print "4) Apollo Justice: Ace Attorney"
            print "5) Phoenix Wright: Ace Attorney: Dual Destinies"
            print "6) Ace Attorney Investigations: Miles Edgeworth"
            print "7) Ace Attorney Investigations: Miles Edgeworth: Prosecutor's Path (Gyakuten Kenji 2)"
    if int(i) == 1:
        print "Choose an option: "
        print "1) The First Turnabout"
        print "2) Turnabout Sisters"
        print "3) Turnabout Samurai"
        print "4) Turnabout Goodbyes"
        print "5) Rise From The Ashes"
        i = ''
        while not (i.isdigit() and 0 < int(i) <= 5):
            i = raw_input('> ')
        if int(i) == 1:
            filename = 'cases/GS1/The First Turnabout/first.pw'
        elif int(i) == 2:
            filename = 'cases/GS1/Turnabout Sisters/sisters.pw'
        else:
            print "This case is coming Soon(TM)!"
            exit()
    else:
        print "This game is coming Soon(TM)!"
        exit()

    import os.path
    index = 0
    shelf = None
    if os.path.isfile(filename[:filename.index('.')] + '.shelf'):
        shelf = shelve.open(filename[:filename.index('.')] + '.shelf')
    from parse import parse
    x = parse(open(filename).read())
    interp_stmts(x, shelf=shelf, filename=filename)