from ursina import *
import random as r

app = Ursina()
window.fullscreen = True
window.color = color.white


dino = Animation('assets\dino',
                 collider='box',
                 x=-5)

def input(key):
  if key == 'space':
    if dino.y < 0.01:
      dino.animate_y(
        2,
        duration=0.4,
        curve= curve.out_sine
      )
      dino.animate_y(
        0,
        duration=0.4,
        delay=0.4,
        curve = curve.in_sine
      )

app.run()