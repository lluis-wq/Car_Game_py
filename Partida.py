from interficie1 import *
from interficie2 import *
from Finalitzacio import *
from animacio import *


def partida():
    juguem_de_nou = True
    while juguem_de_nou:
        num_jugadors = crearSeleccions()
        mode_escollit = crearMenu()
        if mode_escollit[0] == 0:
            break
        elif mode_escollit[0] == 4:
            continue
        else:
            if mode_escollit[1] == 0:
                break
            
            if num_jugadors == 1:
                dades_finals = animacio(mode_escollit[0],mode_escollit[1])
            else:
                dades_finals = animacioMultijugador(mode_escollit[0],mode_escollit[1])
            juguem_de_nou = crearFinal(dades_finals,num_jugadors)
    
    return
    
