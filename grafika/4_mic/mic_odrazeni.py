import pyglet

window = pyglet.window.Window(width=1000, height=700)
micek = pyglet.image.load("./obrazky/micek.png")

# (1) TODO: Vytvorit tridu Micek. Obsahovat bude odkaz na objekt na platne a rychlost tohoto objektu na obou osach rychlost_x a rychlost_y
# (2) TODO: Rychlost na obou osach prijimat jako parametr


objekty = []
# (3) TODO: Do seznamu objektu vlozit instanci objektu Micek

def vykresli():
    window.clear()

    # (4) TODO: Vykresli vsechny elementy ze seznamu objektu. (Teckovou notaci se dostaneme k jakekoliv vlastnosti objektu)

def pohyb(t):
    # (5) TODO: Pri kazdem tiku posunu kazdy z elementu na ose X i Y
    # (6) TODO: Pokud se element dostane na okraj okna, odrazi se (take na obou osach)


pyglet.clock.schedule_interval(pohyb, 1/60)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()

# (BONUS) TODO: Do pohybu zakomponujte i gravitaci (micky budou stale vice pritahovany k zemi)
# (BONUS) TODO: Pro velmi sikovne jedince: muzete doprogramovat kontrolu, ktera vyresi srazku dvou micku
