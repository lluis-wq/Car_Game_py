from funcions_auxiliars import *
import time

class Meta:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.pos = np.array([x,y])
        self.volta=0
        self.t_inicial = 0.00
        self.t_inicial_volta = 0.00
        self.t_ultima_volta = 0.00
        self.t_totes_les_voltes = []


    def calculaPunts(self):
        return [(self.x,self.y),(self.x,self.y+self.w),(self.x+self.h,self.y+self.w),(self.x+self.h,self.y)]
    
    def toquemMeta(self,c):
        punts = c.calculaPunts()
        for p in punts[0]:
            np_p = np.array(p)
            var = np_p - self.pos
            if 0 <= var[0] <= self.h and 0 <= var[1] <= self.w:
                return True
            
        return False


    def voltes(self,c,marcador,trams_visitats,par):
        tM = self.toquemMeta(c)
        temps_actual = time.time()
        final_mode_carrera = False
        if tM == True:
            if self.volta == 0:
                print("Comencem la partida")
                self.t_inicial = temps_actual
                self.t_inicial_volta = temps_actual
                trams_visitats = [False for _ in range(12)]
                self.volta = 1
            elif self.volta > 0:
                count_trams_visitats = 0
                for i in range(12):
                    if trams_visitats[i] == True:
                        count_trams_visitats = count_trams_visitats + 1

                if count_trams_visitats == 12:
                    self.volta = self.volta + 1
                    trams_visitats = [False for _ in range(12)]
                    self.t_ultima_volta = temps_actual - self.t_inicial_volta
                    self.t_inicial_volta = temps_actual
                    if par == 2:
                        final_mode_carrera = True

            
        if self.volta>0:
                temps_total_actual = round(temps_actual - self.t_inicial,2)
                temps_total_volta = round(temps_actual - self.t_inicial_volta,2)
                temps_ultima_volta = round(self.t_ultima_volta,2)
                self.t_totes_les_voltes.append(temps_ultima_volta)
                temps_millor_volta = max(self.t_totes_les_voltes)
                if par == 1 or par == 4:
                    marcador.configure(text = f" Temps Total: {temps_total_actual}\n Temps Volta: {temps_total_volta} \nVoltes: {self.volta - 1}\n"
                                       f"Temps Volta Anterior: {temps_ultima_volta}\nTemps Millor Volta: {temps_millor_volta}\n Morts: {c.morts}")
                    if par == 4:
                        return [4,temps_total_actual,self.volta-1,temps_millor_volta,c.morts]
                if par == 2 or par == 5:
                    marcador.configure(text = f" Temps Total: {temps_total_actual}")
                    if final_mode_carrera == True or par == 5:
                        return [2,temps_total_actual]
                if par == 3 or par == 6:
                    vides = 10 - c.morts
                    marcador.configure(text = f" Temps Total: {temps_total_actual}\nVoltes: {self.volta - 1}\nVides: {vides}")
                    if vides == 0 or par == 6:
                        return [3,self.volta-1]
        return trams_visitats

        

    def pinta(self,w,wv):
        punts = self.calculaPunts()
        wTV_punts_poligon = [wv.worldToViewXY(p[0],p[1]) for p in punts]
        punts_finals_poligon = []
        for p in wTV_punts_poligon:
            punts_finals_poligon.append([p.x,p.y])

        w.create_polygon(punts_finals_poligon,outline='black', fill='white')
