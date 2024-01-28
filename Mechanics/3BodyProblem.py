from vpython import *
import numpy as np
canvas(width=1900, height=930, background=color.black)

G = 6.67e-11
M = 2e30
AU = 1.496e11
Rs = AU/100
Ro = AU/10
v0 = sqrt(5*G*M/(4*Ro))
Rp = np.cbrt(3*G*M*(Ro**2)/v0**2)
m = 1000

s1 = sphere(pos=vec(0,0,0), radius = Rs, color=color.red, make_trail=True)
s2 = sphere(pos=vec(Ro,0,0), radius = Rs, color=color.green, make_trail=True)
s3 = sphere(pos=vec(-Ro,0,0), radius = Rs, color=color.blue, make_trail=True)
p1 = sphere(pos=vec(Rp,0,0), radius = Rs/5, color = color.white, make_trail=True)

s1.p = vec(0,0,0)*M
s2.p = vec(0,-1,0)*M*v0
s3.p = vec(0,1,0)*M*v0
p1.p = vec(0,1,0)*m*v0*Rp/Ro

t = 0
dt = 3600 # 1 hour

while t<100*24*3600:
    rate(100)

    r12 = s2.pos - s1.pos
    r13 = s3.pos - s1.pos 
    r23 = s3.pos - s2.pos 

    r1p = p1.pos - s1.pos
    r2p = p1.pos - s2.pos
    r3p = p1.pos - s3.pos

    F12 = -norm(r12)*G*M*M/mag(r12)**2
    F13 = -norm(r13)*G*M*M/mag(r13)**2
    F23 = -norm(r23)*G*M*M/mag(r23)**2
    p1.F = -norm(r1p)*G*M*m/mag(r1p)**2 + norm(r2p)/mag(r2p)**2 + norm(r3p)/mag(r3p)**2

    s1.F = - F12 - F13
    s2.F = + F12 - F23
    s3.F = + F13 + F23

    s1.p = s1.p + s1.F*dt
    s2.p = s2.p + s2.F*dt
    s3.p = s3.p + s3.F*dt
    p1.p = p1.p + p1.F*dt

    s1.pos = s1.pos + s1.p*dt/M
    s2.pos = s2.pos + s2.p*dt/M
    s3.pos = s3.pos + s3.p*dt/M
    p1.pos = p1.pos + p1.p*dt/m

    t = t + dt
