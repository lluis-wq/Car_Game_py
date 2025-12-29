from interficie1 import *
from interficie2 import *
from Finalitzacio import *
from animacio import *


def partida():
    juguem_de_nou = True
    while juguem_de_nou:
        num_jugadors = crearSeleccions()
        mode_escollit = crearMenu()
        if mode_escollit == 0:
            break
        elif mode_escollit == 4:
            continue
        else:
            if num_jugadors == 1:
                dades_finals = animacio(mode_escollit)
            else:
                dades_finals = animacioMultijugador(mode_escollit)
            juguem_de_nou = crearFinal(dades_finals)
    
    return
    
