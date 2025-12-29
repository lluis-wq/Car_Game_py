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
        trams_visitats = cotxes_humans[0].mou_translacio_huma(b,carretera,cotxes_automatics,trams_visitats,w,wv,1)
        trams_visitats = meta[0].voltes(cotxes_humans[0],marcador,trams_visitats,par)

        for c in cotxes_automatics:
            c.mou(carretera)
            
        cotxes_humans[0].pinta(w,wv)
        for c in cotxes_automatics:
            c.pinta(w,wv)

        if trams_visitats[0] == 4 or trams_visitats[0] == 2 or trams_visitats[0] == 3:
            dades_finals = trams_visitats
            tk.destroy()
            return dades_finals
        w.update()
        
        
        time.sleep(50/1000)


def animacioMultijugador(par):
    tk1=Tk()
    tk1.title("Jugador 1 (Fletxes)")
    tk1.geometry("800x600+0+0")
    w1=Canvas(tk1,width=800,height=600)
    w1.pack()

    tk2=Toplevel(tk1)
    tk2.title("Jugador 2 (WASD)")
    tk2.geometry("800x600+810+0")
    w2=Canvas(tk2,width=800,height=600)
    w2.pack()

    marcador1 = Label(tk1, text="Preparats..., Llestos...", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    marcador1.place(x=550,y=10)

    tanca_joc1 = Label(tk1, text="Premi la tecla 'esc' per sortir", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    tanca_joc1.place(x=10,y=10)

    marcador2 = Label(tk2, text="Preparats..., Llestos...", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    marcador2.place(x=550,y=10)

    tanca_joc2 = Label(tk2, text="Premi la tecla 'esc' per sortir", font=("Helvetica", 10, "bold"), 
                 bg="black", fg="light green", bd=2, relief="ridge", padx=10, pady=5)
    tanca_joc2.place(x=10,y=10)

    wv1=WorldView(WPoint(1200,1400),WPoint(1700,1400+500*6/8),
                VPoint(0,0),VPoint(800,600))
    wv2=WorldView(WPoint(1200,1400),WPoint(1700,1400+500*6/8),
                VPoint(0,0),VPoint(800,600))
    
    lectura = lectura_json("Pràctica_Cotxe/carretera.json") 
    cotxes_humans = lectura[0]
    cotxe_huma_1=cotxes_humans[0]
    cotxe_huma_2=cotxes_humans[1]
    cotxes_automatics = lectura[1]
    carretera = lectura[2]
    meta = lectura[3]
    trams_visitats_1 = [False for _ in range(12)]
    trams_visitats_2 = [False for _ in range(12)]

    while True:
        w1.delete("all")
        w2.delete("all")
        
        punts_previs = None
        for s in carretera:
            if(punts_previs==None):
                punts_previs = s.pinta(w1,wv1)
            else:
                punts_previs = s.pinta(w1,wv1,punts_previs)

        punts_previs = None
        for s in carretera:
            if(punts_previs==None):
                punts_previs = s.pinta(w2,wv2)
            else:
                punts_previs = s.pinta(w2,wv2,punts_previs)

        for m in meta:
            m.pinta(w1,wv1)
            m.pinta(w2,wv2)


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
        d=0
        if keyboard.is_pressed("a"):
            d=1
        if keyboard.is_pressed("d"):
            d=-1
            
        e=0
        if keyboard.is_pressed("w"):
            e=1
        if keyboard.is_pressed("s"):
            e=-1
        
        cotxe_huma_1.mou_gir_huma(a)
        trams_visitats_1 = cotxe_huma_1.mou_translacio_huma(b,carretera,cotxes_automatics,trams_visitats_1,w1,wv1,1,[cotxe_huma_2])

        cotxe_huma_2.mou_gir_huma(d)
        trams_visitats_2 = cotxe_huma_2.mou_translacio_huma(e,carretera,cotxes_automatics,trams_visitats_2,w2,wv2,0,[cotxe_huma_1])

        trams_visitats_1 = meta[0].voltes(cotxe_huma_1,marcador1,trams_visitats_1,par)
        trams_visitats_2 = meta[0].voltes(cotxe_huma_2,marcador2,trams_visitats_2,par)

        for c in cotxes_automatics:
            c.mou(carretera)

        cotxe_huma_1.pinta(w1,wv1)
        cotxe_huma_2.pinta(w1,wv1)
        cotxe_huma_1.pinta(w2,wv2)
        cotxe_huma_2.pinta(w2,wv2)

        for c in cotxes_automatics:
            c.pinta(w1,wv1)
            c.pinta(w2,wv2)

        

        w1.update()
        w2.update()
        time.sleep(50/1000)
    
