import pyglet
window = pyglet.window.Window(width=1000, height=700)

def tik(t):
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)

obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek)

def vykresli():
    window.clear()
    had.draw()
    had.x = window.width / 2 - 40
    had.y = window.height / 2 - 40
    had.rotation = 30

window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
)

pyglet.app.run()
