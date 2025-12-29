import json

from Cotxe import *
from Carretera import *
from Meta import *

def lectura_json(fitxer):
    f=open(fitxer,"r")
    dades=json.load(f)
    f.close()

    cotxes_humans=[]
    for c in dades['human_cars']:
        c1=Cotxe(c['start_position']['x'],c['start_position']['y'],c['width'],c['height'],c['angle'],c['velocity'],c['colour'])
        cotxes_humans.append(c1)
    cotxes_automatics = []
    for c in dades['automatic_cars']:
        c1=Cotxe(c['start_position']['x'],c['start_position']['y'],c['width'],c['height'],c['angle'],c['velocity'],c['colour'])
        cotxes_automatics.append(c1)
    carretera=[]
    for s in dades['sections']:
        s1 = Carretera(s['position']['x'],s['position']['y'],s['angle'],s['height'],s['distance'],s['id'])
        carretera.append(s1)
    meta = []
    for m in dades['finish_line']:
        m1 = Meta(m['position']['x'],m['position']['y'],m['width'],m['height'])
        meta.append(m1)
    return cotxes_humans,cotxes_automatics,carretera,meta
