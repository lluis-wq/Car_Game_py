from tkinter import *
from animacio import *

def destrueixFinestra(jugadors_escollit, menu, jugadors):
    jugadors[0] = jugadors_escollit
    menu.destroy()


def crearSeleccions():
    menu = Tk()
    menu.title("Selecció de Mode")
    menu.geometry("400x400")
    menu.configure(bg="#1a1a1a")
    jugadors = [0]

    titol = Label(menu, text="JOC COTXES", font=("Helvetica", 24, "bold"), 
                   bg="#1a1a1a", fg="#00FF00", pady=20)
    titol.pack()

    subtitol = Label(menu, text="Selecciona el nombre de Jugadors:", font=("Helvetica", 12), 
                      bg="#1a1a1a", fg="white", pady=10)
    subtitol.pack()

    btn1 = Button(menu, text="1 Jugador", font=("Helvetica", 14),
                  bg="#333333", fg="white", activebackground="#00FF00",
                  width=25, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(1, menu, jugadors))
    btn1.pack(pady=5)

    btn2 = Button(menu, text="2 Jugadors", font=("Helvetica", 14),
                  bg="#333333", fg="white", activebackground="yellow",
                  width=25, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(2, menu, jugadors))
    btn2.pack(pady=5)

    peu_de_pagina = Label(menu, text="Pulsa per seleccionar", font=("Arial", 8), 
                   bg="#1a1a1a", fg="gray", pady=20)
    peu_de_pagina.pack(side=BOTTOM)

    menu.mainloop()

    return jugadors[0]