from tkinter import *

def destrueixFinestra(vol_repetir,final,repeticio):
    repeticio[0]=vol_repetir
    final.destroy()

def crearFinal(dades_finals,num_jugadors):
    final = Tk()
    final.title("Resultats finals")
    final.geometry("400x420")
    final.configure(bg="#1a1a1a")

    repeticio = [False]


    estadistiques = Frame(final, bg="#333333", padx=20, pady=20)
    estadistiques.pack(pady=10)
    if num_jugadors == 1:
        if dades_finals[0] == 4:
            Label(final, text="RESULTATS TOTALS", font=("Helvetica", 24, "bold"), 
                    bg="#1a1a1a", fg="blue", pady=20).pack()
            
            Label(estadistiques, text=f"Temps Total: {dades_finals[1]} s\nVoltes Totals: {dades_finals[2]}\nMillor Volta: {dades_finals[3]}\n"
                                        f"Morts Totals: {dades_finals[4]}", font=("Consolas", 14), 
                bg="#333333", fg="white").pack(anchor="w")
        if dades_finals[0] == 2:
            Label(final, text="FINAL DE LA CARRERA", font=("Helvetica", 24, "bold"), 
                bg="#1a1a1a", fg="green", pady=20).pack()
            
            Label(estadistiques, text=f"Temps Total: {dades_finals[1]} s", font=("Consolas", 14), 
                bg="#333333", fg="white").pack(anchor="w")
        if dades_finals[0] == 3:
            Label(final, text="FINAL DE LA PARTIDA", font=("Helvetica", 24, "bold"), 
                bg="#1a1a1a", fg="red", pady=20).pack()
            
            Label(estadistiques, text=f"Voltes Totals: {dades_finals[1]}", font=("Consolas", 14), 
                bg="#333333", fg="white").pack(anchor="w")
            
        
    if num_jugadors == 2:
        if dades_finals[0] == 4:
            Label(final, text="RESULTATS TOTALS", font=("Helvetica", 20, "bold"), 
                    bg="#1a1a1a", fg="blue", pady=20).pack()
            
            Label(estadistiques, text=f"Jugador 1 (Cotxe Blau, WASD)\nTemps Total: {dades_finals[1]} s\nVoltes Totals: {dades_finals[2]}\nMillor Volta: {dades_finals[3]}\n"
                                        f"Morts Totals: {dades_finals[4]}\n\n"
                                        f"Jugador 2 (Cotxe Verd, Fletxes)\nTemps Total: {dades_finals[6]} s\nVoltes Totals: {dades_finals[7]}\nMillor Volta: {dades_finals[8]}\n"
                                        f"Morts Totals: {dades_finals[8]}", font=("Consolas", 10), 
                bg="#333333", fg="white").pack(anchor="w")
        if dades_finals[0] == 2:
            guanyador = 0
            color = None
            if dades_finals[2] > dades_finals[5]:
                guanyador = 1
                color = 'verd'
            else:
                guanyador = 2
                color = 'blau'

            Label(final, text=f"FINAL DE LA CARRERA!\nEl guanyador és el jugador {guanyador}\n amb el color {color}.", font=("Helvetica", 18, "bold"), 
                    bg="#1a1a1a", fg="green", pady=20).pack()
            Label(estadistiques, text=f"Temps Total: {dades_finals[1]} s", font=("Consolas", 10), 
                bg="#333333", fg="white").pack(anchor="w")
        if dades_finals[0] == 3:
            Label(estadistiques, text=f"Jugador 1 (Cotxe Blau, WASD)\nVoltes Totals: {dades_finals[1]}\n"
                                        f"Jugador 2 (Cotxe Verd, Fletxes)\nVoltes Totals: {dades_finals[3]}", font=("Consolas", 10), 
                bg="#333333", fg="white").pack(anchor="w")
            
    btn1 = Button(final, text="Jugar de nou", font=("Helvetica", 14, "bold"),
            bg="#00FF00", fg="black", activebackground="#00CC00",
            width=20, cursor="hand2",
            command=lambda: destrueixFinestra(True, final, repeticio))
    btn1.pack(pady=20)
        

    btn2 = Button(final, text="Tancar el joc", font=("Helvetica", 12),
            bg="#333333", fg="white", activebackground="red",
            width=20, cursor="hand2",
            command=lambda: destrueixFinestra(False, final, repeticio))
    btn2.pack(pady=5)
    
    final.mainloop()

    return repeticio[0]