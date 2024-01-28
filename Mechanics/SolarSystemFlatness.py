from vpython import *
canvas(width=1900, height=930, background=color.black)

# Constantes

m = 0.1
G = 10
R = 0.05
Rstart = 1
dpos = vec(2*random()-1,2*random()-1,2*random()-1)
dpos1 = vec(2*random()-1,2*random()-1,2*random()-1)

b1 = sphere(pos=dpos*Rstart, radius = R, make_trail=True)
b2 = sphere(pos=dpos1*Rstart, radius = R, make_trail=True)

b1.m = m
b2.m = m

v0 =1
b1.p = dpos*b1.m*v0
b2.p = dpos1*b2.m*v0

t = 0
k = 10
dt = 0.01

def collide(b1, b2):
    # return true if collide false if they don't
    r = b1.pos - b2.pos
    if mag(r) < b1.radius + b2.radius:
        return True
    else:
        return False

while t <10:
    rate(1000)
    r = b2.pos - b1.pos
    # Força gravitacional
    b1.F = norm(r)*G*b1.m*b2.m/mag(r)**2 # Curiosamente o vetor sempre tem que ficar na frente da mult!
    b2.F = -norm(r)*G*b1.m*b2.m/mag(r)**2
    
    # Força elastica
    if collide(b1,b2):
        b1.F = b1.F + k*(mag(r) - 2*R)*norm(r)
        b2.F = b2.F - k*(mag(r) - 2*R)*norm(r)

    b1.p = b1.p + b1.F*dt
    b2.p = b2.p + b2.F*dt

    if collide(b1,b2):
        ptot = b1.p + b2.p
        vtot = ptot(b1.m * b2.m)
        b1.p = vtot*b1.m
        b2.p = vtot*b2.m

    b1.pos = b1.pos + b1.p*dt/b1.m
    b2.pos = b2.pos + b2.p*dt/b2.m
    t = t + dt
