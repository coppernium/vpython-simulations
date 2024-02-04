from vpython import *
canvas(width=1900, height=930, background=color.black)

# ball colision test
R = 0.01
M = 0.1
k = 200
G = 0.01
v0 = 0.1

b1 = sphere(pos=vec(0,0,0), radius=R, color=color.yellow, m = M, make_trail=True)
b2 = sphere(pos=vec(4*R,R/0.5,0), radius=R, color=color.red, m = M, make_trail=True)

b1.p = vec(1,0,0)*v0*0*b1.m
b2.p = vec(-1,0,0)*v0*1.5*b2.m

t = 0
dt = 0.001

def collide(b1,b2):
    r = b2.pos - b1.pos
    if mag(r) < b1.radius+b2.radius:
        return(True)
    else:
        return(False)

def setcollide(b1,b2):
    r = b2.pos - b1.pos
    ptot = b1.p + b2.p
    b2.pos = b1.pos + norm(r)*(b1.radius + b2.radius)
    b1.p = ptot*b1.m/(b1.m+b2.m)
    b2.p = ptot*b2.m/(b1.m+b2.m)

while t<10:
    rate(100)
    r = b2.pos - b1.pos
    b1.F = + norm(r)*G*b1.m*b2.m/mag(r)**2
    b2.F = - norm(r)*G*b1.m*b2.m/mag(r)**2

    if collide(b1,b2)==True:
        b1.F = b1.F + norm(r)*k*(mag(r) - (b1.radius + b2.radius))
        b2.F = b2.F - norm(r)*k*(mag(r) - (b1.radius + b2.radius))
    
    b1.p = b1.p + b1.F*dt
    b2.p = b2.p + b2.F*dt

    b1.pos = b1.pos + b1.p*dt/b1.m
    b2.pos = b2.pos + b2.p*dt/b2.m
    t = t + dt
