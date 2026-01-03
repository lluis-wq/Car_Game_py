from funcions_auxiliars import *
import time

class Meta:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.pos = np.array([x,y])


    def calculaPunts(self):
        return [(self.x,self.y),(self.x,self.y+self.w),(self.x+self.h,self.y+self.w),(self.x+self.h,self.y)]
    
    def toquemMeta(self,c,num_voltes):
        punts = c.calculaPunts()
        marge = 0
        if num_voltes > 0 and num_voltes == c.volta:
            marge = 5
        for p in punts[0]:
            if self.x + marge < p[0] < self.x+self.h and self.y < p[1] < self.y+self.w:
                return True
            
        return False


    def voltes(self,c,marcador,trams_visitats,par,num_escollit):
        if par == 2:
            num_voltes = num_escollit
        else:
            num_voltes = 0
        num_vides = num_escollit
        
        tM = self.toquemMeta(c,num_voltes)
        temps_actual = time.time()
        final_mode_carrera = False
        if tM == True:
            if c.volta == 0:
                print("Comencem la partida")
                c.t_inicial = temps_actual
                c.t_inicial_volta = temps_actual
                trams_visitats = [False for _ in range(12)]
                c.volta = 1
            else:
                count_trams_visitats = 0
                for i in range(12):
                    if trams_visitats[i] == True:
                        count_trams_visitats = count_trams_visitats + 1

                if count_trams_visitats == 12:
                    c.volta = c.volta + 1
                    trams_visitats = [False for _ in range(12)]
                    c.t_ultima_volta = temps_actual - c.t_inicial_volta
                    c.t_inicial_volta = temps_actual
                    if par == 2:
                        if num_voltes <= c.volta - 1:
                            final_mode_carrera = True

            
        if c.volta>0:
                temps_total_actual = round(temps_actual - c.t_inicial,2)
                temps_total_volta = round(temps_actual - c.t_inicial_volta,2)
                temps_ultima_volta = round(c.t_ultima_volta,2)
                c.t_totes_les_voltes.append(temps_ultima_volta)
                temps_millor_volta = max(c.t_totes_les_voltes)
                if par == 1 or par == 4:
                    marcador.configure(text = f" Temps Total: {temps_total_actual}\n Temps Volta: {temps_total_volta} \nVoltes: {c.volta - 1}\n"
                                       f"Temps Volta Anterior: {temps_ultima_volta}\nTemps Millor Volta: {temps_millor_volta}\n Morts: {c.morts}")
                    if par == 4:
                        return [4,temps_total_actual,c.volta-1,temps_millor_volta,c.morts]
                if par == 2 or par == 5:
                    marcador.configure(text = f" Temps Total: {temps_total_actual}\nVoltes: {c.volta-1}/{num_voltes}")
                    if final_mode_carrera == True:
                        return [2,temps_total_actual,c.volta-1]
                if par == 3 or par == 6:
                    vides = num_vides - c.morts
                    marcador.configure(text = f" Temps Total: {temps_total_actual}\nVoltes: {c.volta - 1}\nVides: {vides}")
                    if vides == 0:
                        return [3,c.volta-1]
        return trams_visitats

        

    def pinta(self,w,wv):
        punts = self.calculaPunts()
        wTV_punts_poligon = [wv.worldToViewXY(p[0],p[1]) for p in punts]
        punts_finals_poligon = []
        for p in wTV_punts_poligon:
            punts_finals_poligon.append([p.x,p.y])

        w.create_polygon(punts_finals_poligon,outline='black', fill='white')
