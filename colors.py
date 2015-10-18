ENDC = '\033[0m'
def thought(string):
    return '\033[36m(%s)\033[0m \b' % string
def special(string):
    return '\033[31m\033[1m%s\033[0m \b' % string
def green(string):
    return '\033[32m\033[1m%s\033[0m \b' % string
def bold(string):
    return '\033[1m%s\033[0m \b' % string