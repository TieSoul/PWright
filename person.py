class Person:
    def __init__(self, name, talks, attrs):
        self.talks = talks
        self.name = name
        self.talk = attrs['talk']
        self.present = attrs['present']
        self.alreadyTalked = []

    def change(self, attr):
        if attr[0] == 'talk':
            self.talk[attr[1]] = attr[2]
            if attr[1] in self.alreadyTalked:
                self.alreadyTalked.remove(attr[1])
        else:
            self.present[attr[1]] = attr[2]