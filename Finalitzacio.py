from tkinter import *

def destrueixFinestra(vol_repetir,final,repeticio):
    repeticio[0]=vol_repetir
    final.destroy()

def crearFinal(dades_finals):
    final = Tk()
    final.title("Resultats finals")
    final.geometry("400x400")
    final.configure(bg="#1a1a1a")

    repeticio = [False]

    Label(final, text="FINAL DE LA PARTIDA", font=("Helvetica", 24, "bold"), 
          bg="#1a1a1a", fg="red", pady=20).pack()

    estadistiques = Frame(final, bg="#333333", padx=20, pady=20)
    estadistiques.pack(pady=10)
    if dades_finals[0] == 4:
        Label(estadistiques, text=f"Temps Total: {dades_finals[1]} s\nVoltes Totals: {dades_finals[2]}\nMillor Volta: {dades_finals[3]}\n"
                                    f"Morts Totals: {dades_finals[4]}", font=("Consolas", 14), 
             bg="#333333", fg="white").pack(anchor="w")
    if dades_finals[0] == 2:
        Label(estadistiques, text=f"Temps Total: {dades_finals[1]} s", font=("Consolas", 14), 
             bg="#333333", fg="white").pack(anchor="w")
    if dades_finals[0] == 3:
        Label(estadistiques, text=f"Voltes Totals: {dades_finals[1]}", font=("Consolas", 14), 
             bg="#333333", fg="white").pack(anchor="w")
        
    Button(final, text="Jugar de nou", font=("Helvetica", 14, "bold"),
           bg="#00FF00", fg="black", activebackground="#00CC00",
           width=20, cursor="hand2",
           command=lambda: destrueixFinestra(True, final, repeticio)).pack(pady=20)

    Button(final, text="Tancar el joc", font=("Helvetica", 12),
           bg="#333333", fg="white", activebackground="red",
           width=20, cursor="hand2",
           command=lambda: destrueixFinestra(False, final, repeticio)).pack(pady=5)

    final.mainloop()

    return repeticio[0]