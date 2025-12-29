from tkinter import *
from animacio import *

Noms_modes = {
    1: "Mode Lliure",
    2: "Mode Carrera",
    3: "Mode Supervivència",
    4: "Instruccions dels modes"
}

Descripcions = {
    1: "Condueix sense límits ni temps.\nIdeal per practicar.",
    2: "Completa 1 volta el més ràpid possible.\nBat el teu rècord!",
    3: "Tens 10 vides.\nSi xoques contra un cotxe o si estàs fora de la carretera per 5 segons,\n perds una vida."
}

def destrueixFinestra(mode_escollit, menu, mode):
    mode[0] = mode_escollit
    print(f"Iniciant {Noms_modes[mode_escollit]}...")
    menu.destroy()
    if mode_escollit == 4:
        guia = Tk()
        guia.title = ("Guia")
        guia.geometry("700x400")
        guia.configure(bg="#1a1a1a")
        titol = Label(guia, text="Instruccions", font=("Helvetica", 24, "bold"), 
                   bg="#1a1a1a", fg="#00FF00", pady=20)
        titol.pack()

        subtitol = Label(guia, text=f"Mode Lliure:\n{Descripcions[1]}\n\nMode Carrera:\n{Descripcions[2]}\n\nMode Supervivència:\n{Descripcions[3]}", font=("Helvetica", 12), 
                      bg="#1a1a1a", fg="white", pady=10)
        subtitol.pack()

        peu_de_pagina_guia = Label(guia, text="Tanqui la finestra per tornar a la selecció de mode", font=("Arial", 10), 
                   bg="#1a1a1a", fg="gray", pady=20)
        peu_de_pagina_guia.pack(side=BOTTOM)

        guia.mainloop()


def crearMenu():
    menu = Tk()
    menu.title("Selecció de Mode")
    menu.geometry("400x400")
    menu.configure(bg="#1a1a1a")
    mode = [0]

    titol = Label(menu, text="JOC COTXES", font=("Helvetica", 24, "bold"), 
                   bg="#1a1a1a", fg="#00FF00", pady=20)
    titol.pack()

    subtitol = Label(menu, text="Selecciona el mode de joc:", font=("Helvetica", 12), 
                      bg="#1a1a1a", fg="white", pady=10)
    subtitol.pack()

    btn1 = Button(menu, text=Noms_modes[1], font=("Helvetica", 14),
                  bg="#333333", fg="white", activebackground="#00FF00",
                  width=25, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(1, menu, mode))
    btn1.pack(pady=5)

    btn2 = Button(menu, text=Noms_modes[2], font=("Helvetica", 14),
                  bg="#333333", fg="white", activebackground="yellow",
                  width=25, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(2, menu, mode))
    btn2.pack(pady=5)

    btn3 = Button(menu, text=Noms_modes[3], font=("Helvetica", 14),
                  bg="#333333", fg="white", activebackground="red",
                  width=25, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(3, menu, mode))
    btn3.pack(pady=5)

    btn4 = Button(menu, text=Noms_modes[4], font=("Helvetica", 11),
                  bg="#333333", fg="white", activebackground="red",
                  width=20, height=2, bd=0, cursor="hand2",
                  command=lambda: destrueixFinestra(4, menu, mode))
    btn4.pack(pady=5)

    peu_de_pagina = Label(menu, text="Pulsa per seleccionar", font=("Arial", 8), 
                   bg="#1a1a1a", fg="gray", pady=20)
    peu_de_pagina.pack(side=BOTTOM)

    menu.mainloop()

    return mode[0]
