from funcions_auxiliars import *
import time


class Cotxe:
    def __init__(self,x,y,w,h,a=0,v=0,colour='black'):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.a=a
        self.v=v
        self.pos = np.array([x,y])
        self.colour = colour
        self.ultim_tram = None
        self.temps_fora_carretera = 0.00
        self.morts = 0

    def calculaPunts(self):
        a_rad = m.radians(self.a)

        punts_relatius_poligon = [(0,-self.h/2),(-self.w,-self.h/2),(-self.w,self.h/2),(0,self.h/2)]
        punts_relatius_recta = [(-0.25 * self.w,-self.h/2),(-0.25*self.w,self.h/2)]
        
        punts_rotats_poligon = [rotaPunt(a_rad,p,self.pos) for p in punts_relatius_poligon]
        punts_rotats_recta = [rotaPunt(a_rad,p,self.pos) for p in punts_relatius_recta]

        return (punts_rotats_poligon,punts_rotats_recta)
    
    def comprovaSiEstemDins(self, carretera):
        punts = self.calculaPunts()
        for tram in carretera:
            count = 0
            count_global = 0
            for p in punts[0]:
                if tram.estemDinsCarretera(p,self.colour):
                    count = count + 1
                    count_global = count
                else:
                    count = 0
            if count_global > 0:
                self.ultim_tram = tram
            if count == 4:
                break

        if self.colour == 'yellow':
            if count_global <4:
                self.a = self.a + 180
                self.pos = self.pos + angleADireccio(self.a) * (self.w+5)

        else:
            if count_global == 4:
                self.colour = 'pink'
                self.temps_fora_carretera = 0.00
            else:
                if self.temps_fora_carretera == 0.00:
                    self.temps_fora_carretera = time.time()

                temps_total = time.time() - self.temps_fora_carretera
                if temps_total >= 5:
                    self.respawn_cotxe()
                    self.temps_fora_carretera = 0.00
                else:
                    if count_global == 3:
                        self.v = self.v * 0.9
                        self.colour = 'red'
                    elif count_global == 2:
                        self.v = self.v * 0.85
                        self.colour = 'red'
                    elif count_global == 1:
                        self.v = self.v * 0.8
                        self.colour = 'red'
                    else:
                        self.v = self.v *0.75 
                        self.colour = 'red'
    
    
    def estemDinsCotxe(self,p,c):
        p_np = np.array(p)
        var = p_np - c.pos
        na_rad = -m.radians(c.a)

        var_rotat = rotaPunt(na_rad,var)

        if -c.w <= var_rotat[0] <= 0 and -c.h/2 <= var_rotat[1] <=c.h/2:
            return True
        else:
            return False


    def colisioCotxes(self,cotxes_automatics):
        punts = self.calculaPunts()

        for c in cotxes_automatics:
            vector_distancia = self.pos - c.pos
            distancia = np.linalg.norm(vector_distancia)
            if distancia<self.w+c.w+2:
                for p in punts[0]:
                    punt_a_dins = False
                    if self.estemDinsCotxe(p,c):
                        punt_a_dins = True
                        break
                if punt_a_dins:
                    return True
                
        return False
                    
    def respawn_cotxe(self):
        angle = 90 + self.ultim_tram.a
        posicio = self.ultim_tram.pos + angleADireccio(angle) * self.ultim_tram.h/2
        self.pos = posicio
        self.v = self.v * 0.2
        self.a = self.ultim_tram.a
        self.morts = self.morts + 1

    def mou_gir_huma(self,par):
        if self.v != 0:
            if par==1:
                self.a = self.a + 5
            if par==-1:
                self.a = self.a - 5
    
    def mou_translacio_huma(self,par,carretera,cotxes_automatics,trams_visitats,w,wv):
        posicio_antiga = self.pos.copy()
        self.comprovaSiEstemDins(carretera)
        if self.ultim_tram is not None:
            i = self.ultim_tram.id - 1
            trams_visitats[i] = True
            if self.colisioCotxes(cotxes_automatics):
                self.respawn_cotxe()
        if par==1:
            if self.v<=10:
                self.v = self.v + 0.15
            self.pos = self.pos + angleADireccio(self.a) * self.v

        if par==-1:
            if self.v>0:
                self.v=self.v - 0.4
            if self.v>=-2:
                self.v = self.v - 0.1
            self.pos = self.pos + angleADireccio(self.a) * self.v

        if par==0:
            if self.v>-0.5 and self.v<0.5:
                self.v=0
                self.pos = self.pos + angleADireccio(self.a) * self.v
            if self.v<0:
                self.pos = self.pos + angleADireccio(self.a) * self.v
                self.v=self.v + 0.1
            if self.v>0:
                self.pos = self.pos + angleADireccio(self.a) * self.v
                self.v=self.v - 0.2

        diff = self.pos - posicio_antiga
        wv.translateWindow(diff[0],diff[1])
        return trams_visitats

    def mou(self,carretera):
        self.comprovaSiEstemDins(carretera)
        self.pos=self.pos + angleADireccio(self.a)*self.v

    def pinta(self,w,wv):
        punts = self.calculaPunts()
        wTV_punts_poligon = [wv.worldToViewXY(p[0],p[1]) for p in punts[0]]
        punts_finals_poligon = []
        for p in wTV_punts_poligon:
            punts_finals_poligon.append([p.x,p.y])

        w.create_polygon(punts_finals_poligon,outline='black', fill=self.colour)
        
        wTV_punts_recta = [wv.worldToViewXY(p[0],p[1]) for p in punts[1]]
        punts_finals_recta = []
        for p in wTV_punts_recta:
            punts_finals_recta.append([p.x,p.y])

        w.create_line(punts_finals_recta)
