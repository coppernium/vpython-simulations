from vpython import *
canvas(width=1880, height=900, background=color.black,align="left")

# Graficos
g1 = graph(title="linear momemtum",xtitle="t",ytitle="p.x",align="right")
fptot = gcurve(color=color.red, graph=g1)


# Constants
Rstart = 2
R = 0.01
m = 0.1
G = 0.01
k = 200
C = 0.3
w = vec(0,0.4,0)

t = 0
dt = 0.01

#
bs = []
N = 200
n = 0

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

while n != N:
    rt = vec(2*random()-1, 2*random()-1,2*random()-1)*Rstart
    if mag(rt)<Rstart:
        bs = bs + [sphere(pos=rt, radius=R, color=color.white)]
        n = n + 1

for b in bs:
    b.m = m
    rxz = vec(b.pos.x,0,b.pos.z)
    vt = cross(w,rxz)
    b.p = vt*b.m

while t<100:
    rate(1000)
    ptot = vec(0,0,0)
    for i in range(len(bs)):
        bs[i].F = vec(0,0,0)
        for j in range(len(bs)):
            if i !=j:
                rt = bs[i].pos - bs[j].pos
                bs[i].F = bs[i].F - norm(rt)*G*bs[i].m*bs[j].m/mag(rt)
                if collide(bs[i], bs[j]):
                    setcollide(bs[i], bs[j])

    for b in bs:
        ptot = ptot + b.p
        b.p = b.p + b.F*dt
        b.pos = b.pos + b.p*dt/b.m

    
    fptot.plot(t,mag(ptot))
    t = t + dt
