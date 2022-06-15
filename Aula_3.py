from ursina import *
import random as r

app = Ursina()
window.color = color.white

dino = Animation('assets\dino', collider='box', x=-5)

ground1 = Entity(      #criamos o objeto chão, com os parametros de modelo (quadrado), textura, escala e ordem do eixo z
  model='quad',
  texture='assets\ground',
  scale=(50,0.5,1),
  z=1
)
ground2 = duplicate(ground1, x=50) #clone do ground1, porém 50 pontos no eixo x pra direita.
pair = [ground1, ground2]  #criamos um array de dois chãos que ficam lado a lado para que possam se repetir

def update():
  for ground in pair:
    ground.x -= 6*time.dt #chao se move para a esquerda no eixo X ao ser subtraído pela velocidade, essa que é determinada pelo tempo. Ela Pode ser multiplicada, no caso, por 6
    if ground.x < -35:
      ground.x += 100

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