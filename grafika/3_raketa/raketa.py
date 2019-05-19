import pyglet
from math import sin

PRODLEVA_PRED_STARTEM = 1.3
PRODLEVA_PRED_SPUSTENIM_MOTORU = 0.9
OBNOVOVACI_FREKVENCE = 1/60.  # 1/5.
RYCHLOST_HORENI = 0.01
RYCHLOST = 4

window = pyglet.window.Window(width=1000, height=700, caption="Start rakety")

raketa_on = pyglet.image.load('./obrazky/raketa_on.png')
raketa_off = pyglet.image.load('./obrazky/raketa_off.png')

raketa = pyglet.sprite.Sprite(raketa_off)
raketa.x = window.width / 2
raketa.y = 0

@window.event
def vykresli():
    # (1) TODO: Vycisti okno pomoci funkce clear()

    # (2) TODO: Vykresli na okno raketu

    pass

def odstartuj(t):  # dt - zpozdeny start
    # (5) TODO: naplanuj spusteni funkce let. Cetnost obnoveni viz OBNOVOVACI_FREKVENCE

    pass

def rotace_rakety(vyska):
    return sin(vyska / 4)

def let(t):  # dt - zpozdeny start
    # (6) TODO: Dokud raketa nevyleti z obrazovky, kazdy tik (spusteni funkce let) se posune o hodnotu RYCHLOST vzhuru

    # (7) TODO: Pokud raketa vyleti z obrazovky, nastavte ji vysku 0, aby se objevila opet dole


    # (11) TODO: Behem letu se raketa bude pusobenim sil klepat. To provedeme jeji drobnou rotaci. Vypocet provadi funkce rotace_rakety

    pass

def horeni_zapni(t):
    # (9) TODO: U rakety zapneme motory nastavenim obrazku raketa_on. Naplanujeme take spusteni funkce horeni_vypni

    pass

def horeni_vypni(t):
    # (10) TODO: U rakety vypneme motory nastavenim obrazku raketa_off. Naplanujeme take spusteni funkce horeni_zapni

    pass

# (3) TODO: Ihned po otevreni okna spoustet funkci "vykresli"

# (8) TODO: Naplanovat zapnuti motoru po uplynuti casu PRODLEVA_PRED_SPUSTENIM_MOTORU

# (4) TODO: Naplanovat spusteni fce "odstartuj" po uplynuti casu PRODLEVA_PRED_STARTEM.


# (BONUS) TODO: Upravit vlastnosti letu tak, aby raketa pri startu mirne zatacela vpravo (az po odstartovani) :)
# (BONUS) TODO: Stahnout obrazek vesmirneho centra a vlozit ho za raketu jako pozadi


pyglet.app.run()
