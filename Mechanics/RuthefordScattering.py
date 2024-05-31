from vpython import *
canvas(width=1880, height=930, background=color.black)

charge = 1
mass_p = 1
mass_e = 1
G = 0.001
k = 8

R = 0.1
b1 = sphere(pos=vec(-150*R,0,0), radius=R, color=color.white, m = mass_e, make_trail=True)
b2 = sphere(pos=vec(0*R,0,0), radius=5*R, color=color.yellow, m = mass_p, make_trail=True)

b1.q = charge
b2.q = charge

v0 = 0
b1.p = vec(0,0,0)*v0*1.5*b1.m
b2.p = vec(1,0,0)*v0*0*b2.m

t = 0
dt = 0.01

while t < 1000:
    rate(1000)
    r = b2.pos - b1.pos
    b1.F = norm(r)*k*b1.q*b2.q/mag(r)**2 + norm(r)*G*b1.m*b2.m/mag(r)**2
    b2.F = norm(r)*k*b1.q*b2.q/mag(r)**2 - norm(r)*G*b1.m*b2.m/mag(r)**2

    
    b1.p = b1.p + b1.F*dt
    b2.p = b2.p + b2.F*dt

    b1.pos = b1.pos + b1.p*dt/b1.m
    b2.pos = b2.pos + b2.p*dt/b2.m

    t = t + dt

