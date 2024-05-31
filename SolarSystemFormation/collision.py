from vpython import *
canvas(width=1080, height=900, background=color.black,align="left")

# Plots
g1 = graph(title="linear momemtum",xtitle="t",ytitle="p.x",align="right")
fp1 = gcurve(color=color.green, graph=g1)
fp2 = gcurve(color=color.blue, graph=g1)
fptot = gcurve(color=color.red, graph=g1)

g2 = graph(title="angular momemtum",xtitle="t",ytitle="L.x",align="right")
fL1 = gcurve(color=color.green,graph=g2)
fL2 = gcurve(color=color.blue,graph=g2)
fLtot = gcurve(color=color.red,graph=g2)

# ball colision test
R = 0.01
M = 0.1
k = 200
G = 0.01
v0 = 0.1
C = 0.3 #Drag coeficient

b1 = sphere(pos=vec(0,0,0), radius=R, color=color.yellow, m = M, make_trail=True)
b2 = sphere(pos=vec(4*R,R,0), radius=R, color=color.red, m = M, make_trail=True)

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

    if collide(b1,b2):
        vrel = b2.p/b2.m -b1.p/b1.m
        vr = norm(r)*dot(vrel,norm(r))
        b1.F = b1.F + norm(r)*k*(mag(r) - (b1.radius + b2.radius)) + vr*C
        b2.F = b2.F - norm(r)*k*(mag(r) - (b1.radius + b2.radius)) - vr*C
    
    b1.p = b1.p + b1.F*dt
    b2.p = b2.p + b2.F*dt

    b1.pos = b1.pos + b1.p*dt/b1.m
    b2.pos = b2.pos + b2.p*dt/b2.m
    t = t + dt

#   Graficos
    L1 = cross(b1.pos,b1.p)
    L2 = cross(b2.pos,b2.p)

#   momento linear
    fp1.plot(t,b1.p.x)
    fp2.plot(t,b2.p.x)
    fptot.plot(t,b1.p.x + b2.p.x)

#   momento angular
    fL1.plot(t,L1.z)
    fL2.plot(t,L2.z)
    fLtot.plot(t,L1.z + L2.z)
