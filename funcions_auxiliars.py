import numpy as np
import math as m

def matriuRotacio(angle):
    cos=m.cos(angle)
    sin=m.sin(angle)
    matriu_rot = np.array([[cos,-sin],[sin,cos]])
    return matriu_rot

def rotaPunt(angle,p,q=(0,0)):
    p_np = np.array(p)
    q_np = np.array(q)
    pos_rotat = q_np + matriuRotacio(angle) @ p_np
    return (pos_rotat)

def angleADireccio(angle):
    angle_rad = m.radians(angle)
    cos=m.cos(angle_rad)
    sin=m.sin(angle_rad)
    return np.array([cos,sin])

def trobaCentre(p,q):
    p_np = np.array(p)
    q_np = np.array(q)
    c = p_np - q_np
    p_centre = q_np + c/2
    return p_centre