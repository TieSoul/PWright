from time import sleep
music = None
sfx = None
trackName = None
try:
    import sfml.audio as sf
except ImportError:
    print("PySFML is needed for this game.")
    raw_input()
    exit()
def playMusic(name):
    global music, trackName
    trackName = name
    music.stop() if music else None
    music = sf.Music.from_file(name)
    music.loop = True
    music.play()

def playSFX(name):
    global sfx
    sfx = sf.Sound()
    sfx.buffer = sf.SoundBuffer.from_file(name)
    sfx.play()
    sleep(sfx.buffer.duration.seconds)


def stopMusic():
    global music
    music.stop() if music else None

def getMusic():
    global trackName
    return trackName