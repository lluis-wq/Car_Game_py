from interficie import *
from Finalitzacio import *


def partida():
    juguem_de_nou = True
    while juguem_de_nou:
        mode_escollit = crearMenu()
        if mode_escollit == 0:
            break
        elif mode_escollit == 4:
            continue
        else:
            dades_finals = animacio(mode_escollit)
            juguem_de_nou = crearFinal(dades_finals)
    
    return
    
