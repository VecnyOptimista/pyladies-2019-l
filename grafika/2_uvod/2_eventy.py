import pyglet
window = pyglet.window.Window()

def zpracuj_text(text):
    print('Stisknuto:',text)

window.push_handlers(on_text=zpracuj_text)

pyglet.app.run()
