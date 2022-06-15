from ursina import *
import random as r

app = Ursina()
window.fullscreen = True
window.color = color.white

redcube = Entity(model="cube",color=color.red)

def input(key):
    if key == 'space':
        redcube.rotation_z += 50

app.run()