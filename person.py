class Person:
    def __init__(self, name, talks, attrs):
        self.talks = talks
        self.name = name
        self.talk = attrs['talk']
        self.present = attrs['present']

    def change(self, attr):
        if attr[0] == 'talk':
            self.talk[attr[1]] = attr[2]
        else:
            self.present[attr[1]] = attr[2]