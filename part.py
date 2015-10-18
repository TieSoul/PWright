from dialog import *
from music import *
from evidence import *
from parse import parse
import shelve
from place import Place
from person import Person

credibility = 5

names = {}
testimony = []
objection = ''
holdit = ''
takethat = ''
currplace = None
track = ''

def condition(cond):
    global currplace
    for i in cond:
        if i[0] == 'name':
            if i[1] in names:
                if not names[i[1]]:
                    return False
            else:
                return False
        if i[0] == 'not':
            if i[1] in names:
                if names[i[1]]:
                    return False
        if i[0] == 'place':
            if i[1] in names:
                if currplace is not names[i[1]]:
                    return False
            else:
                return False

    return True


def penalize(amount=1):
    global credibility
    credibility -= amount
    print bold("Penalty! Remaining credibility: " + str(credibility) + "/5")

def interp_stmt(stmt, depth):
    global names, testimony, objection, holdit, takethat, currplace, track
    x = stmt[0]
    if x == 'music':
        track = stmt[1]
        if track == 'stop':
            stopMusic()
        else:
            try:
                playMusic('music/' + track + '.wav')
            except IOError:
                print "ERROR: Music track " + track + " cannot be found."
    elif x == 'sfx':
        effect = stmt[1]
        try:
            playSFX('music/' + effect + '.wav')
        except IOError:
            print "ERROR: Sound effect " + effect + " cannot be found."
    elif x == 'dialog':
        dialog(*stmt[1:])
    elif x == 'question':
        print stmt[1]
        for i in stmt[2]:
            print str(stmt[2].index(i)+1) + ') ' + i
        i = ''
        while not (i.isdigit() and 0 < int(i) <= len(stmt[2])):
            i = raw_input('> ')
            if i == 'cr':
                print bold("Evidence:")
                for evidence in Evidence.cr:
                    print evidence.name
                print bold("Profiles:")
                for profile in Profile.pf:
                    print profile.name
                print "Please type 'show (evidence name)' for more info about a piece of evidence or a profile."
            elif i.split(' ')[0] == 'show':
                name = i[5:].lower()
                x = None
                for j in Evidence.cr:
                    if name in j.name.lower():
                        x = j
                        break
                if not x:
                    for j in Profile.pf:
                        if name in j.name.lower():
                            x = j
                            break
                if x:
                    print bold(x.name)
                    print x.desc
                else:
                    print "Profile or evidence " + name + " not found."
            elif i == 'save':
                print "This will save and quit the game. Are you sure? (y/n)"
                j = ''
                while not j.lower() in ['y', 'n', 'yes', 'no']:
                    j = raw_input()
                if j.lower()[0] == 'y':
                    return 'save'

        answer = stmt[3][int(i)]
        if answer[0] != 'continue':
            r = interp_stmts(answer, depth+1)
            if r is True:
                interp_stmt(stmt, depth)
            elif r == 'save':
                return 'save'
    elif x == 'return':
        return True
    elif x == 'continue':
        return False
    elif x == 'penalize':
        penalize(1)
        if credibility == 0:
            print "Game over."
            exit()
    elif x == 'sleep':
        sleep(stmt[1]/1000.0)
    elif x == 'cutscene':
        dialog('', stmt[1], autoEnd=True)
    elif x == 'think':
        dialog(stmt[1], thought(stmt[2]))
    elif x == 'cls':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif x == 'add':
        if stmt[1] == 'PROFILE':
            if not (stmt[-1] in names and names[stmt[-1]].name == stmt[2]):
                names[stmt[-1]] = Profile(*stmt[2:-1])
        else:
            if not (stmt[-1] in names and names[stmt[-1]].name == stmt[2]):
                names[stmt[-1]] = Evidence(*stmt[2:-1])
    elif x == 'testimony':
        print bold("Witness Testimony: " + stmt[1])
        testimony = stmt[1:]
        for i in testimony[2]:
            dialog(stmt[2], i)
    elif x == 'cross-examination':
        statements = testimony[2]
        person = testimony[1]
        title = testimony[0]
        print bold("Cross-Examination: " + title)
        presses = stmt[1]['press']
        presents = stmt[1]['present']
        currstatement = 1
        while True:
            dialog(person, green(statements[currstatement-1]))
            i = raw_input('> ')
            if i == 'save':
                print "This will save and quit the game. Are you sure? (y/n)"
                j = ''
                while not j.lower() in ['y', 'n', 'yes', 'no']:
                    j = raw_input()
                if j.lower()[0] == 'y':
                    return 'save'
            elif i == 'press':
                if currstatement in presses:
                    playSFX(holdit)
                    x = interp_stmts(presses[currstatement], depth+1)
                    if x == 'next' or x is None:
                        currstatement += 1
                        if currstatement > len(statements):
                            currstatement = 1
                            if 'end' in stmt[1]:
                                interp_stmts(stmt[1]['end'], depth+1)
                    elif x is False:
                        return None
                    elif x == 'save':
                        return 'save'
            elif i.split(' ')[0] == 'present':
                name = i[8:].lower()
                x = None
                for j in Evidence.cr:
                    if name in j.name.lower():
                        x = j
                        break
                if not x:
                    for j in Profile.pf:
                        if name in j.name.lower():
                            x = j
                            break
                if x:
                    playSFX(objection)
                    if currstatement in presents:
                        print presents[currstatement]
                        for key in presents[currstatement]:
                            if names[key].name == x.name:
                                x = interp_stmts(presents[currstatement][key], depth+1)
                                break
                        else:
                            x = interp_stmts(presents['default'], depth+1)
                    else:
                        x = interp_stmts(presents['default'], depth+1)
                    if x == 'next' or x is None:
                        currstatement += 1
                        if currstatement > len(statements):
                            currstatement = 1
                            if 'end' in stmt[1]:
                                interp_stmts(stmt[1]['end'], depth+1)
                    elif x is False:
                        return None
                    elif x == 'save':
                        return 'save'
                else:
                    print "Profile or evidence " + name + " not found."
            elif i == 'next':
                currstatement += 1
                if currstatement > len(statements):
                    currstatement = 1
                    if 'end' in stmt[1]:
                        interp_stmts(stmt[1]['end'], depth+1)
            elif i == 'prev':
                currstatement -= 1
                if currstatement == 0:
                    currstatement = 1
            elif i == 'cr':
                print bold("Evidence:")
                for evidence in Evidence.cr:
                    print evidence.name
                print bold("Profiles:")
                for profile in Profile.pf:
                    print profile.name
                print "Please type 'show (evidence name)' for more info about a piece of evidence or a profile.\n"
            elif i.split(' ')[0] == 'show':
                name = i[5:].lower()
                x = None
                for j in Evidence.cr:
                    if name in j.name.lower():
                        x = j
                        break
                if not x:
                    for j in Profile.pf:
                        if name in j.name.lower():
                            x = j
                            break
                if x:
                    print bold(x.name)
                    print x.desc
                else:
                    print "Profile or evidence " + name + " not found."
                print ''

    elif x == 'next':
        return 'next'
    elif x == 'objection':
        objection = 'music/' + stmt[1] + '.wav'
    elif x == 'holdit':
        holdit = 'music/' + stmt[1] + '.wav'
    elif x == 'takethat':
        takethat = 'music/' + stmt[1] + '.wav'
    elif x == 'prove':
        print stmt[1]
        while True:
            i = raw_input('> ')
            if i == 'cr':
                print bold("Evidence:")
                for evidence in Evidence.cr:
                    print evidence.name
                print bold("Profiles:")
                for profile in Profile.pf:
                    print profile.name
                print "Please type 'show (evidence name)' for more info about a piece of evidence or a profile."
            elif i.split(' ')[0] == 'show':
                name = i[5:].lower()
                x = None
                for j in Evidence.cr:
                    if name in j.name.lower():
                        x = j
                        break
                if not x:
                    for j in Profile.pf:
                        if name in j.name.lower():
                            x = j
                            break
                if x:
                    print bold(x.name)
                    print x.desc
                else:
                    print "Profile or evidence " + name + " not found."
            elif i == 'save':
                print "This will save and quit the game. Are you sure? (y/n)"
                j = ''
                while not j.lower() in ['y', 'n', 'yes', 'no']:
                    j = raw_input()
                if j.lower()[0] == 'y':
                    return 'save'
            elif i.split(' ')[0] == 'present':
                name = i[8:].lower()
                x = None
                for j in Evidence.cr:
                    if name in j.name.lower():
                        x = j
                        break
                if not x:
                    for j in Profile.pf:
                        if name in j.name.lower():
                            x = j
                            break
                if x:
                    playSFX(takethat)
                    r = None
                    for i in stmt[2]:
                        if i in names and names[i].name == x.name:
                            r = interp_stmts(stmt[2][i])
                            break
                    else:
                        r = interp_stmts(stmt[2]['default'])
                    if r is False:
                        return None
                    elif r == 'save':
                        return 'save'
                else:
                    print "Profile or evidence " + name + " not found."
    elif x == 'if':
        if condition(stmt[1]):
            return interp_stmts(stmt[2])
    elif x == 'ifelse':
        if condition(stmt[1]):
            return interp_stmts(stmt[2])
        else:
            return interp_stmts(stmt[3])
    elif x == 'set':
        names[stmt[1]] = True
    elif x == 'reset':
        names[stmt[1]] = False
    elif x == 'place':
        names[stmt[1]] = Place(stmt[2], stmt[3])
    elif x == 'person':
        names[stmt[1]] = Person(stmt[2], stmt[3], stmt[4])
    elif x == 'changeplace':
        if isinstance(names[stmt[1]], Place):
            place = names[stmt[1]]
            place.change(stmt[2])
    elif x == 'changeperson':
        if isinstance(names[stmt[1]], Person):
            person = names[stmt[1]]
            person.change(stmt[2])
    elif x == 'print':
        print stmt[1]
    elif x == 'start':
        if isinstance(names[stmt[1]], Place):
            currplace = names[stmt[1]]
            while True:
                if not currplace.entered:
                    interp_stmts(currplace.enter, depth+1)
                    currplace.entered = True
                if track != currplace.music:
                    track = currplace.music
                    if track == 'stop':
                        stopMusic()
                    else:
                        try:
                            playMusic('music/' + track + '.wav')
                        except IOError:
                            print "ERROR: Music track " + track + " cannot be found."
                for i in currplace.when:
                    if condition(i[0]):
                        x = interp_stmts(i[1])
                        if x == 'save':
                            return 'save'
                        elif x is False:
                            return None
                inp = raw_input('\n> ')
                if inp == 'cr':
                    print bold("Evidence:")
                    for evidence in Evidence.cr:
                        print evidence.name
                    print bold("Profiles:")
                    for profile in Profile.pf:
                        print profile.name
                    print "Please type 'show (evidence name)' for more info about a piece of evidence or a profile."
                if inp.startswith('show'):
                    name = inp[5:].lower()
                    x = None
                    for j in Evidence.cr:
                        if name in j.name.lower():
                            x = j
                            break
                    if not x:
                        for j in Profile.pf:
                            if name in j.name.lower():
                                x = j
                                break
                    if x:
                        print bold(x.name)
                        print x.desc
                    else:
                        print "Profile or evidence " + name + " not found."
                if inp == 'look' or inp == 'l':
                    print currplace.desc
                elif inp == 'help' or inp == 'h':
                    print """help - show this message
cr - examine the court record
show - look at a certain piece of evidence
look l - look around
examine x - examine something
move m - move around
talk t - talk if a person is here
present p - present if a person is here
save - save your progress and quit the game"""
                elif inp.split(' ')[0] in ['examine', 'x']:
                    for i in currplace.examine.keys():
                        n = ' '.join(inp.split(' ')[1:])
                        if n in i:
                            x = interp_stmts(currplace.examine[i], depth=depth+1)
                            break
                    else:
                        x = interp_stmts(currplace.examine['default'])
                    if x == 'save':
                        return 'save'
                    elif x is False:
                        return None
                elif inp == 'move' or inp == 'm':
                    n = 1
                    for i in currplace.move:
                        print str(n) + ") " + names[i].name
                        n += 1
                    try:
                        place = int(raw_input('move> '))
                    except Exception:
                        place = 0
                    if not place <= 0 and not place >= n:
                        currplace = names[currplace.move[place-1]]
                elif inp == 'talk' or inp == 't':
                    if currplace.person:
                        person = names[currplace.person]
                        n = 1
                        for i in person.talks:
                            if n in person.talk.keys():
                                print str(n) + ") " + i
                            n += 1
                        try:
                            talk = int(raw_input('talk> '))
                        except Exception:
                            talk = 0
                        if not talk <= 0 and not talk >= n and talk in person.talk.keys():
                            x = interp_stmts(person.talk[talk], depth=depth+1)
                            if x == 'save':
                                return 'save'
                            elif x is False:
                                return None
                elif inp.split(' ')[0] in ['present', 'p']:
                    name = ' '.join(inp.split(' ')[1:])
                    x = None
                    for j in Evidence.cr:
                        if name in j.name.lower():
                            x = j
                            break
                    if not x:
                        for j in Profile.pf:
                            if name in j.name.lower():
                                x = j
                                break
                    if x:
                        playSFX(takethat)
                        print bold("TAKE THAT!")
                        r = None
                        person = names[currplace.person]
                        for i in person.present:
                            if i in names and names[i].name == x.name:
                                r = interp_stmts(person.present[i])
                                break
                        else:
                            r = interp_stmts(person.present['default'])
                        if r is False:
                            return None
                        elif r == 'save':
                            return 'save'
                elif inp == 'save':
                    return 'save'
    return None


def interp_stmts(stmts, depth=0, shelf=None, filename=''):
    global testimony, objection, holdit, takethat, names, currplace
    offset = 0
    if not shelf is None:
        stmts = stmts[shelf['state']:]
        offset = shelf['state']
        Evidence.cr = shelf['evidence']
        Profile.pf = shelf['profiles']
        testimony = shelf['testimony']
        objection = shelf['objection']
        takethat = shelf['takethat']
        holdit = shelf['holdit']
        names = shelf['names']
        currplace = shelf['place']
        if shelf['music']:
            playMusic(shelf['music'])
        if currplace:
            offset += 1
            name = None
            for i in names:
                if isinstance(names[i], Place) and names[i].name == currplace.name:
                    currplace = names[i]
                    name = i
            interp_stmt(['start', name], 0)
    for stmt in stmts:
        x = interp_stmt(stmt, depth)
        if not x is None:
            if x == 'save' and depth == 0:
                f = shelve.open(filename[:filename.index('.')] + '.shelf')
                f['evidence'] = Evidence.cr
                f['profiles'] = Profile.pf
                f['state'] = stmts.index(stmt) + offset
                f['music'] = getMusic()
                f['testimony'] = testimony
                f['objection'] = objection
                f['takethat'] = takethat
                f['holdit'] = holdit
                f['names'] = names
                f['place'] = currplace
                return
            return x
        if stmt[0] == 'start':
            currplace = None
    return None

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    from pprint import pprint
    pprint(parse(open(filename).read()))
