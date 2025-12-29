from funcions_auxiliars import *


class Carretera:
    def __init__(self,x,y,a,h,d,id,colour='light grey'):
        self.id=id
        self.x=x
        self.y=y
        self.a=a
        self.h=h
        self.d=d
        self.pos=np.array([x,y])
        self.colour=colour

    def estemDinsCarretera(self,p,colour='pink'):
        p_np = np.array(p)
        var = p_np - self.pos
        na_rad = -m.radians(self.a)

        var_rotat = rotaPunt(na_rad,var)
        marge = 30
        if colour == 'yellow':
            marge = 0

        if -marge <= var_rotat[0] <= self.d+marge and 0 <= var_rotat[1] <= self.h:
            return True
        else:
            return False


    
    def calculaPunts(self):
        a_rad = m.radians(self.a)

        punts_relatius_carretera = [(0,0),(0,self.h),(self.d,self.h),(self.d,0)]
        punts_rotats_carretera = [rotaPunt(a_rad,p,self.pos) for p in punts_relatius_carretera]

        i=0
        punts_rotats_ratlles = []
        while i<self.d-10:
            ratlla = [(i,self.h/2 - 1),(i,self.h/2 + 1),(10+i,self.h/2 + 1),(10+i,self.h/2 - 1)]
            ratlla_rotada = [rotaPunt(a_rad,p,self.pos) for p in ratlla]
            punts_rotats_ratlles.append(ratlla_rotada)
            i=i+25

        return (punts_rotats_carretera,punts_rotats_ratlles)
    

    def pinta(self,w,wv,punts_previs = None):

        punts = self.calculaPunts()


        wTV_punts_carretera = [wv.worldToViewXY(p[0],p[1]) for p in punts[0]]

        punts_finals_carretera = []
        for p in wTV_punts_carretera:
            punts_finals_carretera.append([p.x,p.y])

        w.create_polygon(punts_finals_carretera, fill=self.colour)
        
        recta_1 = [punts_finals_carretera[1]]+ [punts_finals_carretera[2]]
        recta_2 = [punts_finals_carretera[0]]+ [punts_finals_carretera[3]]
        meta = [punts_finals_carretera[0]] + [punts_finals_carretera[1]] 
        w.create_line(recta_1)
        w.create_line(recta_2)

        if punts_previs is not None:
            w.create_polygon(punts_previs[1],punts_previs[0],punts_finals_carretera[1],punts_finals_carretera[0], fill=self.colour)
            recta_3 = [punts_previs[0]]+[punts_finals_carretera[1]]
            recta_4 = [punts_previs[1]]+[punts_finals_carretera[0]]
            w.create_line(recta_3)
            w.create_line(recta_4)
        
        for p in punts[1]:
            wTV_punts_ratlla = []
            for r in p:
                r_0 = float(r[0])
                r_1 = float(r[1])
                L = wv.worldToViewXY(r_0,r_1)
                wTV_punts_ratlla.append(L)
            punts_finals_ratlla = []
            for r in wTV_punts_ratlla:
                punts_finals_ratlla.append([r.x,r.y])
            w.create_polygon(punts_finals_ratlla, fill='white')

        return (punts_finals_carretera[2],punts_finals_carretera[3])

