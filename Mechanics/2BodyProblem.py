from vpython import *
canvas(width=1900, height=930, background=color.black)

# Constantes
M = 10e24
G = 6.674e-11
AU = 1.495e11
R = AU/50
dt = 3600
t = 0


b1 = sphere(pos=vec(0,0,0), radius=R, color=color.blue, m = 1.989e30, make_trail=True)
b2 = sphere(pos=vec(57.909e9,0,0), radius=R, color=color.red, m = 0.3301*M, make_trail=True)

cm_pos = (b1.pos*b1.m + b2.pos*b2.m)/(b1.m + b2.m)
cm = sphere(vec=cm_pos, radius=R/5, color=color.white, make_trail=True)

v0 = 47.36e3 

b1.p = vec(0,0,0)*b1.m
b2.p = vec(0,1,0)*b2.m*v0

while t<dt*1e6:
    rate(100)
    r = b2.pos - b1.pos
    F = norm(r)*G*b1.m*b2.m/mag(r)**2
    
    b1.p = b1.p + F*dt
    b2.p = b2.p - F*dt

    b1.pos = b1.pos + b1.p*dt/b1.m
    b2.pos = b2.pos + b2.p*dt/b2.m
    t = t + dt
