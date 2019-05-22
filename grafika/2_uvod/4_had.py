import math

import pyglet

window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    had.x = 150
    had.rotation = had.rotation + 10

obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek, x=10, y=10)

def vykresli():
    window.clear()
    had.draw()

def klik(x, y, tlacitko, mod):
    print(tlacitko, mod)
    had.x = x
    had.y = y

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik,
)

obrazek2 = pyglet.image.load('had2.png')

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

pyglet.clock.schedule_once(zmen, 0.2)

pyglet.app.run()
