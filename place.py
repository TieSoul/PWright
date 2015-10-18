class Place:
    def __init__(self, name, attrs):
        self.name = name
        self.move = attrs['move']
        self.examine = attrs['examine']
        self.desc = attrs['desc']
        self.when = attrs['when']
        self.person = attrs['person']
        self.enter = attrs['enter']
        self.entered = False
        self.music = attrs['music']

    def change(self, attr):
        if attr[0] == 'move':
            self.move.append(attr[1])
        elif attr[0] == 'examine':
            for i in attr[1]:
                self.examine[i] = attr[2]
        elif attr[0] == 'desc':
            self.desc = attr[1]
        elif attr[0] == 'person':
            self.person = attr[1]
        elif attr[0] == 'enter':
            self.enter = attr[1]
            self.entered = False
        elif attr[0] == 'music':
            self.music = attr[1]