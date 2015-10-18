from colors import *
class Evidence:
    cr = []
    def __init__(self, name, desc, silent):
        self.name = name
        self.desc = desc
        Evidence.cr.append(self)
        if not silent:
            print("\nEvidence added: %s" % name)
            print(bold(name))
            print(desc + "\n")

class Profile:
    pf = []
    def __init__(self, name, desc, silent):
        self.name = name
        self.desc = desc
        Profile.pf.append(self)
        if not silent:
            print("\nEvidence added: %s" % name)
            print(bold(name))
            print(desc + "\n")