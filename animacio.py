from tkinter import *
import time
import keyboard

from Lectura_json import *
from Cotxe import *
from Carretera import *
from Meta import *
from VPoint import *
from WPoint import *
from WorldView import *


def animacio(par):
    tk=Tk()
    w=Canvas(tk,width=800,height=600)
    w.pack()

    marcador = Label(tk, text="Preparats..., Llestos...", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    marcador.place(x=550,y=10)

    tanca_joc = Label(tk, text="Premi la tecla 'esc' per sortir", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    tanca_joc.place(x=10,y=10)

    wv=WorldView(WPoint(1200,1400),WPoint(1700,1400+500*6/8),
                VPoint(0,0),VPoint(800,600))

    lectura = lectura_json("Pràctica_Cotxe/carretera.json") 
    cotxes_humans = lectura[0]
    cotxes_automatics = lectura[1]
    carretera = lectura[2]
    meta = lectura[3]
    trams_visitats = [False for _ in range(12)]

    while True:
        w.delete("all")
        
        punts_previs = None
        for s in carretera:
            if(punts_previs==None):
                punts_previs = s.pinta(w,wv)
            else:
                punts_previs = s.pinta(w,wv,punts_previs)
        for m in meta:
            m.pinta(w,wv)

            
        a=0
        if keyboard.is_pressed("left arrow"):
            a=1
        if keyboard.is_pressed("right arrow"):
            a=-1
            
        b=0
        if keyboard.is_pressed("up arrow"):
            b=1
        if keyboard.is_pressed("down arrow"):
            b=-1
        
        if keyboard.is_pressed("esc"):
            par = par + 3
            
        cotxes_humans[0].mou_gir_huma(a)
        trams_visitats = cotxes_humans[0].mou_translacio_huma(b,carretera,cotxes_automatics,trams_visitats,w,wv)
        trams_visitats = meta[0].voltes(cotxes_humans[0],marcador,trams_visitats,par)

        for c in cotxes_automatics:
            c.mou(carretera)
            
        for c in cotxes_humans:
            c.pinta(w,wv)
        for c in cotxes_automatics:
            c.pinta(w,wv)

        if trams_visitats[0] == 4 or trams_visitats[0] == 2 or trams_visitats[0] == 3:
            dades_finals = trams_visitats
            tk.destroy()
            return dades_finals
        w.update()
        
        
        time.sleep(50/1000)
    
    
